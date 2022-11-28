x = 10
y = 2
#----------------------------------------
# Normales if 
if x > y:
    print("x ist größer als y")
#-----------------------------------------
# if not
if not y > x:
    print("y ist nicht größer als x")
#-----------------------------------------
# if else
if y > x:
    pass # nichts tun
else:
    print("alles andere nur nicht das y nicht größer x ist")
#-----------------------------------------
# elif
if x < y:
    pass
elif x>y:
    print("x ist zwar nicht kleiner y aber es ist größer")
#------------------------------------------