data = input()
file_data = open(data, 'r')
nums = []

while True:
    line = file_data.readline()
    if not line:
        break
    nums.append(int(line.strip()))
file_data.close()

med = sorted(nums)[len(nums)//2]
steps = 0
for i in nums:
    steps += abs(i - med)

print(steps)

