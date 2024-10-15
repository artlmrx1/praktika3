def calculate_sum(n):
    S = 0
    for i in range(1, n + 1):
        term = i ** i
        if i % 2 == 0:
            S -= term
        else:
            S += term
    return S

def main():
    try:
        user_input = input("Ievadiet naturālu skaitli n: ")
        n = int(user_input)
        if n <= 0:
            raise ValueError("Skaitlim jābūt pozitīvam.")
    except ValueError as ve:
        print(f"Ievades kļūda: {ve}")
        return
    
    S = calculate_sum(n)
    print(f"Summa S = {S}")

