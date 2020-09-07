weight = 90
height = 56
BMI = 703*weight/(height**2)
print(f"BMI is {BMI}")
if BMI < 18.5:
  print("underweight")
elif BMI < 25.0:
  print("normal")
elif BMI < 30.0:
  print("overweight")
else:
  print("obese")

