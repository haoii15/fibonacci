import sys

def recursive(n):
    if n <= 1:
        return n
    else:
        return (recursive(n - 1) + recursive(n - 2))

def non_recursive (i, file):
    fib = 0
    prev = 0
    last = 0

    for n in range(0, i):
        if n <= 1:
            last = prev
            prev = n
            fib = prev + last
        else:
            fib = prev + last
            last = prev
            prev = fib

        file.write(f"Non-recursive: {fib}\n")
    
    file.write("\n")

def fibonacci(i):
    file = open("../results/fibonacci.txt", "w+")
    non_recursive(i, file)

    for n in range(i):
        r = recursive(n)
        file.write(f"Recursive: {r}\n")

    file.close()
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Bad Call! Please enter the wanted length of the Fibonacci sequence as an argument:\n\n\tpython3 fibonacci.py <length>\n")
    else:
        n = 0
        try:
            n = int(sys.argv[1])
        except:
            print("The given length is not an integer.")
        
        if n != 0:
            fibonacci(n)

