# ------using map function(using lambdas)-----
nums = [2,4,6,89,1]
doubles = map(lambda x: x*2, nums)
for num in doubles:
    print(num)

# ----------------
people = ["abhishek","nobin","indranil","mir","sourendu"]

peeps = map(lambda name: name.upper(), people)

print(list(peeps))

