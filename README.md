# Organisational-Hierarchy-Chart-traversal-program

Organisational hierarchy chart traversal program used to find the shortest path of communication between employees
in a company that has very strict rules about only passing information up and down the chain of command.


## How To Use.
### Upon booting program
Upon booting of the program, the user is displayed three options:
  <br />  * 1: Build Org Chart.
  <br />  * 2: Find shortest path through chain of management between two employees.
  <br />  * Q: Quit the Program. 
The program prompts the user to enter an option, and then from this option redirects the user accordingly.
#### More on the options:
Option | What it does
-------|-------------
Build Org Chart | When the program starts the tree is defined as an empty list, this means before anything else can happen the user is going to need to define the tree for the first time, to know how to do this read the "Build Org Chart" section.
Find Shortest Path | When the program starts for the first time, you will be unable to select option 2. This is because the organisational chart has not yet been defined, run option 1 to build the chart before running this command. To know how to find the shortest path read the "Find shortest path" section.
Quit | Exits the program

### Build Org Chart
Upon selecting option 1, the getTree() function is called, this results in the program asking for the information on the employees in the tree.<br /> 
The screen prompts are pretty straight-forward, so follow the prompts and enter the employees in any order, entering yes when prompted to state whether or not you have any more employees to add. Just make sure that the manager id that you input does correlate to a real employee id, as there is no validation preventing this from going through.<br /><br />
When you've completed entering your employee information don't forget to enter no when the prompt asking you if you have any more employees to add appears on the screen.

### Find Shortest Path
Upon selecting option 2 (if the org chart has already been built), the traverseTree() function is called, this results in the program asking for the names of the two employees the user wants to find the shortest path of commnication between. Upon the appearance of this prompt enter the two names one at a time and simply press enter. Though make sure you are spelling the names correctly, as if you don't the program will not find the employee.<br />
After entering both employee names correctly, if a path of communication is found, the program will display it in the shell.

## Known Bugs
The following bugs in the program are known:
Known Bug | Function found in|Why has it happened
----------|------------------|-------------------
program accepts non-existent manager ids | getTree() | This has occurred as since the user must be able to input the employees in any order, the code can't impliment a validation check that ensures the manager already exists in the list before you can reference it. 

