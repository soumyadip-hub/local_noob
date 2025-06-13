# ----function part2--------
# def sum_all_nums(num1,num2,num3,num4,num5):
#     return num1+num2+num3+num4+num5
# print(sum_all_nums(4,6,8.7,9,3))
# print(sum_all_nums(3,5,2,56,78))
#using args -------------- doing above easily
def sum_all_nums(*args):
    total=0
    for num in args:
        total += num
    return total
print(sum_all_nums(4,6,7,89,3))
print(sum_all_nums(4,6))

# --------using kargs------
def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favourite colour is {color}")
    
fav_colors(david="purple", ruby="skyred", putra="black")

