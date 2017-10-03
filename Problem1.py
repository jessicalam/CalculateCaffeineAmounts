'''
Calculations for:
1. Amount of hours passed when caffeine levels go below 65 mg. after 1 cup of coffee.
2. Amount of caffeine in body after 24 hours have passed.
3. Amount of caffeine in body after 24 hours have passed while drinking a cup of coffee after every hour.
Done by Kevin Kye and Jessica Lam. For HW3 due on October 5, 2017.
'''


# Set cup count, caffeine and hours.
cup_count = 1
caffeine = 130 * cup_count
hours = 0
# Decrease caffeine by 13% every hour until caffeine levels are below 65mg.
while caffeine > 65:
    caffeine -= caffeine*.13
    hours +=1
print('CAFFEINE VALUES')
print('One cup:  less than 65 mg. will remain after', hours, 'hours')


caffeine = 130 * cup_count
hours = 0
# Decrease caffeine by 13% every hour until 24 hours has passed.
while hours != 24:
    caffeine -= caffeine*.13
    hours+=1
print('One cup:  {:.2f} mg. will remain after 24 hours.'.format(caffeine))


caffeine = 130 * cup_count
hours = 0
# Decrease caffeine by 13% every hour until 24 hours has passed while increasing caffeine by 130 mg. after every hour.
while hours!= 24:
    caffeine -= caffeine*.13
    caffeine+=130
    hours+=1
print('One cup:  {:.2f} mg. will remain after 24 hours.'.format(caffeine))
