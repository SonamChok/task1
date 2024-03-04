age=int(input("enter your age:"))
student=input("are you studnt(ye/no):")
if (age<=12) or (age>=13 and age<=18 and student=='yes'):
    print("you are eligibl for discount on the movie ticket")
else:
    print("you are not eligible for discount on the movie ticket")
