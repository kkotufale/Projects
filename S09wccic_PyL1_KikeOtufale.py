# S09_Logic1_StarterFile.py  <- this is the Starter File for Session 09
# K.Schmitz (c) 2023,2024,2025
#  Starter File for CIS2010 Session 09, Python Logic 1
##################Initialization information, do not modify ################
#
from cis2010utils4 import StartHere, EndHere, strhash
#####################################################################################
# Start Workshop
#
# Task 2
StartHere( "Kike Otufale", "S09w", "Spring 2025")
# This is a comment, prior line is code

#
#Task 4 numbers
a = 123
b = 456.78
age = 32
print(a, type(a) )
print(b, type(b) )
#
#Task 5 math operations + - ** / * ()
print( a - age)
c = 2/3
d = a - 100
e = 2 ** 8
n5 = e * (b - a)
n = 0
n= n + 1
#
#Task 6 Boolean
b6 = True
c6 = (a >= b)
d6 = (a > age)
e6 = (not c6)
f6 = b == 123
print(b6 == c6)
#
#Task 7 Text Strings
s7 = "hello world"
a7 = "123"
c7 = '2/3'
#len and print functions
count = len(s7)
print( s7, count)
#convert to str & to int
x2 = int(a7)
x3 = float(a7)
x4 = str(c)
x5 = str(x3)
#increment & concatenate
h7 = "baby"
h7 = h7 + " shark" #increment
i7 = ', doo-doo'
j7 = h7 + i7       #concatenate
#substrings and slicing
print( j7)
print( j7[0] )
print( j7[0:3] )
k7= j7[5:10]
print ( k7 )


#Task 8 lists
store = ['milk', 'eggs', 'bread', 'chips', "dip"]
print( store[0] )
print( store[1] )
#modify the list
store[1] = 'banana'
#
#Task 9 create & fix fatal error
yesterday = "Mon"
today = yesterday + "day"
print( 'value=', today)


# Workshop END
###########################################################
# Collaboration Challenge START
#
# S09ccq Q4
StartHere( "Kike Otufale", "S09wcc", "Spring 2025")

#
# S09ccq Q5
c5 = 17.305 + 12.77
print( c5 )
#
# S09ccq Q6
a6 = 5 * 4 * 3 * 2 * 1
print( a6 )

#
# S09ccq Q7
x7 = 144
y7 = 7.5
v7 = x7 / (y7 - 5)
print( v7 )
#
# S09ccq Q8
score = (93 * .3) + (79 * .35) + (87 * .35)
print( score )
#
# S09ccq Q9
F9 = 98.6
K9 = (F9 + 459.67) * (5.0 / 9.0)
print( K9 )
#
# S09ccq Q10
F9 = 98.6
R = F9 + 459.67
print( R )
#
# S09ccq Q11
K = 1
F = (K - 273.15) * (9 / 5) + 32
print( F )

#
# S09ccq Q12 & Q13
sb = 'a dream'
sa = 'I have'
sc = 'today!'
scALL = [sa, sb, sc]
print(sa, sb, sc)

#
# Collaboration Challenge END
###########################################################
# Individual Challenge START
#
# S09icq Q1
StartHere( "Kike Otufale", "S09wccic", "Spring 2025")
#
# S09icq Q2
miles = 68.0
km = miles * 1.60934
print( km )
#
# S09icq Q3
speed = 4.8
dist = 64
dur = dist / speed
print ( dur )
#
# #S09icq Q4
sx="Give me your tired, "
sx2="your poor, "
sx3="your huddled masses "
sx4="yearning to breathe free"
sx5 = sx + sx2 + sx3 + sx4
c4 = len(sx5)

#
#S09icq Q5
print(sx2, sx3, sx4)

#
# S09icq Q6
t6 = [9, 8, 7, 6, 5, 4, 3] 
print( t6[4] )

#
# S09icq Q7
z7 = len (t6)
#
# S09icq Q8
print ( scALL )
sca = scALL[2]
z8 = len( sca )
scb = sca[0]
#
# S09icq Q9
pi = 3.1415
r = 13
area = pi * (r ** 2)
print ( area )
#
# Individual Challenge  Save and close
EndHere( globals() )
#exit()
###########################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$>-LPNPJ%TYZKFQJ%4ZXJWX4PNPJTYZKFQJlSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
