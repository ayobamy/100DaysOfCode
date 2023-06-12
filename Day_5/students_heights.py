# sum students height

heights = input("Input a list of students height: ").split()
print(heights)

for h in range(0, len(heights)):
    heights[h] = int(heights[h])
    print(heights)

total_height = 0
for height in heights:
    total_height += height

num_students = 0
for s in heights:
    num_students += 1

avg_height = round(total_height / num_students)

# print(avg_height)
