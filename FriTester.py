class Technician:
    def __init__(self, name, age, food, colour, eye, height):
        self.name = name
        self.age = age
        self.food = food
        self.colour = colour
        self.eye = eye
        self.height = height

    def __str__(self):
        return f"{self.name} är {self.age} år gammal och har {self.eye} ögon färg. {self.name} är {self.height} och gillar färgen {self.colour}, men favoritmaten är {self.food}"

def run_the_program(technicians_list):
    while True:
        print("Hej och välkommen din potatis:)")
        print("\nMeny:")
        print("1. Lägg till en vän")
        print("2. Visa alla vänner")
        print("3. Avsluta")

        choice = input("Skriv in ditt val genom att välja alternativ 1, 2 eller 3: ")

        if choice == "1":
            new_name = input("Vad heter du?: ")
            new_age = input("Hur gammal är du?: ")
            new_food = input("Din favoritmat?: ")
            new_colour = input("Din favoritfärg?: ")
            new_eye = input("Din ögonfärg? Svara i plural!: ")
            new_height = input("Din längd?: ")

            new_technician = Technician(new_name, new_age, new_food, new_colour, new_eye, new_height)
            technicians_list.append(new_technician)
            print(f"{new_name} är tillagd som din vän")
            print("Friend added!")

        elif choice == "2":
            print("Alla vänner:")
            for friend in technicians_list:
                print(friend)

        elif choice == "3":
            print("Exiting the menu.")
            break

        while True:
            keep_run = input("Vill du fortsätta? (ja/nej): ")
            if keep_run.lower() == "ja":
                break
            elif keep_run.lower() == "nej":
                exit()

if __name__ == "__main__":
    johan_instance = Technician("Johan", 19, "NTI", "Arboga", "monster", "singel")
    hans_instance = Technician("Hans", 18, "NTI", "Stockholm", "monster", "singel")
    albin_instance = Technician("Albin", 17, "NTI", "Stockholm", "monster", "pimpmaster")

    technicians_list = [johan_instance, hans_instance, albin_instance]

    run_the_program(technicians_list)