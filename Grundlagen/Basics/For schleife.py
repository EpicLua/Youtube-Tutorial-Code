#-----------------------------------------------
# Normale for schleife range gibt die Zahlen von 0 bis 9 aus 
for x in range(10):
    print(x)
#-----------------------------------------------
# gibt die zahlen 0,2,4,6,8 aus
for x in range(0, 10, 2):
    print(x)
#-----------------------------------------------
# Gibt die einzelnen Buchstaben aus s aus 
s = "Hallo"
for x in s:
    print(x)
#-----------------------------------------------
# gibt 0 bis 9 aus der liste aus 
l = [0,1,2,3,4,5,6,7,8,9] # liste
for x in l:
    print(x)
#----------------------------------------------
# Gibt erst alle namen aus und dann alter
d = {"Name" : ["lars, john, Marc"], "Alter" : [20, 18, 19]} # Dictunary
for x in d: # schreibt die liste in x 
    for y in x: # liest die values aus x aus  
        print(y)
#----------------------------------------------