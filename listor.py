'''

#Tre olika alternativ välj 1 eller alla för att printa ut
numbers = [1, 2, 3, 4, 5]
words = ["hej", "världen"]
mixed = [1, "två", 3.0, True]
print(numbers) 
print(words)
print(mixed)

'''


'''
#Len beräknar ut antalet objekt i listan 
thislist = ["apple", "banana", "cherry", "kiwi", "pear", 1, 2, 3]
print(len(thislist))

'''

'''
list1 = ["abc", 34, True, 40, "male"]
print(list1)
'''

'''
#Type definierar vilken sort classvilket är list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
'''



'''
#list((abc)) funkar sammma som [abc]
thislist = list(("apple", "banana", "cherry")) #Dubbel paranteser
print(thislist)
'''





'''
#printas enskilt vertikalt
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:

    print(fruit)
'''




'''
#for, if, else
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:
    if fruit !="cherry": #else satsen kommer in här 

        print("I like " + fruit)
    else: print("I don't like " + fruit)
'''



'''
#Lägga till objekt i lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Radera objekt från lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)
'''

'''
#Apple start på 0, banana 1 cherry är 2 därför byts den ut till pear
my_list = ["apple", "banana", "cherry"]
my_list[2] = "pear"
print(my_list)

my_list.insert(3, "orange")
print(my_list)

my_list.append("grape")
print(my_list)
'''




'''
lista = ["Stockholm", "Göteborg", "Nynäshamn", "Nyköping"]
lista.append("Linköping")
print(lista)

lista.remove("Göteborg")
print(lista)
'''




'''
lista = ["Stockholm", "Göteborg", "Nynäshamn", "Nyköping"]
for x in lista:
  print (x)
  if x =="Nyköping":
   break

lista2 = [4, 8, 10, 30, 20]
summera = sum(lista2)

print(f"Summan är:  {summera}")
'''

