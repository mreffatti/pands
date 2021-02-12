nums = []

num = int(input("enter number (0 to quit): "))
while num != 0:
 nums += [num]

 num = int(input("enter number (0 to quit): "))

for x in nums:
 print (x)

average = float(sum(nums)) / len(nums)
print (f"The average is {average}")
