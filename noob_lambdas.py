# # built -in - functions
# # ------using map function(using lambdas)-----
# nums = [2,4,6,89,1]
# doubles = map(lambda x: x*2, nums)
# for num in doubles:
#     print(num)

# # # ----------------
# people = ["abhishek","nobin","indranil","mir","sourendu"]

# peeps = map(lambda name: name.upper(), people)

# print(list(peeps))

# # ------filter function(example1)-----------
# names = ["austin","penny","augusta","sombu","aritra"]
# a_names = filter(lambda n: n[0]=='a', names)
# print(list(a_names))
# # --------filter function(example2)-------
# users = [
#     {"username": "samirul","tweets": ["i love biriyani","i love chai also"]},
#     {"username": "kartik","tweets": ["i love pussy"]},
#     {"username": "jeff","tweets":[]},
#     {"username": "bob34","tweets":[]},
#     {"username": "samuel","tweets": ["i love hacking"]},
#     {"username": "jolly","tweets":[]},
# ]
# inactive_users = list(filter(lambda u: u['tweets'] , users))
# print(inactive_users)
# ---------MAX-MIN FUNCTION-----------

names = ['arya',"simpson","dora","tim","ollivia"]
print(min(len(name) for name in names))
print(max(names, key=lambda n:len(n)))