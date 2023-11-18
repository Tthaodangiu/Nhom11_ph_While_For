while True:
    bits = input("Enter 8 bits (or blank line to exit): ")
    if bits == "":
        break
    if len(bits) != 8 or not bits.isdigit():
        print("Invalid input. Please enter 8 binary digits (0s and 1s).")
        continue
    count_ones = bits.count("1")
    if count_ones % 2 == 0:
        parity_bit = "0"
    else:
        parity_bit = "1"
    print(f"Parity bit should be: {parity_bit}")
