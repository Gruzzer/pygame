class Calculator:
    def __init__(self):
        self.count =0
    def add(self, num1,num2):
        result=num1+num2
        print(("\n%d + %d = %d") % (num1, num2,result))
    def sub(self, num1, num2):
        result = num1 - num2
        print(("\n%d - %d = %d") % (num1, num2, result))

    def mul(self, num1, num2):
        result = num1 * num2
        print(("\n%d * %d = %d") % (num1, num2, result))

    def div(self, num1, num2):
        result = num1 / num2
        print(("\n%d / %d = %d") % (num1, num2, result))

    def menu(self):
        print("\n계산기")
        while self.count < 1:
            print('''
1. +
2. -
3. *
4. /
5.종료''')
            num = int(input("\n"))

            if num == 1:
                num1 = int(input("첫번째 수 입력 : "))
                num2 = int(input("두번째 수 입력 : "))
                self.add(num1,num2)
            elif num == 2:
                num1 = int(input("첫번째 수 입력 : "))
                num2 = int(input("두번째 수 입력 : "))
                self.sub(num1, num2)
            elif num == 3:
                num1 = int(input("첫번째 수 입력 : "))
                num2 = int(input("두번째 수 입력 : "))
                self.mul(num1, num2)
            elif num == 4:
                num1 = int(input("첫번째 수 입력 : "))
                num2 = int(input("두번째 수 입력 : "))
                self.div(num1, num2)
            elif num == 5:
                self.count = 1
            else:
                print("error!!")

cal=Calculator()
cal.menu()