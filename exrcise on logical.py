age= int(input("Enter your age:"))
student=input("Are you studnt(yes/no):")
if (age<=12) or (age>=13 and age<=18 and student=='yes'):
    print("you are elligible for discount on the movie ticket")
else:
    print("you are not elgible for discount on the movie ticket")
    