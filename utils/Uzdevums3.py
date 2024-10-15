def calculate_interval_sum(a, n):
    return sum(range(a, a + n))

def main():
    try:
        a_input = input("Ievadiet intervāla sākumu a: ")
        n_input = input("Ievadiet skaitu n: ")
        a = int(a_input)
        n = int(n_input)
        if n <= 0:
            raise ValueError("n jābūt pozitīvam veselim skaitlim.")
    except ValueError as ve:
        print(f"Ievades kļūda: {ve}")
        return
    
    S = calculate_interval_sum(a, n)
    print(f"Saskaitot {n} skaitļus no {a}, summa ir {S}")
