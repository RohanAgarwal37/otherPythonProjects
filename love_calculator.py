# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1=name1.lower()
lower_name2=name2.lower()
combined_name=lower_name1+lower_name2
t_count=combined_name.count("t")
r_count=combined_name.count("r")
u_count=combined_name.count("u")
e_count=combined_name.count("e")
l_count=combined_name.count("l")
o_count=combined_name.count("o")
v_count=combined_name.count("v")
fst=t_count+r_count+u_count+e_count
scn=l_count+o_count+v_count+e_count

score=fst*10+scn

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos")
elif score>40 and score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")