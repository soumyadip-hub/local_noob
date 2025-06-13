# built -in - functions
# ------using map function(using lambdas)-----
nums = [2,4,6,89,1]
doubles = map(lambda x: x*2, nums)
for num in doubles:
    print(num)

# ----------------
people = ["abhishek","nobin","indranil","mir","sourendu"]

peeps = map(lambda name: name.upper(), people)

print(list(peeps))

#------filter function-----------
names = ["austin","penny","augusta","sombu","aritra"]
a_names = filter(lambda n: n[0]=='a', names)
print(list(a_names))

