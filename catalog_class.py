#Let's make a class

class Catalog:
    
    """
    This class is going to be used to catalog the NYC Open Data catalog CSV file.
    """
    
    def __init__(self, name = "none", description = "none", category = "none", keywords = "none", creation_date = "none", last_update = "none"):
        
        #Formating the items that way I want
        
        self.name          = name.split("(")[0]
        self.description   = description
        self.category      = category
        self.keywords      = keywords.split(",")
        self.creation_date = creation_date[0:-5]
        self.last_update   = last_update[0:-5]
        
    def __str__(self):
        return "\nname: %s\ndescription: %s\ncategory: %s\nkeywords: %s\ncreation date: %s\nlast update: %s\n]" %(self.name, self.description, self.category, self.keywords, self.creation_date, self.last_update)

    def __repr__(self):
        
        return self.__str__()