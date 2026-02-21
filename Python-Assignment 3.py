
Answer1
"""""
limit = 42.0
length = float(input("Enter the length of the zander in centimeters: "))

if length < limit:
    missing_cm = limit - length
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing_cm:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")

 Answer2

cabin = input("Enter the cabin class (LUX, A, B, or C): ")

if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

Answer3

gender = input("Enter biological gender (male/female): ").lower()
hb = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hb < 117:
        print("Your hemoglobin is low.")
    elif 117 <= hb <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
elif gender == "male":
    if hb < 134:
        print("Your hemoglobin is low.")
    elif 134 <= hb <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")

 Answer4

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    """
    