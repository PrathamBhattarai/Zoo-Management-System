from tabulate import tabulate
#import sqlite3
#import tkinter as tk

'''root = tk.Tk()
root.title("Welcom!")

label = tk.Label(root, text = "Zoo Mangament System")
label.pack()




root.mainloop()'''






















class Animal:
    def __init__(self, name, age, species, diet):
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet
        self.is_resting = False
        self.is_eating = False
        self.is_sleeping = False
    
    def eat(self):
        if not self.is_resting:
            self.is_eating = True
            print(f"{self.name} of {self.species} is eating {self.diet} food")
        else:
            print(f"{self.name} of {self.species} is resting now!")
        
    
    def sleep(self):
        self.is_sleeping ==True
        self.is_eating ==False
        print(f"{self.name} of {self.species} is peacefully sleeping now!")
    

class Mammal(Animal):
    def __init__(self,  name, age, species, diet, fur_color):
        super().__init__(name, age, species, diet)
        self.fur_color = fur_color

    def give_birth(self):
        user_input = input(f"is {self.name} the {self.species} pregnent: Yes/No? : ").lower()

        if user_input == 'Yes':
            print(f"Take {self.name} the {self.species} to the regular checkup")
        elif user_input=="No":
            print(f"Keep {self.name} the {self.species} in breeding section!")
        else:
            print("Invalid input")

#creating Objects
generic_animal = Animal("Generic Name", 10, "Unknown", "Omnivore")
lion = Mammal("jack", 10, "Lion", "Carnivor", "Golden" )

#interact with objects and generate output
print("\n--- Generic Animal ---")
generic_animal.eat()
generic_animal.sleep()

print("\n--- Mammal (Lion) ---")
lion.eat()
lion.sleep()
lion.give_birth()





  
