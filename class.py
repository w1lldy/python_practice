class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    # Метод экземпляра
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    # Другой метод экземпляра
    def speak(self, sound):
        return f"{self.name} says {sound}"
lion = Dog("Lion", 5, any)
#print(lion)
#print(lion.speak("Gaf gaf epta"))
philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.") 