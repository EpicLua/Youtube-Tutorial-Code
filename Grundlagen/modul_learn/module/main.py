# Modul einbinden 
import modul # from modul import say | geht auch aufrufen dann nur mit say
#---------------
# externes modul
import modul_ex.modul_2
# durch __init__.py möglich




modul.say("Hallo") # aufruf der funktion aus modul 
modul_ex.modul_2.say_name("john") # aufruf aus externem modul 