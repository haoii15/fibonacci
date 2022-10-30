import sys

def recursive(n):
    """
    Recursive Fibonacci function.
    Finds Fibonacci number n.
    """
    # Handles the edge cases where n < 2
    if n <= 1:
        return n
    
    # For all other n, f(n-1) and f(n-2) is called
    else:
        return (recursive(n - 1) + recursive(n - 2))

def non_recursive (i, file):
    """
    Non-Recursive Fibonacci function.
    Finds a sequence of Fibonacci numbers starting at 0 and ending on i.
    Writes the sequence to file.
    """

    # Variables for the Fibonacci number and the two previous Fibonacci numbers
    fib = 0
    prev = 0
    last = 0

    # Iterates the whole range
    for n in range(0, i):

        # Edge cases
        if n <= 1:
            prev = n
            fib = prev + last
        
        # Finds Fibonacci number i and updates last and prev to their new values
        else:
            fib = prev + last
            last = prev
            prev = fib

        file.write(f"Non-recursive: {fib}\n")
    
    file.write("\n")

def fibonacci(i):
    """
    Function who calls both Fibonacci functions.
    Writes the two Fibonacci sequences to a file.
    """
    file = open("../results/fibonacci.txt", "w+")
    non_recursive(i, file)

    for n in range(i):
        r = recursive(n)
        file.write(f"Recursive: {r}\n")

    file.close()
        
if __name__ == '__main__':
    # Check if the command line call is done right, and if not give instructions
    if len(sys.argv) != 2:
        print("Bad Call! Please enter the wanted length of the Fibonacci sequence as an argument:\n\n\tpython3 fibonacci.py <length>\n")
    else:
        # Variable for storing the length argument from command line
        n = 0
        # Try to make sure the argument is an integer 
        try:
            n = int(sys.argv[1])
        except:
            print("The given length is not an integer.")
        
        # When the argument is an integer, runs the Fibonacci function
        if n != 0:
            fibonacci(n)

