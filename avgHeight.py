# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height=0
for height in student_heights:
  total_height += height

number = 0
for student in student_heights:
  number += 1

avg_height = round(total_height/number)
print(f"average height of the class is {avg_height}")