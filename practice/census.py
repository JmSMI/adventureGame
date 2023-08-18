class Person:
    age = 15
    name = "Rolf"
    favourite_foods = ['beets', 'turnips', 'wesswurst']

    def __init__(self, age, name, favourite_foods):
        self.name = name
        self.age = age
        self.favourite_foods = favourite_foods

    def __str__(self):
        return "Name: {} Age: {} Food: {}".format(
            self.name,
            self.age,
            self.favourite_foods[0])

    def birth_year(self):
        return 2023 - self.age


people = [Person(15, 'Rake', ['turnips', 'peas']), Person(20, 'Tand', ['pizza', 'tomatoes', 'licorice']),
          Person(80, 'Hose', ['beans', 'meat'])]

ageSum = 0
birthSum = 0

for person in people:
    ageSum += person.age
    birthSum += person.birth_year()

print("Average age is: " + f"{(ageSum / len(people)):.0f}")
print("Average birth year is: " + f"{birthSum / len(people):.0f}")

for person in people:
    print(person)
