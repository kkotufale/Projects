# S10_Logic2_StarterFile.py  <- this is the Starter File for Session 10
# K.Schmitz (c) 2022,2023,2024
#  Starter File for CIS2010 Session 10, Python Logic 2
##################Initialization information, do not modify ################
#
from cis2010utils4 import StartHere, EndHere, strhash
import statistics as stats
#####################################################################################
# Start Workshop
#
# Task 2 
StartHere( "Kike Otufale", "S10w", "Spring 2025")

#
#Task 3 assign and increment
x = 0
y = 0
y = y + 1
y += 1
print( y )
#
#Task 4 strings
cis = '2010'
cisL = len(cis)
# hash function
cisH = strhash(cis)
#
#Task 5 Lists
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
print( days[0] )
print( days[1] )
daysL = len(days)
print('length of list is ', daysL )

hd = 'Humpday this week is '
hd += days[3]
hdL = len(hd)
hdH = strhash(hd)
print( hd, 'count=', hdL, 'hash=', hdH )
#
#Task 6 math formulas
ft = 6
inches = ft * 12
cm = inches * 2.54
m1 = cm / 100
m2 = (inches * 2.54) / 100
m3 = ( (ft * 12) * 2.54) / 100
#
#Task 7 IF statement (Conditional logic)
F = 98.6
F = F + 2.4
if (F >= 100) :
    print ("sick")
else :
    print ("healthy")
print("health check complete")
#
#Task 8 
t8 = 0
u8 = 4
v8 = 6
if (u8 < v8) :
    print(u8, '<', v8)
    t8 += 1
if (u8 <= v8) :
    print(u8, '<=', v8)
    t8 += 1
if (u8 == v8) :
    print(u8, '==', v8)
    t8 += 1
if (u8 >= v8) :
    print(u8, '>=', v8)
    t8 += 1
if (u8 > v8) :
    print(u8, '>', v8)
    t8 += 1
if (u8 != v8) :
    print(u8, '!=', v8)
    t8 += 1

print('u8=', u8, 'v8=', v8, 't8=', t8)
#
#Task 9
idx = 1
nxt = idx + 1
if (nxt < daysL) :
    print('today is', days[idx])
    print('tomorrow must be', days[nxt])
else : print(nxt, 'is too big')
print("back to sequential mode")
#
# Task END
###########################################################
# Collaboration Challenge
#
# S10ccq Q5
StartHere( "Kike Otufale", "S10wcc", "Spring 2025")

# S10ccq Q7
gr = [89, 75, 96, 64, 85, 94]
g7 = stats.mean( gr )
if (g7 > 84 ) :
    print('Good but not great')
else : print('I can do better')
print('g7 =', g7)
    
#
# S10ccq Q8 
gr = gr + [92]
A8 = stats.mean( gr )
if (A8 >= 85) :
    print('Good but not great')
else : print('I can still do better')
print('A8=', A8)
#
# S10ccq Q9
gr[1] = 90
A9 = stats.mean(gr)
if (A9 >= 85 ) :
    print('Getting better')
else : print( 'I can still do better')
print ('A9=', A9)
#
# S10ccq Q10
xtra = days + ['halloween', 'tax day', 'pi day']
XL = len(xtra)
if (XL > 7):
    XL = XL - 2
    print( xtra[XL])
print('XL=', XL)
    
#
# S10ccq Q11 & Q12
n = inches
b = False
if (n > 15) :
    print ( n, "is greater than 15")
    b = (not b)
print("This code is not part of the IF statement")
#
# Task Q14 & Q15 & Q16
gBm = 80
gB = 83
gBp = 87
mygrade = (g7 - y)
msg = 'The grade is higher than C and qualifies for '
if (mygrade >= gBm) :
    if (mygrade >= gBp) :
        msg += 'B+'
    else :
        if (mygrade >= gB) :
            msg += 'B'
        else:
            msg += 'B-'
    print(msg)
else:
    print('The grade is C+')
print('The calculated score is', mygrade)
#
# Collaboration Challenge   End
###########################################################
# Individual Challenge
#
# S10icq Q1
StartHere( "Kike Otufale", "S10wccic", "Spring 2025")
print( gr[idx])
# S10icq Q2 & Q3
ht = [61, 52, 72, 82, 86, 87, 86, 79, 71, 54, 62, 51]
at = stats.mean(ht)
if (at < 70 ):
    print('Less than 70')
else:
    print('Greater than 70')

#
# S10ICq Q4
xt = min(ht)
if (xt < 80 ):
    print ('Below 80')
else :
    print ('Above 80')
#
# S10ICq Q5
NYC = 40.71
MIA = 25.77
ATL = 33.75
DAL = 32.79
if ATL > DAL :
    LAT = 'North'
else :
    LAT = 'South'
print('LAT=', LAT)

#
# S10ICq Q6
if (g7 > A9) :
    print ("g7 is larger")
else :
    print("A9 is larger")
D6 = A9 + g7
#
# Individual Challenge  Save and close
EndHere( globals() )
#exit()
###########################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$>-LPNPJ%TYZKFQJ%4ZXJWX4PNPJTYZKFQJlSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
