name_user=input("please enter your name: ")
gender=input("please enter your gender as male or female:").lower()
while True:
    age_input = input("Enter your age in years: ")
    if age_input.isdigit() and int(age_input) > 0:
         age = int(age_input)
         break
    else:
         hint_text="hint:enter a positive age"
         print(f"please enter a valid age. {hint_text:>10}\n")
days = age * 365
weeks = age * 52
months = age * 12
minutes = days * 24 * 60
seconds = minutes * 60
weeks_left=0
print("\n" + "="*40)
print(f"{name_user}'s Life in Numbers".center(40))
print("="*40)
print(f"{'Unit':<10} | {'Amount':>15}")
print("-"*27)
print(f"{'Days':<10} | {days:>15,}")
print(f"{'Weeks':<10} | {weeks:>15,}")
print(f"{'Months':<10} | {months:>15,}")
print(f"{'Minutes':<10} | {minutes:>15,}")
print(f"{'Seconds':<10} | {seconds:>15,} and counting")
if gender=="male":
     weeks_left=(72*52)-weeks
else:
     weeks_left=(77*52)-weeks
print(f"{name_user},you have {weeks_left} weeks left,based on the average life span")
