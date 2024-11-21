import statistics

class Person:
    def __init__(self,name,age,contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def set_details(self,name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number

    def get_details(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Contact Number: {self.contact_number}""" 
    
class Member(Person):
    def __init__(self, name, age, contact_number):
        super().__init__(name, age, contact_number)
        self.membership_id = ''
        self.sport = ''
        self.performance_scores = []

    def set_member_details(self,membership_id, sport):
        self.membership_id = membership_id
        self.sport = sport

    def add_performance_score(self,score):
        (self.performance_scores).append(score)

    def calculate_average_score():

