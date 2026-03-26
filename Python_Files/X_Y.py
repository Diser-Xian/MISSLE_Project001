import time

#THIS GRAPH THE X AND Y ENTERCEPT BUT EXCLUDING THE Z AXIS


print("="*30)
print("WELCOME TO THE X AND Y GRAPHICIZER")
print("="*30)

#variable
CharL = "#"
start = True

while start:
    print("="*30)
    x = input("Enter the Point [X]: ")
    print("="*30)
    y = input("Enter the Point [Y]: ")
    print("="*30)
    
    
    if x.isalpha() and y.isalpha():
        print("INVALED INPUT")
    else:
        print(f"X: {x}")
        for X in range(int(x)-1):
            if X == 0:
                print("@")
            print(CharL)
            time.sleep(0.4)
            
        
        for Y in range(int(y)):
             print(CharL, end=" ", flush=True)
             if Y == int(y) - 1:
                print("@")
             time.sleep(0.4)
            
        print(f"Y: {y}")
    print("\n")
      
    print("="*30)
    print("<SUCCESSFULLY GRAPHICIZE>")
    print("="*30)
    
    again = input("0 > [EXIT], 1 > [AGAIN]:")
    if again == 1:
        continue
    else:
        break