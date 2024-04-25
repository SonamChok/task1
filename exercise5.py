for i in range(1,10):
    if i == 3:
        print("skipping 3 in the inner loop")
        continue
    
    elif i == 7:
        print("reached 7, breaking outer loop")
        break
    
    else:
        print(i)