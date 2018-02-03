print('How many kilometers did you cicyle today?')
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f'Your {kms}km ride was {miles} mi')