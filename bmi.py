# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=weight/(height**2)
final="{:.2f}".format(bmi)
print(final)
if bmi<18.5:
  print(f"your bmi is {final}, you are under weight.")
elif 18.5<=bmi<25:
    print(f"your bmi is {final}, you have normal weight.")
elif 25<=bmi<30:
    print(f"your bmi is {final}, you are slightly over weight.")
elif 30<= bmi <35:
    print(f"your bmi is {final}, you are obese.")
else:
    print(f"your bmi is {final}, you are clinically obese.")
