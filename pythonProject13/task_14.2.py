from tkinter import *
import tkinter as tk
from tkinter import font, ttk, messagebox, simpledialog
from PIL import Image, ImageTk, ImageDraw

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, place, work_time):
        super().__init__(restaurant_name, "мороженое")
        self.location = place
        self.time = work_time
        self.taste = {"Мороженое в стаканчике": ["Мята", "Ваниль", "Кокос", "Шоколад"], "Фруктовый лед": ["Яблоко", "Вишня", "Ананас"],"Мороженое в рожке": ["Клубника", "Фисташка", "Ваниль", "Банан"]}

    def display_flavors(self):
        return "\n".join(
            f"{ice_type.capitalize()}: {', '.join(flavors)}"
            for ice_type, flavors in self.taste.items()
        )

    def add_flavor_to_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if flavor in self.taste[ice_type]:
            return "Такое мороженое уже есть в списке"
        else:
            self.taste[ice_type].append(flavor)
            return "Добавлен новый вкус"

    def delete_flavor_from_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if ice_type in self.taste and flavor in self.taste[ice_type]:
            self.taste[ice_type].remove(flavor)
            return "Мороженое успешно удалено"
        else:
            return "Ошибка. Мороженое не найдено"

    def find_flavor_in_types(self, flavor):
        flavor = flavor.lower()
        for ice_type, flavors in self.taste.items():
            if flavor in (f.lower() for f in flavors):  # Проверяем наличие вкуса в списке
                return f"Мороженое '{flavor}' есть в '{ice_type}'."
        return "Ошибка. Мороженое не найдено."

    def add_new_type(self, ice_type):
        if ice_type in self.taste:
            return "Такое мороженое уже есть в списке"
        else:
            self.taste[ice_type] = []
            return "Добавлено новое мороженое"


stand = IceCreamStand("Cute Kitty Ice","Южный парк", "8:00-20:00")
root = tk.Tk()
root.title("Cute Kitty Ice")
root.geometry("720x570")
img = Image.open("background_image.png") # фон
bcg = ImageTk.PhotoImage(img)
background_label = Label(root, image=bcg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

roof_canvas = tk.Canvas(root, width=440, height=100, bg="#f5d5e4", highlightthickness=0) # нежно розовый квадрат
roof_canvas.pack()
roof_canvas.create_text(220, 50, text="Cute Kitty Ice", font=("Helvetica", 40), fill="#F81894") #текст

text_display = tk.Text( width=40, height=8, bg="#fff", fg="#000000", font=(10))
text_display.pack(padx=10, pady=20)

frame_buttons = tk.Frame(root, bg="#4F311C") #корич
frame_buttons.pack(pady=70)

def update_display():
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, stand.display_flavors())

def add_flavor():
    taste = simpledialog.askstring("Добавить новый тип", "Введите тип мороженого:")
    flavor = simpledialog.askstring("Добавить новый вкус", "Введите вкус:")
    if taste and flavor:
        msg = stand.add_flavor_to_type(taste.lower(), flavor.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def delete_flavor():
    taste = simpledialog.askstring("Добавить тип", "Введите тип мороженого:")
    flavor = simpledialog.askstring("Удалить вкус", "Введите вкус:")
    if taste and flavor:
        msg = stand.delete_flavor_from_type(taste.lower(), flavor.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def add_type():
    taste = simpledialog.askstring("Добавить новый тип", "Введите новый тип мороженого:")
    if taste:
        msg = stand.add_new_type(taste.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def find_flavor():
    flavor = simpledialog.askstring("Поиск вкуса", "Введите вкус:")
    if flavor:
        msg = stand.find_flavor_in_types(flavor.lower())
        messagebox.showinfo("Результат", msg)

tk.Button(frame_buttons, text="Добавить новый вкус", fg="#FFFFFF", command=add_flavor, bg="#F81894").grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame_buttons, text="Удалить вкус",fg="#FFFFFF", command=delete_flavor, bg="#d71868").grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_buttons, text="Добавить новый тип", fg="#FFFFFF", command=add_type, bg="#F81894").grid(row=0, column=2, padx=10, pady=10)
tk.Button(frame_buttons, text="Найти вкус", fg="#FFFFFF", command=find_flavor, bg="#F81894").grid(row=0, column=3, padx=5, pady=5)

update_display()
root.mainloop()