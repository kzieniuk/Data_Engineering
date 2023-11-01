import random

dinosaur_names = [
    "Tyrannosaurus Rex",
    "Triceratops",
    "Stegosaurus",
    "Brachiosaurus",
    "Velociraptor",
    "Diplodocus",
    "Ankylosaurus",
    "Pteranodon",
    "Allosaurus",
    "Spinosaurus",
    "Parasaurolophus",
    "Compsognathus",
    "Archaeopteryx",
    "Iguanodon",
    "Carnotaurus",
    "Microraptor",
]

sizes = ["Small", "Medium", "Large", "Huge"]

weights = [f"{random.randint(1, 10)} tons", f"{random.randint(11, 50)} tons", f"{random.randint(51, 100)} tons"]


class Dinos():
    def __init__(self):
        self.name = random.choice(dinosaur_names)
        self.weight = random.choice(weights)
        self.size = random.choice(sizes)
        self.age = random.randint(3, 50)

    def __call__(self):
        return (self.name, self.weight, self.size, self.age)

def get_dino(dinos):
    name, weight, size, age = dinos()
    return {
        'name': name,
        'weight': weight,
        'size': size,
        'age': age,
    }
