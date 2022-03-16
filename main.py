print("Welcome to the rollercoaster!")
height = int(input("What is your height(cm)? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age =int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child ticket are $5!")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7!")
  if age >= 45 and age <= 55:
    print("You can have a free ride on us!")  
  else:  
    bill = 12
    print("Adult tickets are $12!")

  wants_photos = input("Do you want a photo taken? Y or N. ")
  if wants_photos == "Y":
    #Adding $3 to bill
    bill += 3

  print(f"Your final bill is ${bill}")
  
else:
  print("Sorry! you can not ride!")