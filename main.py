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

    def calculate_average_score(self):
        if self.performance_scores == []:
            return 0
        return round(statistics.mean(self.performance_scores),2)
    
    def get_member_summary(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Contact Number: {self.contact_number}
        Sport: {self.sport}
        Membership Id: {self.membership_id}
        Average Performance Score: {self.calculate_average_score()}
""" 
    
class Coach(Person):
    def __init__(self, name, age, contact_number):
        super().__init__(name, age, contact_number)
        self.coach_id = ''
        self.specialisation = ''
        self.salary = ''
        self.mentees = []

    def set_coach_details(self, coach_id, specialisation, salary):
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary

    def assign_mentee(self,member):
        self.mentees.append(member)
        print(f"Coach {self.name} is now mentoring {member.name} in {member.sport}.")

    def get_mentees(self):
        l = []
        for x in self.mentees:
            l.append(f"{x.name} who does {x.sport}")
        return l

    def increase_salary(self,percentage):
        self.salary = (self.salary * percentage / 100) + self.salary

    def get_coach_summary(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Contact Number: {self.contact_number}
        Coach ID: {self.coach_id}
        Specialisation: {self.specialisation}
        Salary: {self.salary}
        Mentees: {self.get_mentees()}
""" 

class Staff(Person):
    def __init__(self, name, age, contact_number):
        super().__init__(name, age, contact_number)
        self.staff_id = ''
        self.position = ''
        self.years_of_service = 0

    def set_staff_details(self,staff_id, position, years_of_service):
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service

    def increment_years_of_service(self):
        self.years_of_service += 1

    def assist_member(self,member):
        print(f"Staff {self.name} assisted {member.name} in resolving an issue.")
    
    def get_staff_summary(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Contact Number: {self.contact_number}
        Staff ID: {self.staff_id}
        Position: {self.position}
        Years of service: {self.years_of_service}
""" 

Member1 = Member("Armeen",17,"07435612325")
Member1.set_member_details("A123","Basketball")
Member2 = Member("Eli",19,"07123482634")
Member2.set_member_details("F312","Football")

Coach1 = Coach("Alice",32,"072342918235")
Coach1.set_coach_details("L098","Basketball",40000)
Coach2 = Coach("John",49,"077523256876")
Coach2.set_coach_details("D142","Football",55000)

Staff1 = Staff("Will",59,"07835425646")
Staff1.set_staff_details("F142","Club CEO",25)

Coach1.assign_mentee(Member1)
Member1.add_performance_score(10)
Member1.add_performance_score(5)
Member1.add_performance_score(7)
Member1.add_performance_score(9)
Staff1.assist_member(Member2)
Coach1.increase_salary(15)
Staff1.increment_years_of_service()

print(
Coach1.get_coach_summary(),
Coach2.get_coach_summary(),
Member1.get_member_summary(),
Staff1.get_staff_summary(),
Member2.get_member_summary(),
)