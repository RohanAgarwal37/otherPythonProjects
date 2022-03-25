total=input("What was the total bill? $")
tip=input("How much tip would you like to give? 10, 12, 15? ")
people=input("How many people to split the bill? ")

split=(int(total)/int(people))*((int(tip)/100)+1)
final=round(split,2)
print(f"PAID BY EACH PERSON {final}")