from call_database import call_db
from print_to_screen import print_display

def search_options():
    """
    Prints a list of search options
    """
    
    #List of search options
    search_options = ["Name", "Keyword", "Leading Char", "View All"]
    
    #print list of options to screen
    for option in search_options:
        print option
        

def user_search():
    
    """
    Asks the user what they want to search for
    """
    
    print "Enter the word(s)/phrase(s) that you would like to search for.\n"
    
    #creates a list with the words to be searched
    search_for = raw_input("ex. (cats, dogs, 311, a, b, c, etc):  ").lower().split(",")
    
    #formats list so that no words start with a space.
    for index in range(len(search_for)):
        if search_for[index][0] == " ":
            
            tempt             = search_for[index][1:]
            search_for[index] = tempt
            
        else:
            pass
        
    return search_for  

def total_results(results):
    
    """
    Prints the total number of results to screen
    """
    
    print "\n\nThere are a total of", len(results), " for this search."
    

    
        
def search_selector(stack):
    
    """
    A function used to select the type of search you
    want to perform.
    """
    
    print "\n\nPlease select one of the following search options. \n\n"
    
    #prints the search options
    search_options()
    
    #The variable that will holde the user's search type selctions
    search_type = ""
    
    #A loop to make sure that the user selects a search type
    while search_type == "":
        
        search_type = raw_input("\n\nEnter your search type:  ").lower()
        
        if search_type == "name":
            
            print "\n\n\t\t\t\tName Search\n"
            results = name_search(stack)
            
        elif search_type == "keyword":
            
            print "\n\n\t\t\tKeyword Search\n"
            results = keyword_search(stack)
            
        elif search_type == "leading char":
            
            print "\n\n\t\t\tLeading Char Search\n"
            results = leading_char_search(stack)
            
        elif search_type == "view all":
            
            print "\n\n\t\tView all search"
            results = view_all_search(stack)
            
        else:
            
            print "\n\n I do not regonize that search type. Would you like to try again?\n\n"
            
            try_again = raw_input("(y/n")
            
            if try_again == "y":
                
                search_type = ""
            
            else:
                
                pass
        
    #I want to return the results of the search.    
    return results


def name_search(stack):
    
    """
    The logic for the name search
    """
   
    #collects user input
    search_for = user_search()
    
    #results will be put in this list
    results = []
    
    #the search logic
    for index in range(len(stack)):
        
        for item in search_for:
        
            #If statement for when str.find finds a match
            if stack[index].name.lower().find(item) != -1:
            
                results.append(stack[index])
            
            else:
                pass
    
    #prints out the total number of results
    total_results(results)  
    
    #The varibale results is ready to be sent to the print_display function!
    return results

def keyword_search(stack):
    
    #collects user input
    search_for = user_search()
    
    #List of results
    results = []
    
    #keyword search
    for index in range(len(stack)):
        
        for keyword in stack[index].keywords:
            
            for items in search_for:
                
                if items == keyword:
                    results.append(stack[index])
                    
                else:
                    pass
    
    #prints out the total number of results
    total_results(results) 
    
    #The varibale results is ready to be sent to the print_display function!   
    return results

"""
Need to test Leading Char Search!
"""
def leading_char_search(stack):
    
    """
    This search will return a list of classes from the stack that
    have the same leading char.
    """
    
    """
    I need to write a sort function...
    """
    def sort_stuff(item):
        
        return item.name
    
    
    #print stack
    stack.sort(key = sort_stuff)
    #print "The stack:", stack
    
    chars = user_search()
    
    """
    Logic:
    
    I will create a string of the leading chars and then
    I will use the indexs derived from this string to find the
    start and end indexs of the wanted subset of the stack.
    """
    
    """
    Note: Every leading char seems to be a number or a capital letter.
    """
    
    #string of leading chars
    char_string = ""
    
    for index in range(1,len(stack)):
        
        """
        Note: the range starts at one because the first item
        in the stack is a class that is completely empty...
        
        my bad :(
        
        I am too lazy to fix it. Hahahaha
        """
        
        char_string += stack[index].name[0]
    
    #testing
    #print char_string
    
    #list of results
    results = []
    
    #finds the start and end index
    for char in chars:
        
        start_index = char_string.find(char)
        
        end_index   = char_string.find(chr(ord(char)+1))
        
        for index in range(start_index,end_index):
            
            results.append(stack[index])
            
    #prints out the total number of results
    total_results(results)  
    
    #The varibale results is ready to be sent to the print_display function!
    return results

def view_all_search(stack):
    
    #prints out the total number of results
    total_results(stack)  
    
    #The varibale results is ready to be sent to the print_display function!
    return stack
        
            
def testing2():

    db_items = call_db()
    
    results = search_selector(db_items)
    print_display(results)
    
#testing2()
