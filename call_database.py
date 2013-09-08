import shelve

def call_db():
    """
    Calls the database and puts the DB items in a stack
    """
    
    catalog_list = []
    
    db = shelve.open("catalog-db1")
    
    for key in db:
        
        catalog_list.append(db[key])
    
    #print "call_db works!"    
    return catalog_list
