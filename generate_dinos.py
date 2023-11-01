import json
import random

from dinosaurs import Dinos, get_dino

dinosaur_data = []

for _ in range(10001):
    dinosaur = get_dino(Dinos())
    dinosaur_data.append(dinosaur)

# Write the data to a JSON file
with open("dinosaur_data.json", "w") as json_file:
    json.dump(dinosaur_data, json_file, indent=4)

