# Binary Tree traversal software
#
#Author: Nathaniel Pankhurst
#Date: 04/03/2016

import threading

def getUserChoice():
    inputValid = False
    while not inputValid:
        userChoice = input("Please choose from one of the options Below: \n     1: Build Org Chart \n     2: Find path of management between 2 employees \nuserChoice: ")
        if(userChoice == "1") or (userChoice == "2"):
            inputValid = True
        else:
            inputValid = False
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            input("")
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
                input("")
                numberValid = False
        while not nameValid:
            employeeName = input("What is the name of employee " + str(repetitionCount) + "?: ")
            if not (employeeName == ""):
                nameValid = True
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                input("")
                nameValid = False
        while not managerValid:
            try:
                employeeManager = input("What is the employee number of employee " + str(repetitionCount) + "'s manager? (enter 0 if employee has no manager): ")
                int(employeeManager)
                managerValid = True
            except ValueError:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: user input invalid, please try again.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                input("")
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
            input("")
    return repeat

def getName(nameType):
    nameValid = False
    while not nameValid:, tree
        name = input("Input the name for the person at the " + nameType + " of the chain: ")
        for i in len(tree):
            if name == tree[i][2]:
                print(name)
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: This name isn't present in the Organisational chart, please enter another name.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                input("")
    return name

def traverseTree():
    tree = [(1, "Mr Big", 0), (2, "Alan Amis", 1), (3, "Bob Bridger", 1), (6, "Charlie Chubb", 2), (12, "Dave Dell", 3), (15, "Ernie East", 3), (16, "Fred Fish", 6), (17, "George Green", 6)]
    fromStartQueue = []
    fromEndStack = []
    name1 = getName("Start")
    name2 = getName("End")
    

def findManagers(searchName):    
    for i in len(tree):
        print(i)
        i = i + 1


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
            else:
                print("You broke something...")
            endMain = True
                    
#main()
