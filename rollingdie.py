import random


command = "y"

while command == "y":

    print ("Number on the dice is:")
    no=(random.randint(1,6))

    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if no == 2:
        print("[-----]")
        print("[0    ]")
        print("[    0]")
        print("[-----]")

    if no == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")

    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")

    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")  

    if no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")          

    print("if you are interested to Roll the dice again press 'y' ")
    print("if you are not interested to Roll the dice again press 'n' ")
    command = input("Are you interested to Roll the dice again?")
    

else:
    command="n"
    exit()    