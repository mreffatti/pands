def displaymenu():
    print("What  would you like to do? ")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) quit")
    choice = input("Type your Letter (a/v/q): ").strip()

    return choice

def doAdd():
     print("in adding")

def doView():
    print("in viewing")

#main program
choice = displaymenu()
while(choice != 'q'):
 # we could do this with lamda functions
 # I am keeping this basic for the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
        
    choice=displaymenu() 
