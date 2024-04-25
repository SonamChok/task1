height=int(input("Enter the height of the triangle (number of rows):"))
print("right triangle pattern:")
for i in range(1, height+1):
    for j in range(1, i+1):
        print("*", end="")
    print()