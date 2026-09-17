#Lauren Bowman
#CTC389
#Lab 8-Music Career Choices
#Create an interactive story using 5 different decisions. Each decision must have 3 decisions to choose from. Make sure the user can play the game as long as they choose "yes" at the end or they die.

def door1():
    print("Door 1: Private Piano Teacher")
    print ("You are teaching a student, but notice the piano bench is wobbly. What do you do next?")
    print ("1. Fix the bench before playing with a wrench.")
    print ("2. Swap out the bench for a chair.")
    print ("3. Ignore that the bench is broken, hop on the bench and play violently.")
   
    choice = input ("Choose 1,2, or 3: ")
    if choice == "1":
        print("You fix the bench and have a great lesson!")
    elif choice == "2":
        print ("The student learns discipline and becomes a great pianist. The parents help you by donating a new piano bench to you a week later.")
    elif choice == "3":
        print("The bench breaks, you fall, hit the back of your head on your floor and die.")
    else:
        print("Invalid choice. You wasted time and the lesson ended.")

def door2():
    print("Door 2: Street performer")
    print(" You are playing at 3rd Street Promenade when a rival musician tries to take your spot. What do you do next?")
    print ("1. Perform a duet together.")
    print ("2. Play louder to drown them out and attract more of a crowd.")
    print ("3. Physically attack the rival.")
   
    choice = input ("Choose 1, 2, or 3:")
    if choice == "1":
        print ("The crowd loves it! You both make a lot of money and become friends.")
    elif choice == "2":
        print ("You win the crowd over with your amazing skills.")
    elif choice == "3": 
        print ("The rival pulls out a knife and you die after being attacked.")
    else:
        print("Invalid choice. The rival steals your spot.")

def door3():
    print("Door 3: Music Producer" )
    print (" Your high-teach studio console sparks during a big recording session. What do you do next?")
    print ("1. Call an electrician to fix it.")
    print ("2. Grab the live wires with bare hands.")
    print ("3. Switch to working on your laptop.")
   
    choice = input("Choose 1,2, or 3: ")
    if choice == "1":
        print ("The console gets fixed safely and you finish the album.")
    elif choice == "2":
        print ("You get electrocuted by high voltage and die.")
    elif choice == "3":
        print ("You finish the song on your computer thanks to your knowledge of music tech and production software and win a Grammy!")
    else: 
        print ("Invalid choice. You lose the project file.")

def door4():
    print("Door 4: High School Band Director")
    print("Right before a big championship, the band is out of tune. What do you do next?")
    print ("1. Tune every instrument carefully.")
    print ("2. Give an inspiring pep talk.")
    print ("3. Scold the band for being irresponsible.")

    choice = input("Choose 1, 2, or 3:")
    if choice == "1":
        print("The band plays perfectly and wins 1st place because you took the time to tune them!")
    elif choice == "2":
        print("The pep talk motivates them to play their best, but they didn't win the competiion.")
    elif choice == "3":
        print("The stress kills you and you have a heart attack on the football field right after they play.")
    else:
        print("Invalid choice. The band misses their turn.")

def door5():
    print(" Door 5: Touring Musician" )
    print("You are on stage at a huge rock concert with pyrotechnics going off. What do you do next?")
    print("1. Stay in your area onstage and play your solo.")
    print("2. Jump directly into the live flame cannons.")
    print("3. Jump off the stage into the crowd.")

    choice = input("Choose 1,2, or 3: ")
    if choice == "1":
        print("Your solo goes viral and you become famous!")
    elif choice == "2":
        print ("You cath on fire and die instantly.")
    elif choice == "3":
        print ("The crowd catches you and carries you around then back onto the stage!")
    else:
        print ("Invalid choice. You miss your tuen to play your solo.")

def game():
    playing = True
    while playing:
        print("-----------------------------------------------------")
        print(" Welcome the game of Music Careers! Choose wisely!")
        print("-----------------------------------------------------")
        print("1. Private Piano Teacher")
        print("2. Street Performer")
        print("3. Music Producer")
        print("4. High School Band Director")
        print("5. Touring Musician")

        door = input("Hello! Pick a door (#1-5): ")

        if door == "1":
            door1()
        elif door == "2":
            door2()
        elif door == "3":
            door3()
        elif door == "4":
            door4()
        elif door == "5":
            door5()
        else:
            print("Door choice invalid.")
        
        playagain = input("Do you want to play again? (yes or no)?" )
        if playagain == "no":
            playing = False
            print("Thank you for playing, this is the end of the game!")
            print("=====================================================")


game()
