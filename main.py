class Najaf:
    def __init__(self):
        print("parent class is ready!")
    def who(self):
        print("my father")
    def work(self):
        print("he is a teacher")
class Orhan(Najaf):
    def __init__(self):
        super().__init__()
        print("child is ready")
    def whoisthis(self):
        print("it is my little brother")
    def work(self):
        print("he is a baby")
#object
child = Orhan()
child.whoisthis()
child.work()
child.who()