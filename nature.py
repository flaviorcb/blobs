from food import Food
import random

world_width = 800
world_height = 600

born_energy = 10000
reproduction_energy = 200
food_min = 100
food_max = 3000

k = 0.3

def energy_consume(speed, radius):
    return k * ((speed * speed) + radius)
    
def generate_food():
    x = random.randint()
    