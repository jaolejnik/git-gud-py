class Person:
    def __init__(self, first_name, last_name, age, country, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.job = job

    def say_name(self):
        print(f"My name is {self.first_name} .")

    def say_age(self):
        pass

    def say_country(self):
        pass

    def say_job(self):
        pass

    def introduction(self):
        print("Hello!")
