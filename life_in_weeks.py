#original
'''age = input("What is your current age?")

days = int(age) * 365
weeks = int(age) * 52
months = int(age) * 12
current_age = 90 - age
time_left = current_age_days + current_age_weeks + current_age_months
time_left = (current_age_days + 'days, ') + current_age_weeks + 'weeks, ' + current_age_months + 'months')
print('You have ' + time_left)
'''
#refactored
age = input("What is your current age?")

years = 90 - int(age) 
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")