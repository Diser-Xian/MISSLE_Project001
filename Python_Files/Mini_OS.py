from datetime import datetime
import os


class neazeOS():
    
    def __init__(self):
        self.__name = ""
        self._PassWord__ = ""
        self._LogIn__ = False
    
    
    def createuser(self):
        while True:
            user_input = input("Enter Username: ").split()
            if len(user_input) > 1:
                print("Username Should not contain space")
            else:
                self.__name = user_input[0]
                break
        while True:
            passwd = input("Enter your password: ").split()
            if len(passwd) > 1:
                print("Password Should not contain space!")
            else:
                psswd = passwd[0]
                if len(psswd) <= 8:
                    print("Password Should be more than 8 character!")
                else:
                    self._PassWord__ = psswd
                    self._LogIn__ = True
                    break
            
    
    def Show_user_info(self):
        if self._LogIn__ == False:
            print("Please Login First!")
            self.createuser()
        else:
            print(f"User: '{self.__name}' \nPassword: '{self._PassWord__}'")
    
        
    def  time(self):
        time = datetime.now()
        cur_time = time.strftime("%H:%M:%S")
        print(f"Currrent Time: {cur_time}", flush=True)
        
    def clear(self):
        os.system("cls")
    
    def Help(self):
        print("tabang >> Shows Available Command")
        print("erase >> clear the terminal")
        print("oras >> shows the current Time")
        print("add_me >> Create user")
        print("\n")
        
    def start(self):
        print("neazeOS\n")
        print("Type tabang to see Commands\n\n")
        while True:
            
            input_ = input("~# ")
            
            match input_:
                case "tabang":
                    self.Help()
                case "erase":
                    self.clear()
                case "oras":
                    self.time()
                case "add_me":
                    self.createuser()
                case "open_me":
                    self.Show_user_info()
                    
                    
                case "_":
                    print("Invalid Command!")
            
            

minios = neazeOS()
minios.start()
            