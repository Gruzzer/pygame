
class main_sword():
    def __init__(self):
        self.POWER=10
        self.atk_speed=1
        self.magic='none'
    def put(self):
        print("""
        POWER = %d
        atk_speed = %.1f
        magic = %s"""%(self.POWER, self.atk_speed, self.magic))
class Long_sword(main_sword):
    def __init__(self):
        print("Long_sword")
        self.POWER=int(input("POWER : "))
        self.atk_speed=float(input("atk_speed : "))
        self.magic=str(input("magic : "))
        self.skill=str(input("skill : "))
    def put(self):
        print("""
        POWER = %d
        atk_speed = %.1f
        magic = %s
        skill = %s"""%(self.POWER, self.atk_speed, self.magic,self.skill))
class short_sword(main_sword):
    def __init__(self):
        print("Short_sword")
        self.POWER = int(input("POWER : "))
        self.atk_speed = float(input("atk_speed : "))
        self.magic = str(input("magic : "))
        self.skill = str(input("skill : "))
    def put(self):
        print("""
        POWER = %d
        atk_speed = %.1f
        magic = %s
        skill = %s"""%(self.POWER, self.atk_speed, self.magic,self.skill))

sword=main_sword()

longsword=Long_sword()

shortsword=short_sword()

sword.put()

longsword.put()

shortsword.put()