# Activity 1: Computational Thinking Exercise - Smart Vending Machine

Group Members:
- Angela Martinez
- Zakiyyah Munnilakath
- Aurasia Olaso

Section: 9-Arayat



## Main Problem
Making a vending machine that works properly without breaking down. It needs to let people choose snacks, take money, drop the item, and give back change.


 # Part 1: Decomposing the Problem
 Place here



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
