class Restaurant:
    def __init__(self, name, cuisine_type, rating=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.name} сейчас открыт!")

    def rating_obnovka(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг {self.name} обновлен до {self.rating}.")

restik_new = Restaurant("Сачмэлли", "Грузинская")
restik1 = Restaurant("Якитория", "Японская", 4.5)
restik2 = Restaurant("Хмель", "Русская", 4.3)
restik3 = Restaurant("Чеснок", "Русская", 4.7)

print(restik_new.name)
print(restik_new.cuisine_type)
restik_new.describe_restaurant()
restik_new.open_restaurant()
print()

restik1.describe_restaurant()
print()
restik2.describe_restaurant()
print()
restik3.describe_restaurant()
print()

restik_new.rating_obnovka(4.9) #обновление рейтинга ресторана
restik_new.describe_restaurant()
