from random import randint, shuffle

for i in range(5):
    nums = set()
    while len(nums) < 6:
        nums.add(randint(1, 45))

    print(nums)
    
print("=====================")

for i in range(5):
    nums = list(range(1, 46))
    shuffle(nums)
    print(nums[:6])
