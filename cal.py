class Calculator:
    def get_number(self, prompt):
        return float(input(prompt))
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
     if b!=0:
         return a/b
     else:
         return"Error, division doesn't allow zero"
    def percent(self,a,b):
        if b!=0:
            return(a/b)*100
        else:
            return"Error"

    def start(self):
     print("Mini calculator")
     print("1.ADDITION")
     print("2.SUBTRACTION")
     print("3.MULTIPLICATION")
     print("4.DIVISION")
     print("5.PERCENTAGE")
     print("6.EXIT")




     while True:
         try:
             choice=int(input("Enter the choice from above.....:"))
             if choice ==6:
                print("Thankyou.. Exiting the calculator..Good bye")
                break

             if choice in [1, 2, 3, 4,5]:
                A = self.get_number("Enter the number..: ")
                B = self.get_number("Enter the number..: ")

                if choice==  1:
                    print(f"Result:{self.add(A, B)}")
                elif choice== 2:
                    print(f"Result:{self.sub(A, B)}")
                elif choice== 3:
                   print(f"Result:{self.mul(A, B)}")
                elif choice== 4:
                    print(f"Result:{self.div(A, B)}")
                elif choice==5:
                    print(f"Result:{self.percent(A, B):.2f}%")
             else:
                    print("Invalid choice")

         except ValueError:
            print("Invalid error... please enter numbers only")

if __name__=="__main__":
 cal=Calculator()
 cal.start()



