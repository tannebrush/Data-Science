#If och Elif sats
'''
x = 15
b = 11
if x > b:
    print("x är större än b")
elif b < x:
    print ("b är mindre än x ")
'''

#if elif else sats
'''
x = 15
b = 10
if x > b:
    print("x är större än b")
elif b == x:
    print ("b och x är lika mycket ")
else: 
    print ("b är mindre än x")
'''

#While loop
'''
i = 1
while i < 6:
    print (i)
    i +=1

#While loop break
i = 1 
while i < 6:
    print (i)
    if i == 3:
     break
    i +=1
'''


#If else
'''
x= 18
b= 15
input("Din ålder: ")
if x > b:
    print("Du är minderårig")
else: 
    print("Du är myndig")
'''


#if elif else while true
'''
while True:

    tal = float(input("Skriv in ett tal (eller skriv 'q' för att avsluta): "))


    if tal > 0:
        print("Talet är positivt.")
    elif tal < 0:
        print("Talet är negativt.")
    else:
        print("Talet är noll.")


    fortsätt = input("Vill du fortsätta? (j/n): ").strip().lower()
    if fortsätt == 'n':
        print("Programmet avslutas. Hej då!")
        break
'''


#1 % räknar ut om talet är jämnt eller udda genom att dividera med 2
'''
tal = int(input("Skriv in ett heltal: "))


if tal % 2 == 0:
    print("Talet är jämnt.")
else:
    print("Talet är udda.")
'''

#2 Foor loop 1-10
'''
for i in range (1,11):
    print (i)
'''

#Poängsystem 
'''
point=int(input("Mata in poäng: "))


if (point>=0) and (point<=150):

    if point>80:
        print("A")
    elif point>70:
        print("B")
    elif point>600:
        print("C")
    elif point>50:
        print("D")
    elif point>20:
        print("E")
    else:
        print("F")
else: 
    print("fel inmatning)")
'''
