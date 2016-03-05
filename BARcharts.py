# Binary Tree traversal software
#
#Author: Nathaniel Pankhurst
#Date: 04/03/2016

#Tree defined  for testing purposes only
tree = [(1, "Mr Big", 0), (2, "Alan Amis", 1), (3, "Bob Bridger", 1), (6, "Charlie Chubb", 2), (12, "Dave Dell", 3), (15, "Ernie East", 3), (16, "Fred Fish", 6), (17, "George Green", 6)]

def getUserChoice():
    inputValid = False
    while not inputValid:
        userChoice = input("Please choose from one of the options Below: \n     1: Build Org Chart \n     2: Find shortest path through chain of management between 2 employees \n     Q: Quit the Program \nuserChoice: ")
        userChoice = userChoice.lower()
        if(userChoice == "1") or (userChoice == "2") or (userChoice == "q"):
            inputValid = True
        else:
            inputValid = False
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            input("*Press Enter to continue*")
    return userChoice

def getTree(tree):
    treeFinished = False
    while not treeFinished:
        numberValid = False
        nameValid = False
        managerValid = False
        repetitionCount = 1
        while not numberValid:
             try: 
                employeeNumber = int(input("What is the employee number for employee " + str(repetitionCount)+ "?: "))
                int(employeeNumber)
                numberValid = True
             except ValueError:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                input("*Press Enter to continue*")
                numberValid = False
        while not nameValid:
            employeeName = input("What is the name of employee " + str(repetitionCount) + "?: ")
            if not (employeeName == ""):
                nameValid = True
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                input("*Press Enter to continue*")
                nameValid = False
        while not managerValid:
            try:
                employeeManager = input("What is the employee number of employee " + str(repetitionCount) + "'s manager? (enter 0 if employee has no manager): ")
                int(employeeManager)
                managerValid = True
            except ValueError:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                input("*Press Enter to continue*")
                managerValid = False
                
        tree.append((employeeNumber, employeeName, employeeManager))
        treeFinished = checkFinished()
        repetitionCount = repetitionCount + 1
    print(tree)


def checkFinished():
    repeat = False
    valid = False
    while not valid:
        getFinished = input("Do you have any more employees to add? (Y/N): ")
        getFinished = getFinished.lower()
        if getFinished == "y" or getFinished == "yes":
            valid = True
            repeat = False
        elif getFinished == "n" or getFinished == "no":
            print("Tree Built")
            valid = True
            repeat = True
        else:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            input("*Press Enter to continue*")
    return repeat

def getEmployeeId(nameType, tree):
    nameValid = False
    nameFound = False
    while not nameValid:
        name = input("Input the name for the person at the " + nameType + " of the chain: ")
        i = 0
        for i in range(len(tree)):
            if name == tree[i][1]:
                nameValid = True
                nameFound = True
                employeeId = tree[i][0]
                print("Employee " + name + " found.")
            elif not nameFound:
                if i == (len(tree) - 1):
                    nameValid = False
                    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: This name isn't present in the Organisational chart, please enter another name.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    input("*Press Enter to continue*")
    return employeeId

def traverseTree():
    senderCoC = [""]
    recipientCoC = [""]
    sender = getEmployeeId("Start", tree)
    recipient = getEmployeeId("End", tree)
    senderCoC = getEmployeeChainOfCommand(sender)
    recipientCoC = getEmployeeChainOfCommand(recipient)
    shortestPath = findShortestPath(senderCoC, recipientCoC)
    print("The shortest chain of communication between the two employees is: " + shortestPath)
    
def getEmployeeChainOfCommand(employeeId):
    chainOfCommand = []
    toBeSearched = employeeId
    listComplete = False
    while not listComplete:
        for i in range(len(tree)):
            if toBeSearched == tree[i][0]:
                chainOfCommand.append(tree[i][1])
                toBeSearched = tree[i][2]
            elif toBeSearched == 0:
                listComplete = True
    return chainOfCommand

def findShortestPath(senderCoC, recipientCoC):
    shortestPath = ""
    intersectionFound = False
    for i in range(len(senderCoC)):

        if not intersectionFound:
            if not (i == 0):
                shortestPath = shortestPath + " -> "
            shortestPath = shortestPath + senderCoC[i]
        for j in range(len(recipientCoC)):
            if senderCoC[i] == recipientCoC[j]:
                intersectionFound = True
                backStep = j - 1
                while not backStep == -1:
                    shortestPath = shortestPath + " <- " + recipientCoC[backStep]
                    backStep = backStep - 1
    return shortestPath
                
            
def main():
#The main function, called upon launch of the program.
        print("---------------------------------")
        print("------------BARCharts------------")
        print("---------------------------------")
        endMain = False
        tree = []
        while not endMain:
            userChoice = getUserChoice()
            if (userChoice == "1"):
                tree = []
                getTree(tree)
            elif (userChoice == "2"):
                traverseTree()
            elif (userChoice == "q"):
                endMain = True
            else:
                print("You broke something...")
                    
main()
quit()

