from tabulate import tabulate
#import sqlite3
#import tkinter as tk

'''root = tk.Tk()
root.title("Welcom!")

label = tk.Label(root, text = "Zoo Mangament System")
label.pack()




root.mainloop()'''




#animal Class
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
    

#mammal class
class Mammal(Animal):
    def __init__(self,  name, age, species, diet, fur_color):
        super().__init__(name, age, species, diet)
        self.fur_color = fur_color

    def give_birth(self):
        user_input = input(f"is {self.name} the {self.species} pregnent: Yes/No? : ").lower().strip()

        if user_input == 'yes':
            print(f"Take {self.name} the {self.species} to the regular checkup")
        elif user_input=="no":
            print(f"Keep {self.name} the {self.species} in breeding section!")
        else:
            print("Invalid input")


#Bird class
class Bird(Animal):
    def __init__(self,  name, age, species, diet, feathers_color):
        super().__init__(name, age, species, diet)
        self.feathers_color = feathers_color

    def fly(self):
        print(f"{self.name} the {self.species} is flying with its beautiful {self.feathers_color}")


    def sound(self):
        print(f"{self.name} the {self.specis} is making the sound chirp")   


#Reptile class
class Reptile(Animal):
    def __init__(self, name, age, species, diet, scales):
        super().__init__(name, age, species, diet)
        self.scales = scales

    
    def egg(self):
        print(f"{self.name} the {self.species} is laying eggs with its beautiful {self.scales}")

    def sound(self):
        print(f"{self.name} the {self.species} is making the sound hiss")
    


class Enclosure():
    def __init__(self, name, size, capacity, type):
        self.name = name
        self.size = size
        self.capacity = capacity
        self.animals = []
        self.type = type

    def add_animals(self, animal):
        if not self.is_full() and self.is_compactible(animal):
            self.animals.append(animal)
            print(f"{animal.name} the {animal.species} is added  to the {self.name}")
        else:
            if self.is_full():
                print(F"{animal.name} cannot be added to the as {self.name} is full")
            else:
                print(f"{self.name} is not compactible with {animal.species}. {animal.name} cannot be added there")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} the {animal.species} has been removed from {self.name}")
        else:
            print(f"{animal.name} is not present in {self.name}")

    def is_full(self):
        return len(self.animals) >= self.capacity
    
    def is_compactible(self, animal):
         if isinstance(animal, Mammal) and self.type.lower() == "land":
            return True
         elif isinstance(animal, Bird) and (self.type.lower() == "aviary" or self.type.lower() == "bird"):
            return True
         elif isinstance(animal, Reptile) and self.type.lower() == "reptile":
                return True
         return False



class Zookeeper():
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
        self.animal_assigned = []
    
    
    def assign_animal(self, animal):
        self.animals_assigned.append(animal)
        print(f"{animal.name} the {animal.species} has been assigned to {self.name}.")

    
    def feed_animals(self):
        for animal in self.animal_assigned:
            animal.eat()
    


        


#creating Objects
generic_animal = Animal("Generic Name", 10, "Unknown", "Omnivore")
lion = Mammal("jack", 10, "Lion", "Carnivor", "Golden" )
tiger = Mammal("john", 11, "Tiger", "Carnivore", "Orange")
peacock = Bird("hira", 3, "Peacock",  "Herbivore", "Blue")
snake = Reptile("naag", 4, "Python", "Carnivore", "Black with yellow stripes")




mammal_enclosure = Enclosure("Mammal's Den", 500, 3, "land") 
bird_enclosure = Enclosure("Aviary World", 1000,  5, "aviary")
reptile_enclosure = Enclosure("Reptile House", 400,   2, "reptile")


mandilal = Zookeeper("Mandilal", 4)
boula = Zookeeper("Boula", 8)

#Add animals to Enclosure
mammal_enclosure.add_animals(lion)
bird_enclosure.add_animals(peacock)
reptile_enclosure.add_animals(snake)

#Assign animal
mandilal.assign_animal(lion)
boula.assign_animal(snake)


# Display zoo information (using tabulate for formatting)
animal_data = [
    [animal.name, animal.species, animal.age, animal.diet] 
    for Enclosure in [mammal_enclosure, bird_enclosure, reptile_enclosure] for animal in Enclosure.animals
]
print(tabulate(animal_data, headers=["Name", "Species", "Age", "Diet"], tablefmt="grid"))

zookeeper_data = [
    [zookeeper.name, zookeeper.experience, [animal.name for animal in zookeeper.animal_assigned]]
    for zookeeper in [mandilal, boula]
]
print(tabulate(zookeeper_data, headers=["Zookeeper", "Experience", "Animals Assigned"], tablefmt="grid"))



#interact with objects and generate output
print("\n--- Generic Animal ---")
generic_animal.eat()
generic_animal.sleep()

print("\n--- Mammal (Lion) ---")
lion.eat()
lion.sleep()
lion.give_birth()





  
