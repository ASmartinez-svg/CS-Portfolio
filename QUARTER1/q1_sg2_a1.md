# Activity 1: Computational Thinking Exercise - Smart Vending Machine

Group Members:
- Angela Martinez
- Zakiyyah Muneer Munnilakath
- Aurasia Olaso

Section: 9-Arayat



## Main Problem
Making a vending machine that works properly without breaking down. It needs to let people choose snacks, take money, drop the item, and give back change.

## Sub-Problems:
1. Students choosing the right snack
2. Checking if the snack is available
3. Checking the amount of change given by the machine
4. Machine being able to handle multiple students using it in succession

 # Part 1: Decomposing the Problem
 Sub-Problem 1: Students choosing the right snack
CT Skill: Algorithm design
Solution: The machine should show the items and their prices. Then the buyer would pick the item they want

Sub-Problem 2: Checking if the snack is available
CT Skill: Pattern Recognition
Solution: The machine checks if the chosen snack is available. If it is available, it tells the buyer to pick the snack they want.

Sub-Problem 3: Checking the amount of change given by the machine
CT Skill: Algorithmic design
Solution: create a system which calculates the amount of change that should be given to a person then gives the correct change to the student


Sub-Problem 4: Machine being able to handle multiple students using it in succession
CT Skill: Algorithmic design
Solution: create a system which allows the machine to reset after each purchase so it can serve multiple students one after another




 # Part 2: Algorithmic Solution


Selected part: Payment and selection process

### Pseudocode

START
    
    Show all snacks and prices
    Ask buyer to press item code

    IF item is empty THEN
        Show "Out of stock"
        Go back to START
    ENDIF

    Get item price
    Show price to buyer
    
    total_paid = 0
    
    WHILE total_paid < price DO
        Show remaining price
        Ask for money
        
        IF buyer presses cancel THEN
            Return all money
            Show "Cancelled"
            Go back to START
        ENDIF
        
        total_paid = total_paid + inserted_money
    ENDWHILE

    Drop snack
    
    IF total_paid > price THEN
        change = total_paid - price
        Give change
    ENDIF

    Show "Thank you"
END

