'''
name = "Bengt"
age1 = 30
age2= 40

print(f"Tja {name}, är din ålder {age1}?, du ser ut o vara {age2}...")
'''


'''
#If och Elif sats
x = 10
b = 15
if x > b:
    print("x är mindre än b")
elif b > x:
    print ("b är större än x ")


#if elif else sats
x = 10
b = 15
if x > b:
    print("x är mindre än b")
elif b == x:
    print ("b och x är lika mycket ")
else: 
    print ("b är större än x")
'''

'''
#Beräkna summan tillsammans 
x = 10 
y = 20 

print(f"summan av {x}+{y} är",(x+y))
'''

'''
#While loop
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
'''
#Heltal konvertering
x=42
y = (x)
print(y)
print(type(y))

#Flyttal konvertering
x=3.60
y= (x)
print(y)
print(type(y))

#Lista konvertering
x= ["banana", "apple", "grape"]
y = (x)
print(y)
print(type(y))

#Text konvertering
x="Anna"
y= (x)
print(y)
print(type(y))
'''
'''
#Skapa en sträng som innehåller siffror (t.ex., "123").
#Konvertera den till ett heltal och multiplicera det med 2.
#Förväntat resultat: 246.

#Multiplicera och konvertera siffror till heltal
x="123"
y=2 
z= int(x) 
a=z*y
print(a)    
'''

'''
x=5
y = float(x)
print(y)
z= 3,14
print(int(z))
'''

'''
#Skapa två variabler, x = 10 och y = 3.
#Använd alla grundläggande matematiska operatorer (+, -, *, /, //, %, **) och
#skriv ut resultaten.

x=10
y=3

print(x+y)
print(x-y)
print(x/y)
print(x//y)
print(x*y)
print(x%y)
print(x ** y)
'''




'''
#Skapa en variabel pi = 3.14.
#Konvertera den till ett heltal och skriv ut resultatet.
#Konvertera ett heltal 5 till ett flyttal.
pi=3.14
int_pi = int(pi)
print(int_pi)
x=5
float_x= float(x)
print(float_x)
'''
'''
#Konverterar strängen 5 med int 
x = "5"
y = int(x) 
print(y + 2) 

#Adderar ett valfritt helttal med 10
x = input("Skriv in ett heltal: ")
x= int(x)
print(x+10)

#Konverterar 10 till sträng
x = 10
text = "Summan är: " + str(x)
print(text) 


#Konverterar från flytal till heltal
x=8.5
y= int(x)
print(y)

#Konvertera från heltal till flyttal
z=float(5)
print(z)
'''
'''
#Skriv ett program som frågar användaren om två tal (som strängar).
#Konvertera strängarna till heltal och skriv ut deras summa.


x = input("Skriv första talet: ")
y = input("Skriv andra talet: ")
summa = int(x) + int(y)
print(f"Summan är: {summa}")
'''

'''
#Skapa en variabel med ett tal.
#Konvertera talet till en sträng och skriv ut text som inkluderar det.

x=50
text = "talet är: " + str(x)
print(text)
'''
'''
#Strängar
fornamn = "Anna"
efternamn = "Andersson"
fullnamn = fornamn + " " + efternamn
print(fullnamn) 
'''
'''
text = " Python är Kul! "
print(text.upper()) #PYTHON ÄR KUL! #upper= gör strängen till versaler
print(text.strip()) #Python är Kul! #strip=Tar bort mellanslag mellan strängen
print(text.replace("Kul", "fantastiskt")) #Replace= byter yt en del av strängen
'''

#Skapa en variabel text = "Data Science".
#Skriv ut:
#Första tecknet.
# Sista tecknet.
# De första fem tecknen.
'''
text = "Data"
print(text.replace( "Science", "Data"))

text = "Science"
print(text.replace("Data", "Science"))


text = "Data Science"
print(text[0])
print(text[-1])
print(text[4])
'''

'''
#Skapa en sträng: " Python är roligt! ".
#Använd metoder för att:
#Ta bort mellanslag runt texten.
#Byta ut "roligt" mot "fantastiskt".
#Skriv ut texten i VERSALER.
text="python är roligt"
no_whitespace = text.strip()
print(no_whitespace)

fantastico = no_whitespace.replace("roligt", "fantastiskt")

print(fantastico)

UPPER = fantastico.upper()

print(UPPER)
'''
'''
#Fråga användaren om deras namn och ålder.
#Skriv ut en hälsning som:
#Hej, [namn]! Du är [ålder] år gammal.


name= "Bengt"
age="50"

print(f"Hej {name}, du är {age} år gammal")
'''










