import random
import time


name = input("Enter your Name: ")
print("="*35)
print(f"Hello {name}!!")
print("I will ask you some random question")
print("and detect it, if its True/False")
print("="*35)
time.sleep(1)


question = [">Do you like One of your clssmate? ",
            ">Do you Cheat During your exam or quize? ",
            ">Do you Have a crush on one of your Teacher or Professor"
]



def Game_process():
    game = True

    while game:
        Question = random.choice(question)
            
        print("ANSWER YES OR NO")
        answer = input(f"{Question}: ")
        time.sleep(1)
        
        
        print("Analyzing brain signals....")
        time.sleep(1)
        print("Detecting heart rate....")
        time.sleep(1)
        print("Scanning facial expression....")
        time.sleep(1)
        print("Finalizing.....")
        time.sleep(1.5)
        
        detection_result = random.choice([">>>TRUE<<<",">>>FALSE<<<"])
        print("="*35)
        print(f"RESULT: {detection_result}")
        print("="*35)
        
        try_again = str(input("Do you want to try again? (Y)(N): ").upper)
        
        if try_again == "Y":
            Game_process()
        elif try_again == "N":
            game = false
        
          
            
        
    
    



Game_process()