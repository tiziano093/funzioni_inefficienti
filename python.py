import psutil
from memory_profiler import memory_usage

def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

def concatenate_strings(lst):
    result = ""
    for item in lst:
        result += item
    return result

def create_squares(n):
    squares = []
    for i in range(n):
        squares.append(i * i)
    return squares

def find_max(lst):
    max_val = float('-inf')
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def filter_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

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

if __name__ == "__main__":
    test_functions()
