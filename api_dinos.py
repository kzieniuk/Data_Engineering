from fastapi import FastAPI
from pydantic import BaseModel
from dinosaurs import Dinos, get_dino

app = FastAPI()




@app.get("/random_dinosaurs/")
def get_random_dinosaurs(count: int = 1001):
    dinosaurs = [get_dino(Dinos()) for _ in range(count)]
    return dinosaurs