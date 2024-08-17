import random
# So this is a simple python word game using mostly if, elif and else statement
# It has random functions in it used to guess four numbers between the range of 0 and 1
# I will try to explain some of this code
# This code started from the bottom, became the code i call was from the bottom
# So check the bottom of this code now

def main():
    print( " This is a basic python game")
    print( "it involves basic python functions")
    name = input("What is your name? ")
    begin(name)

def finish(name):
    print("The ultimate stage of this game ")
    print("It will involve a guessing game ")
   
    score = 10 
    while score > 0:
        try:
            number = float(input("input four numbers between 0 and 1: "))
            if number < 0 or number > 1:
                print("Please enter a number between 0 and 1")
                continue
        except ValueError:
            print(" Invalid input, Please ennter a valid number. ")  
            continue
        random_numbers = random.random() in range (4)
        score -= 1 
  
        if random_numbers == number:
                print("correct!!")
                print(score)
                break

        else:
            print("incorrect")   
            print(f" You have {score} chances left")

        
def courage(name):
    print(f"Increase your courage {name}")
    print("Semi-final you can say, that if you get to finish ")
    print("You are confronted with your greatest fear")
    print("you have the chance to either face it or walk away")

    chance = input("will you face it (Y/N )? ").strip().upper()
    if chance == "Y":
        finish(name)
    elif chance == "N":
        print(f"it was nice meeting you, {name}. ")
        exit(0)
    else:
        print(" Invalid choice, please enter Y or N. ")    
        courage(name)


def doorA(name):
    print(f"Welcome to the door of endless of oppurtunities {name} ")
    print(""" You have a choice to live one of these lives
          i. You become richest in the midst of the poor or 
          ii. You become the poorest among the rich 
          """)
    choice = input (" i or ii ").strip().upper()
    if choice == "i":
        print("A typical Nigerian ")
        exit(0)
    else:
        print("great choice, proceed to the next stage. ")
        courage(name)


def doorB(name):
    print("""Welcome the humble one, you will be faced with alot of options so think well and understand the questions before 
        you pick the answers""")    
    print("You have are been faced by this giant robot, you is meant to kill and wipe out humanity")
    print("You have three weapons but you have to choose one ")
    print("Please pick one ")
    print("A a cyborg hand that have 2 funtions: blast out endless amount of fire and make you invisible")
    print( " B a gun to shoot yourself and died immediately leaving the world and not been the hero of the GREAT EARTH")
    print(" C a cup of water, i dont think an explanation for this .........")
    weapon = input( "pick a weapon A, B or C").strip().upper()
    if weapon in ( "A", "B", "C"):
        if weapon == "A":
            print("You blast the human terminator with a large fireball and run aroung the room till you face the next door")
            print("atleast you still have hope even though the robot is not died")
            courage()
        elif weapon == "B":
            print(" Nothing to do here, you are died so bye bye ")  
            exit(0)    
        elif weapon == "C":
            print(" You pour a glass of water on the robot, and it malfunctions ")
            print("well you won, you began the hero of the world")
            print("final stage of the game")
            finish(name)
        else:
            print(" Invalid choice. Please enter A B or C. ")
            doorB(name)

def begin(name):  
    print(" Two doors are before you, one seems to have a golden handle and the other with a silver handle. ")
    print(" You have to choose a door which will determine your destiny in this areana of WAR")
    doors = input ("DOOR A == Golden handle, DOOR B == Sliver handle ").strip().upper()
    if doors == "DOOR A":
        print("You have choosen your destiny")
        doorA(name)
    elif doors == "DOOR B":
        print(" Your destiny lies ahead of you ENTER")
        doorB(name)    
    else:
        print(" Invalid choice. Please enter DOOR A or DOOR B. ")
        choice = input(" Do you wnat to quit now ( YES/ NO)? ").strip().upper()
        if choice == "YES":
            print("Nice choice mate, ending the game. ")
            exit(0)
        elif choice ==  "NO":
            begin(name)
        else:
            print("Invalid input choice. Please enter YES or NO. ")
            begin(name) 
  
if __name__ == "__main__":
    main()      




