"""Convert a non-negative whole number to binary and hexadecimal."""

def main():
    try:
        number = int(input("Enter a non-negative whole number: "))
        if number < 0:
            print("Please enter zero or a positive whole number.")
            return
    except ValueError:
        print("Please enter a valid whole number.")
        return

    print(f"Decimal: {number}")
    print(f"Binary: {bin(number)[2:]}")
    print(f"Hexadecimal: {hex(number)[2:]}")

if __name__ == "__main__":
    main()
