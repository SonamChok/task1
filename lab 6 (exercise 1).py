def generate_multiplication_table(number, limit):
    print(f"Multiplication table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

def main():
    number = int(input("Enter the number for which you want the multiplication table: "))
    limit = int(input("Enter the limit up to which you want the table generated: "))
    generate_multiplication_table(number, limit)

if __name__ == "__main__":
    main()