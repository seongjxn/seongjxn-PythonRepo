class Bird:
    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")

class Sparrow (Bird):
    def birdsong(self):
        print("짹짹")

class Chicken(Bird) :
    pass

class Shape :
    def __init__(self) -> None:
        self.x = int(input())