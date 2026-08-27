#Lauren Bowman
#CTC389
#Lab 6
#Aug 26, 2026


names = ["Lauren","Yukiko","Sasha","Inari","Carl"]
print ("Hello! Here is your class roster:") 
print ("1.", names[0])
print ("2.", names[1])
print ("3.", names[2])
print ("4.", names[3])
print ("5.", names[4])

x = int(input ("Select an option: 1 to add a student , 2 to modify a student name, or 3 to remove a student: "))
if x == 1:
   
    addname = input ("Add student to list: ")
    names.append (addname)
    print ("Here is the new list of students: ")
    print ("1.", names[0])
    print ("2.", names[1])
    print ("3.", names[2])
    print ("4.", names[3])
    print ("5.", names[4])
    print ("6.", names[5])

if x == 2:
    
    print ("1.", names[0])
    print ("2.", names[1])
    print ("3.", names[2])
    print ("4.", names[3])
    print ("5.", names[4])
    
    y = int(input("Which number student's name do you want to modify? "))
    n = input("Enter the student's modified name: ")
    
    names[y - 1] = n

    print ("After list element 1 modfication: ")
    print ("1.", names[0])
    print ("2.", names[1])
    print ("3.", names[2])
    print ("4.", names[3])
    print ("5.", names[4])



if x == 3:
    print ("1.", names [0])
    print ("2.", names [1])
    print ("3.", names [2])
    print ("4.", names [3])
    print ("5.", names [4])
    
    z = int(input("Which number student do you want to remove?"))
    names.pop(z - 1)

    print ("After removing one name:")
    print ("1.", names[0])
    print ("2.", names[1])
    print ("3.", names[2])
    print ("4.", names[3])
    



