import csv
import shelve 
from catalog_class import Catalog

# I am putting all of the CSV data into this stack
stack= []


with open('NYC_OpenData_Catalog.csv', 'rb') as file:   #Opens said cvs file
    reader = csv.reader(file)                          #Saves File to variable reader
    for row in reader:
        stack.append(row)                              #Each stack index contains a complete CSV row
        
        """
        index: name
        
        2 : name
        4 : description
        6 : category
        7 : keywords
        26: creation date
        27: last update
        """
   
for x in range(1,len(stack)): #Creates the Catalog class objects
    
    stack[x][2] = Catalog(stack[x][2], stack[x][4], stack[x][6], stack[x][7], stack[x][26], stack[x][27])

#print "\n" ,stack[1][2], "\n", stack[1][2].name

db = shelve.open("catalog-db6") #Creating the database

print db.__class__, "db.__class__"

for x in range(1,len(stack)): #loading the database
    
    print "name:", stack[x][2].name, "\n"
    print "class:", stack[x][2]
    db[stack[x][2].name] = stack[x][2]
    
db.close()
    

    
