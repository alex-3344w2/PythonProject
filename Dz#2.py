# print("hello world")
import random
class Student:
    def __init__(self, name):
        self.name = name
        self.money = 500
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_work(self):
        print("Need money")
        self.gladness -= 3
        self.progress -= 0.05
        self.money += 200

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3
        self.money -= 50


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 100

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money < 50:
            print("Got fired…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money} $")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        if self.money < 150:
            self.to_work()
        elif self.gladness < 10:
            self.to_chill()
        elif self.progress < -0.25:
            self.to_study()
        elif self.progress > 3.5:
            self.to_chill()
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                self.to_work()
            self.end_of_day()
            self.is_alive()

nick = Student(name="Nick")
kate = Student(name="Kate")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)

# #
# #
# #
# #
#
#
# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         self.money = 3000
#         print(self)
#
# nick = Student()
# nick1 = Student()
# # print(nick.money,"$")
# print(nick)
