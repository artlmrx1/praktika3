import random
from math import prod

def generate_natural_number():
    return random.randint(1, 20) 

def calculate_product(a, b):
    return prod(range(a, b + 1))

def main():
    a = generate_natural_number()
    b = generate_natural_number()
    print(f"Ģenerētie skaitļi: a = {a}, b = {b}")
    
    if a > b:
        a, b = b, a
        print(f"Skaitļi mainīti vietām: a = {a}, b = {b}")
    elif a == b:
        print("a = b, R = 1")
        return
    
    R = calculate_product(a, b)
    print(f"Reizinājums no {a} līdz {b} ir R = {R}")

