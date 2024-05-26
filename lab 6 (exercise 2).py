def print_right_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

def main():
    height = int(input("Enter the height of the triangle (number of rows): "))
    print_right_triangle(height)

if __name__ == "__main__":
    main()