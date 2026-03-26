
#Grade management system

class Student():
    
    def __init__(self):
        self.__grade = 0
        self.__name = ""
    
    def askName(self):
        while True:
            name = input("Enter the Name: ")
            if name.isalpha():
                self.__name = name
                break
            else:
                print("invalid input!")
            
    
    
    def askGrade(self):
        while True:
            grade = input("Enter the Grade: ")
            if grade.isdigit():
                grade = int(grade)
                
                if int(grade) >= 0 and int(grade) <= 100:
                    self.__grade = grade
                    break
                else:
                    print("Invaled Input")
            else:
                print("invalid input!")

    
    
    def updateGrade(self):
        while True:
            newgrade = input("Enter Grade to update it: ")
            
            if newgrade.is_integer():
                newgrade = int(newgrade)
                
                if newgrade >= 0 and newgrade <= 100:
                    self.__grade = newgrade()
                    
                else:
                    print("Invaled Input")
            else:
                print("Invalid Input")
        
    def showINfo(self):
        print(f"NAME: {self.__name} \nGRADE: {self.__grade}")
        


Student_list = []

def Display_Students_info(std_info):
    print("\n"*2)
    
    for std in std_info:
        print("="*15)
        std.showINfo()
    
    print("\n"*2)

def Create_Student():
    std = Student()

    std.askName()
    std.askGrade()
    Student_list.append(std)
   
    
while True: 
    print("[1] Create Student \n[2] Show Student list \n[3] exit")
    menu = input("enter 1-4: ")
    match menu:
        case "1":
            Create_Student()
        case "2":
            Display_Students_info(Student_list)
        case "3":
            break
        case _:
            print("Invaled Input")
        
    