import os
from call_database import call_db

def user_input(start_index, end_index, stack):
    
    """
    This function will be called within the viewer functions,
    and it will be used to deal with the user input
    """
    
    #The user variable will be used to save the users response and
    #to control the flow of the following while loop.
    user = "y"
    
    while user == "y":
        
        print "The index set is [%s:%s]\n" %(str(start_index), str(end_index))
        user = raw_input("\nEnter the index of the number of the item that you want to view or push enter to see the next set of items:  ")
        
        try: #checking to see if the user entered an integer
            
            user = int(user)
            
        except:
            
            pass
        
        #The logic for the user entering an int
        if isinstance(user , int) == True:
            
            print "\n", stack[user], "\n"
            
            #Askes the user if they want to restart this loop
            user = raw_input("Do you want to view any other items? (y/n):  ")
            
        else:
            
            pass
    
    #print "user_input works!"
    return user


def stopper_function(stack, count):
    
    """
    Makes sure no more than 20 items are printed to the screen at a time.
    """
    
    if len(stack) <= count + 20:
        
        stopper = len(stack) - 1
        
    else:
        
        stopper = count + 20
        
    return stopper


# I cannot remember what is the propper order for the aruguments with assigned values
# and the arguments without assigned values.
def print_display(stack, count = 0):
    
    """
    This function will print the items of the stack to the screen, and
    the stopper_function will control how many items are printed to 
    screen. 
    """
    
    #The starting index of the print of "stack"
    start_index = count
    
    #Creating a stopper variable (AKA "you have hit the 20 item mark")
    
    stopper = stopper_function(stack, count)
    
    
    #The loop responsible for priting the items to screen    
    while count < len(stack):
        
        print "\nindex:", count
        print "name of Item:", stack[count].name, "\n"
        
        if count == stopper:
            
            response = user_input(start_index, stopper, stack)
            
            #reseting variables
            start_index = count
            stopper = stopper_function(stack, count)
            
            if response == "exit":
                
                sys.exit()
                
            else:
                pass
            
        else:
            pass
        
        count += 1
    
    #print "print_display works!"    
    return "done"


def testing():
    
    db_itmes = call_db()
    
    print_display(db_itmes)
    

#testing()
