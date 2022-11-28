import random # komplette random libery importiren
from time import sleep # einbinden einer einzelnen funktion oder bestimmteb funktionen


while True:
    
    x = random.randrange(1,1000,1) # da komplett importiert muss random. da stehen
    # Zufalszahl start = 1 max = 1000 step = 1
    print(x)
    sleep(1) # kann ohne time. genutzt werden da oben so eingebunden 