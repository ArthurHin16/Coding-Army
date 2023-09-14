"""
Write a Python program to create a person class. Include attributes like name, 
country and date of birth. Implement a method to determine the person's age. 
"""
import datetime
class Person():
    def __init__(self, name, country, day_of_birth, month_of_birth, year_of_birth):
        self.name = name
        self.country = country
        self.day = day_of_birth
        self.month = month_of_birth
        self.year = year_of_birth
        
    
    def calculate_age(self):
        today = datetime.date.today()
        year = today.year
        day = today.day
        month = today.month
        age = year - self.year
        
        if self.month == month and self.day > day:
            age -= 1  

        elif self.month > month:
            age -= 1 
        
        return age
    
person1 = Person('Osmanis', 'Cuba', 8, 7, 1969)
person1_age = person1.calculate_age()
print(person1_age)
