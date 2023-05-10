# class Grandparent:
#     def about(self):
#         print("I am GrandParent")
#     def about_myself(self):
#         print("I am Grandparent")
# class Parent(Grandparent):
#     def about_myself(self):
#         print("I am Parent")
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
# nick = Child()

class Mam:
    def __init__(self):
        self.hair = "Dark brown"
        self.eyes = "Grey-green"
        self.height = 172
class Dad:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hair1 = "Black"
        self.eyes = "Hazel"
        self.height = 173
class Child(Dad, Mam):
    def print_info(self):
        print(f"Hair: {self.hair}")
        print(f"Eyes: {self.eyes}")
        print(f"Height: {self.height}")
child = Child()
child.print_info()