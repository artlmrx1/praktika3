def calculate_y(x):
    return x**3 + 2*x - 5

def main():
    print(f"{'x':<3} | {'y':<5}")
    for x in range(1, 11):
        y = calculate_y(x)
        print(f"{x:<3} | {y:<5}")
