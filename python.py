# Importa i moduli necessari per il monitoraggio delle prestazioni
import psutil
from memory_profiler import memory_usage

# Definisce una funzione per sommare tutti gli elementi di una lista
def sum_list(lst):
    total = 0  # Inizializza la variabile total a 0
    for number in lst:  # Cicla attraverso ogni elemento nella lista
        total += number  # Aggiunge l'elemento corrente al totale
    return total  # Restituisce il totale calcolato

# Definisce una funzione per concatenare tutte le stringhe in una lista
def concatenate_strings(lst):
    result = ""  # Inizializza una stringa vuota per il risultato
    for string in lst:  # Cicla attraverso ogni stringa nella lista
        result += string  # Aggiunge la stringa corrente al risultato
    return result  # Restituisce la stringa concatenata

# Definisce una funzione per creare una lista di quadrati dei numeri da 0 a n-1
def create_squares(n):
    squares = []  # Crea una lista vuota per i quadrati
    for i in range(n):  # Cicla da 0 a n-1
        squares.append(i * i)  # Calcola il quadrato di i e lo aggiunge alla lista
    return squares  # Restituisce la lista dei quadrati

# Definisce una funzione per trovare il valore massimo in una lista
def find_max(lst):
    if not lst:  # Controlla se la lista è vuota
        return None  # Restituisce None se la lista è vuota
    max_val = lst[0]  # Imposta il primo elemento come il valore massimo iniziale
    for num in lst:  # Cicla attraverso ogni numero nella lista
        if num > max_val:  # Se il numero corrente è maggiore del massimo trovato finora
            max_val = num  # Aggiorna il massimo
    return max_val  # Restituisce il valore massimo trovato

# Definisce una funzione per filtrare i numeri pari in una lista
#
#
def filter_evens(lst):
    return [num for num in lst if num % 2 == 0] 

# Definisce una funzione per calcolare la somma dei quadrati dei numeri in una lista
#
#
def sum_of_squares(lst):
    return sum(number * number for number in lst) #calcola il quadrato di ogni numero nella lista. sum: per fare la somma 

# Definisce una funzione per generare una lista di numeri pari fino a n
def generate_evens(n):
    evens = []  # Crea una lista vuota per i numeri pari
    for i in range(n):  # Cicla da 0 a n
        if i % 2 == 0:  # Controlla se il numero è pari
            evens.append(i)  # Se è pari, lo aggiunge alla lista
    return evens  # Restituisce la lista dei numeri pari

# Funzione che duplica gli elementi di una lista
def duplicate_items(lst):
    duplicated = [] # Crea una lista vuota per i duplicati
    for item in lst: # Cicla attraverso ogni elemento nella lista
        duplicated.append(item) # Aggiunge l'elemento alla lista dei duplicati
        duplicated.append(item)
    return duplicated # Restituisce la lista dei duplicati

# Funzione che conta le occorrenze di un elemento in una lista
def count_occurrences(lst, element):
    count = 0 # Inizializza il contatore a 0
    for item in lst: # Cicla attraverso ogni elemento nella lista
        if item == element: # Controlla se l'elemento corrente è uguale all'elemento passato
            count += 1 # Se è uguale, incrementa il contatore
    return count # Restituisce il contatore

# Funzione che inverte una stringa
#
#
def reverse_string(s):
    return s[::-1] # slicing 

# Funzione che trova il minimo in una lista
def find_minimum(lst):
    if not lst: # Controlla se la lista è vuota
        return None # Restituisce None se la lista è vuota
    min_val = lst[0] # Imposta il primo elemento come il valore minimo iniziale
    for num in lst: # Cicla attraverso ogni numero nella lista
        if num < min_val: # Se il numero corrente è minore del minimo trovato finora
            min_val = num # Aggiorna il minimo
    return min_val # Restituisce il valore minimo trovato

def profile_function(func, *args):
    p = psutil.Process()
    p.cpu_percent(interval=None)      
    mem_usage = memory_usage((func, args), max_usage=True)
    cpu_percent = p.cpu_percent(interval=None)
    
    print(f"Codice {func.__name__}:")
    print(f"Utilizzo percentuale della CPU: {cpu_percent}%")
    print(f"Uso massimo della memoria: {mem_usage:.2f} MiB\n")

def test_functions():
    lst = list(range(5000))
    str_lst = ["hello" for _ in range(5000)]

    profile_function(sum_list, lst)    
    profile_function(concatenate_strings, str_lst)    
    profile_function(create_squares, 5000)
    profile_function(find_max, lst)
    profile_function(filter_evens, lst)
    profile_function(sum_of_squares, lst)
    profile_function(generate_evens, 5000)
    profile_function(duplicate_items, lst)
    profile_function(count_occurrences, lst, 2500)
    profile_function(reverse_string, concatenate_strings(str_lst))
    profile_function(find_minimum, lst)

if __name__ == "__main__":
    test_functions()
