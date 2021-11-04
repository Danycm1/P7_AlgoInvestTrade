from bruteforce import bruteforce
from optimized import optimized
from file import get_info_from_file
import time

def Menu():
    print('Menu Principal:')
    print('1. Force brute')
    print('2. Optimisé')
    print('3. Quitter')

while True:
    Menu()
    try:
        choice = int(input('Select an option: '))
        if choice == 1:
            start = time.time()
            result = bruteforce(500, get_info_from_file(input('Select a CSV file: ')))
            print("Voici la liste d'action les plus rentable pour un budget maximum de 500€", '\n')
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result[1]]), '\n')
            print(f"Notre bénéfice total s'élève à {result[0]} €", '\n')
            end_time = round(time.time() - start, 2)
            print(f"Temps d'exécution: {end_time} secondes", '\n')
        if choice == 2:
            start = time.time()
            result = optimized(500, get_info_from_file(input('Select a CSV file: ')))
            print("Voici la liste d'action les plus rentable pour un budget maximum de 500€", '\n')
            print('\n'.join([str(x) for x in result]), '\n')
            print(f'Notre bénéfice total s"élève à {round(sum([x[2] for x in result]), 2)}€', '\n')
            end_time = round(time.time() - start, 2)
            print(f"Temps d'exécution: {end_time} secondes", '\n')
        if choice == 3:
            quit()
    except ValueError:
        print("Sélectionner un numéro valide")
