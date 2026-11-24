marks=int(input("Enter Your Marks"))
if marks>100 or marks<0:
    print("invalid marks")
elif marks>=90 and marks<=100:
    print("A grade")
elif marks>=80 and marks<90:
    print("B grade")
elif marks>=70 and marks<80:
    print("C grade")
elif marks>=60 and marks<70:
    print("D grade")
else:
    print("Fail")