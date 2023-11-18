def square_root(x):
    guess = x / 2
    epsilon = 1e-12  # Define the desired level of accuracy
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess
def main():
    x = float(input("Enter a number: "))
    result = square_root(x)
    print("Square root:", result)
if __name__ == '__main__':
    main()