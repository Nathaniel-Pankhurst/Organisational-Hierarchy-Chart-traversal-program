# Binary Tree traversal software
#
#Author: Nathaniel Pankhurst
#Date started: 04/03/2016
#Date finished: 05/03/2016

def getUserChoice(tree):
# Function called in the main() function to give user the range of choices, pull the user's choice as an input,
# then validate that choice.
    inputValid = False
    while not inputValid:
        userChoice = input("Please choose from one of the options Below: \n     1: Build Org Chart \n     2: Find shortest path through chain of management between 2 employees \n     3: Print Org Tree \n     Q: Quit the Program \nuserChoice: ")
        userChoice = userChoice.lower()
        if(userChoice == "1") or ((userChoice == "2") and not (tree == [])) or (userChoice == "3")or (userChoice == "q"):
            inputValid = True
        else:
            inputValid = False
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            input("*Press Enter to continue*")
    return userChoice

def getTree(tree):
# Function called as the first option from the main() function used to take user inputs and then build these inputs into a list
# of tuples that represents the organisational hierarchy chart
# All inputs in this function have been validated to make sure that they fit into their respective intended type,
# and in the case of employee number to ensure that no employee number is repeated.
    treeFinished = False
    repetitionCount = 1
    ceoPresent = False
    while not treeFinished:
        numberValid = False
        nameValid = False
        managerValid = False
        checkPresent = False
        
        while not numberValid:
             try:
                employeeNumber = int(input("What is the employee number for employee " + str(repetitionCount)+ "?: "))
                if employeeNumber >= 1:
                    if repetitionCount > 1:
                        for j in range(repetitionCount - 1):
                            if employeeNumber == tree[j][0]:
                                checkPresent = True
                    if not checkPresent:
                        numberValid = True
                    else:
                        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: There is already an employee with that number, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                else:
                    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: Please enter a value greater than 0 for the employee number.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    input("*Press Enter to continue")
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
                employeeManager = int(input("What is the employee number of employee " + str(repetitionCount) + "'s manager? (enter 0 if employee has no manager): "))
                if employeeManager >= 0 and not ceoPresent:     
                    managerValid = True
                    ceoPresent = True
                elif employeeManager >= 1:
                    managerValid = True
                else:
                    errorOut = "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: Please enter a value greater than "
                    if not ceoPresent:
                        errorOut = errorOut + "or equal to "
                    errorOut = errorOut + "0 for the employee's manager number.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" 
                    print(errorOut)
                    input("*Press Enter to continue")
            except ValueError:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                input("*Press Enter to continue*")
                managerValid = False
                
        tree.append((employeeNumber, employeeName, employeeManager))
        treeFinished = checkFinished()
        repetitionCount = repetitionCount + 1
    print(tree)


def checkFinished():
# Function implemented by getTree() that checks whether or not the user has finished entering in the values for the tree,
# and then returns a boolean value stating the result.
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

def traverseTree(tree):
# Function called by main() for the purpose of finding, and building the shortest path of communication between two employees.
# For this to occur traverseTree pulls the employeeId's of the user's chosen employees through use of getEmployeeId(),
# passes those into getEmployeeChainOfCommand() to find the chains of command for both employee,
# and then finally prints out to the user the shortest path between the two employees that was found by
# passing in both chains of command into findShortestPath()

    senderCoC = [""]
    recipientCoC = [""]
    sender = getEmployeeId("Start", tree)
    recipient = getEmployeeId("End", tree)
    senderCoC = getEmployeeChainOfCommand(sender, tree)
    recipientCoC = getEmployeeChainOfCommand(recipient, tree)
    shortestPath = findShortestPath(senderCoC, recipientCoC)
    print("\nThe shortest chain of communication between the two employees is: " + shortestPath + "\n")
    input("*Press Enter to continue*")

def getEmployeeId(nameType, tree):
# Function used by traverseTree() to find the employee number of an employee in the org chart
# who has a name that is obtained through user input.
# Validation in place to check that the inputted name is present in the Org Chart.

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
                    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: This name isn't present in the Organisational chart, please enter another name.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    input("*Press Enter to continue*")
    return employeeId

    
def getEmployeeChainOfCommand(employeeId, tree):
# Function used by traverseTree() to find the chain of command for a given employee.
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
# Function used by traverseTree() that compares two different chains of command to find the shortest route of communication
# between two employees, returning this route as a string.
    shortestPath = ""
    intersectionFound = False
    for i in range(len(senderCoC)):
        if not intersectionFound:
            if not (i == 0):
                shortestPath = shortestPath + " -> "
            shortestPath = shortestPath + senderCoC[i]
        for j in range(len(recipientCoC)):
            if senderCoC[i] == recipientCoC[j]:
                if not intersectionFound:
                    intersectionFound = True
                    backStep = j - 1
                    while not backStep == -1:
                        shortestPath = shortestPath + " <- " + recipientCoC[backStep]
                        backStep = backStep - 1
    return shortestPath
                
            
def main():
# This is the main function, upon calling the program this calls the functions used to determine the user's choice of action
# then routes the user to the functins needed to complete the intended task.
        print("---------------------------------")
        print("------------BARCharts------------")
        print("---------------------------------")
        endMain = False
        tree = []
        while not endMain:
            userChoice = getUserChoice(tree)
            print("\n\n")
            if (userChoice == "1"):
                tree = []
                getTree(tree)
            elif (userChoice == "2"):
                traverseTree(tree)
            elif (userChoice == "3"):
                print(tree)
            elif (userChoice == "q"):
                endMain = True
            else:
                print("You broke something...")
                    
main()
quit()

