for i in range(1, 10):
    if i == 7:
        break
    elif i == 3:
        continue
    else:
        print("Outer Loop:", i)
        for j in range(1, 10):
            if j == 3:
                continue
            print("Inner Loop:", j)