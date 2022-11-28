class User:
    def __init__(self, name,alter, email): # inizialisiren in anderen sprachen constructor
        
        self.name = name # klassen variablen müssen immer mit self. bezeichnet werden
        self.alter = alter
        self.email = email
        
    def get_data(self):
        return {"Name": self.name, "Alter" : self.alter, "Email" : self.email}
    
user_daten = User("John", 19, "john_213@mail.com") # ininzialisirung und anlegen
# des objekts user_daten aus der Klasse User
print(user_daten.get_data) # ruft methode auf und printet den return