import sys
from call_database import call_db
from search_functions2 import search_selector
from print_to_screen import print_display


def opening():
    
    """
    Introduces the program and gives the option of runnung the program
    or exiting out of the program.
    """
    
    opening = """\n\nThis is a program created by Marcus Willock with the purpose of searching 
the NYC OpenData catalog CSV file, which is, in essence, a catalog of all 
the different data sets that NYC OpenData has.
                 
        To proceed to the search options, enter run.
                 
        To exit the program, enter exit.
              """
              
    print opening
    
    #calls the function that collects the answer
    opening_answer()
    
    
def opening_answer():
    
    """
    Takes in the answer to the question asked during the opening function
    """
    
    user = raw_input("\n\nEnter your answer here:  ")
    
    if user.lower() == "run":
        
        #Run search options
        db_items = call_db()
        results = search_selector(db_items)
        print_display(results)
        #print "run works"
        
    elif user.lower() == "exit":
        
        #Exit the program
        sys.exit()
        print "exit works"
    
    else:
        
        #safety protocal
        print "We do not recogize that answer. Try again."
        
        opening_answer()
        
    
    


def main():
    
    """
    The main function will control the flow of the entire program.
    """
    while "infinite" == "infinite": #an infinite loop to keep the program running
        
        opening()
    
main()
    
    
    
    
    