# S11_LogicH_StarterFile.py  <- this is the Starter File for Session 11
# K.Schmitz (c) 2022,2023, 2024
#  Starter File for CIS2010 Session 11, Python Hash Function
##################Initialization information, do not modify ################
#
from cis2010utils4 import StartHere, EndHere, strhash
import pandas as pd
#####################################################################################
# Start Workshop
#
# Task 2 
StartHere( "Kike Otufale", "S11w", "Spring 2025")

#Task 3 setup variables
x3 = 0
dd = ", doo-doo"
fish = ['minow', 'bass', 'tuna', 'shark']
fm = ['baby', 'mommy', 'daddy', 'grandma', 'grandpa']
fmL = len( fm )
sk = " "
sk += fish[3]   #incrament a string
x3 += 1         #incrament a number

#
#Task 4 If statement
who = fm[0]
e4 = who + sk
x4 = 0
if (x4 < 3) :
    x4 += 1
    e4 += dd
if (x4 < 3) :
    x4 += 1
    e4 += dd
if (x4 < 3) :
    x4 += 1
    e4 += dd
if (x4 < 3) :
    x4 += 1
    e4 += dd
if (x4 < 3) :
    x4 += 1
    e4 += dd

print(e4)

#
#Task 5 FOR Loop
zoo = ['lions', 'tigers', 'bears']
msg5 = ""  #message (empty)
for item in fish :
    msg5 += " baby " + item
    print(msg5)
print(item)

#
# BING Copilot  https://bing.com/copilot
# enter this prompt to Copilot
#  Build a python loop to print the message “I will not facebook in class” six times using the loop variable i6. In the post-loop afterparty print the message “…until tomorrow”, then also print the loop variable.
#
#Task 6
for i6 in range(5):
    print("I will not facebook in class")

print("...until tomorrow")
print("Loop variable:", i6)

#
#Task 7
#setup variables
doodoos = 3
who = fm[0]
who2 = who + sk
ew = ""
ew += who2
H7a = strhash(ew)
print("earworm 1")
#loop
for a in range(doodoos) :
    ew += dd
ew += '\n' #End of Line
print(ew)
H7c = strhash(ew)
#
#Task 8
EOL = '\n'
v = 3
ew2 = ""
print("earworm 2")
# nested loop
for b in range(v) :
    ew2 += who2
    for a in range(doodoos) :
        ew2 += dd
    ew2 += EOL
ew2 += (who2 + EOL)
print( ew2)
H8b = strhash(ew2)
#
#Task 9
print("earworm 3")
ew9 = ""
for who in fm :
    who2 = who + sk
    for b in range(v) :
        ew9 += who2
        for a in range(doodoos) :
            ew9 += dd
        ew9 += EOL
    ew9 += (who2 + EOL)
print(ew9)
H9a = strhash(ew9)
L9a = len(ew9)
#
#Task 10
GAc = pd.read_csv('GAcodes.csv')
hx = strhash( str(GAc))
# Workshop END
#
###########################################################
# Collaboration Challenge
#
# S11ccq Q6 
StartHere( "Kike Otufale", "S11wcc", "Spring 2025")

# S11ccq Q7
ce = ['hello', 'WORLD']
ceH = strhash( str(ce))

#
# S11ccq Q8
grades = [92, 74, 84, 89, 95]
grades = grades + [79]
cnt = len(grades)
total = 0
for item in range(cnt) :
    score = grades[item]
    total = total + score
total = (total / cnt)
print('final grade is', total)

#
# S11ccq Q11
jz = 0
cz = 0
for jz in range(10) :
    cz += 1
print(jz)
print(cz)
#
# S11ccq Q12
sv = 0
for lv in range(19):
    sv += 2
print(lv)
print(sv)


#
# Collaboration Challenge END
#
###########################################################
# Individual Challenge
#
# S11icq Q1 
StartHere( "Kike Otufale", "S11wccic", "Spring 2025")
print( strhash( str(grades[1])))
#
# S11icq Q3
a3 = ""
m3 = "hello"
a3 = a3 + a3
a3H = strhash(a3)
#
# S11icq Q4
a2 = "Hello"
m2 = "World"
a2 = a2 + m2 + '!'
pyQ4 = strhash(a2)
#
# S11icq Q5
se = fm[4]
sf = fish[2]
sg = se + sf

#
# S11icq Q6
for sm in range(2) :
    sg = sg + dd
print (sg)
sgH = strhash( str(sg))
sgL = len(sg)

#
# S11icq Q9
for item in range(5) :
    print('this works!')
    
for item in grades :
    print('this works!')
   
for item in ew2 :
    print('this works!')

for item in fish :
    print('this works!')

    
#
# S11icq Q10

ans9 = ' '
for k in range(5) :
    ans9 += "hello "

ans9 = ans9 + "world"
ans9H = strhash(ans9)

#
# Individual Challenge  END
EndHere( globals())
#exit()
###########################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$>-LPNPJ%TYZKFQJ%4ZXJWX4PNPJTYZKFQJlSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
