import asyncio, os, math
from utils import Uzdevums1, Uzdevums2, Uzdevums3, Uzdevums4
from utils.Uzdevums5 import calculate_days

def main():
    while True:
        os.system('cls')
        print('Artjoms Litvinovskis P2-1')
        print('Praktiskais Darbs N3')

        print('select\n1.Uzdevums 1\n2.Uzdevums 2\n3.Uzdevums 3\n4.Uzdevums 4\n5.Uzdevums 5\n6. Exit\n')

        ans = input('> ')

        if ans == '1':
            Uzdevums1.main()
            input('Press Enter to continue...')
        elif ans == '2':
            Uzdevums2.main()   
            input('Press Enter to continue...') 
        elif ans == '3':
            Uzdevums3.main()
            input('Press Enter to continue...')
        elif ans == '4':
            Uzdevums4.main()
            input('Press Enter to continue...')
        elif ans == '5':
            days = calculate_days()
            print(f"\nCementa pietiks {days} dienām.")
            input('Press Enter to continue...')
        elif ans == '6':   
            os.system('exit')   
            break
        else:
            continue 


if __name__ == '__main__':
    main()