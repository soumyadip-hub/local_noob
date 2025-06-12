# #milage converter
# print("how many kilometer did you cycle today")
# kms = input()
# miles = float(kms)/1.60943
# miles = round(miles,2)
# print(f"your {kms} km to {miles} miles")

#------------- ------------ -------------------

#------conditional statements------

color = input("whats your favourite colour?\n")
if color == 'purple':
    print("execellent choice")
elif color == 'teal':
    print("not bad")
elif color == 'seafoam':
    print("mediacore")
elif color == 'pure darkness':
    print("i like how you think")
else:
    print("you monster!")
# ~~~~~ ~ ~ ~ ~ ~ ~ ~~ ~~~ ~ ~ ~ ~ ~
#----[bouncer]------
age = input("how old you are: ")#ask for age
#---------rule to bouncer(if anyone want to entry)----)
#               18-21 years wristband
#               21+ years normal entry
#               too young, sorry
if age:
    age = int(age)
    if age >= 21:
        print("you are good to enter and can drink!")
    elif age >= 18:
        print("you can enter,but need wristband")
    else:
        print("you can't came in,little one! :(")
else:
    print("please ener the age")

