
'''
#Felhantering
try:
    x= int("hej") 
except:
    print("Ett fel uppstod")


try:
    x= int("123") 
except:
    print(x)


print("Programmet fortsätter här") 
'''


'''
#ValueError
print("fånga specifika fel")

try:
    x =int("hej")
except ValueError:
    print("Ett värdefel uppstod")
'''
'''
#Try-Except-Finally (ZeroDivisionError)
try:
    x = 10/0
except ZeroDivisionError:
    print("Du kan inte dela med 0")
finally: 
    print("programmet fortsätts")
'''


'''
#Felmeddelanden
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Ogiltig e-postadress: Saknar '@'")

try:
    email = input("Ange e-postadress: ")
    validate_email(email)

except InvalidEmailError as e:
    print(f"Fel: {e}")

else:
    print("E-postadressen är giltig.")



finally:
    # Kör oavsett om exception kastas eller inte
    print("Programmet avslutas.")

'''



'''
class InvalidPasswordError(Exception): 
    pass

def validate_password(password):
    if "0" not in password: 
        raise InvalidPasswordError("Måste innehålla minst en nolla '0'")
    
try: 
    password = input("Ange lösenord: ")
    validate_password(password)

except InvalidPasswordError as e: 
    print(f"fel: {e}")

else: print("Lösenord inkorrekt!")

finally: print("programmet avslutas.")
'''

'''
class InvalidAgeRequirmentError(Exception):  
    pass

def validate_requirment(requirment):
    if "18" not in requirment:
        raise InvalidAgeRequirmentError("Måste vara minst'18'")

try:
    requirment = input("Ange ålder: ")
    validate_requirment(requirment)

except InvalidAgeRequirmentError as e:
    print(f"Fel: {e}")

else:
    print("Ålder bekräftad!")  
    
finally:
    print("Programmet avslutas.")
'''



