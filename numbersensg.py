import math

def examine_number():
    while True:
        try:
            number = int(input("Please enter a whole number (or type 'q' to quit): "))
            if number == 'q':
                break

            # Check even or odd
            if number == 0:
                print("The number is zero.")
            elif number % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")

            # Check perfect square root
            square_root = math.sqrt(number)
            if square_root == int(square_root):
                print("The number has a perfect square root of", int(square_root))
            else:
                print("The number does not have a perfect square root.")

            # Find factors
            factors = []
            for i in range(1, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    factors.append(i)
                    if i * i != number:  # Don't add perfect square root twice
                        factors.append(number // i)  # Add complementary factor

            if not factors:
                print("The number has no factors (except 1 and itself).")
            else:
                print("The factors of the number are:", factors)

        except ValueError:
            print("Invalid input. Please enter an integer.")

examine_number()
