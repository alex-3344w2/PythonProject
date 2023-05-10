import logging
import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.pet = pet
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_pet(self):
        self.pet = Pet(pets_list)

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)


    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "dog food":
            print("Bought dog food")
            self.money -= 70
            self.home.food_for_dog += 70
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 20
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def to_the_park(self):
        self.gladness += 20
        self.satiety -= 5
        self.pet.gladness1 += 20
        self.pet.satiety1 -= 20

    def lunch_for_the_dog(self):
        if self.home.food_for_dog <= 0:
            self.shopping("dog food")
        else:
            if self.pet.satiety1 >= 100:
                self.pet.satiety1 = 100
                return
            self.pet.satiety1 += 20
            self.home.food_for_dog -= 20

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Dog food – {self.home.food_for_dog}")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        pet_indexes = f"{self.pet.dog} pet indexes"
        print(f"{pet_indexes:^50}", "\n")
        print(f"Satiety – {self.pet.satiety1}")
        print(f"Gladness – {self.pet.gladness1}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.pet is None:
            self.get_pet()
            print(f"I bought a pet {self.pet.dog}")
        if self.car is None:
            self.get_car()
            print(f"I bought a car{self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif self.pet.satiety1 < 7:
            print("I have to feed the dog")
            self.lunch_for_the_dog()
        elif self.pet.gladness1 < 8:
            print("Gotta walk the dog")
            self.to_the_park()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")
        self.pet.run()

pets_list = {
    "Sheepdog":{"satiety1":45, "gladness1":40},
    "Spitz": {"satiety1":20, "gladness1":30},
    "Australian shepherd": {"satiety1":35, "gladness1":35},
    "Alabai": {"satiety1":50, "gladness1":40}
}

class Pet:
    def __init__(self, pets_list):
        self.dog = random.choice(list (pets_list))
        self.satiety1 = pets_list[self.dog]["satiety1"]
        self.gladness1 = pets_list[self.dog]["gladness1"]
    def lie(self):
        self.gladness1 -= 2
        self.satiety1 -= 1
    def play(self):
        self.gladness1 += 2
        self.satiety1 -= 2
    def run(self):
        run = random.randint(1, 2)
        if run == 1:
            self.lie()
        elif run == 2:
            self.play()


brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }


class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list (brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.food_for_dog = 0

job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 24 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }


class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(1,800):
    if nick.live(day) == False:
        break
