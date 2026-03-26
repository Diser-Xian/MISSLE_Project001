import time

#initialize variable
Code = 782495
fuel_level = "Full"
power = 80000
timer = 5

#Header
print("#--------------------------#")
print("#      Missile Launcher    #")
print("#--------------------------#")

#ask for Code
code_input = input("Enter the Launch Code# ")

#Checking Launch Code 
if code_input.isdigit():
    if int(code_input) == Code:
        target = input("Enter the Location of Target: ")
        time.sleep(1)
        #LAUNCHING MISSILE
        print("#--------------------------#")
        print("#   LAUNCHING MISSILE..    #")
        print("#--------------------------#")
        print("Fuel Status: " + fuel_level)
        print("Missile Power: " + str(power))
        #Timer
        for i in range(timer):
            print(timer-i,flush=True)
            time.sleep(0.5)
            
        print(">>>SUCCESSFULLY LAUNCH<<<")
        print("Target location: " + target)

#warning if the code is incorrect
else:
    print(">>>>WARNING CODE INCORRECT<<<<")
    
        

