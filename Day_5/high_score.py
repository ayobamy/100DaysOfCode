student_scores = input("Input a list of students scores:  ").split()

for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

max_score = 0
# highest_score = max(student_scores)
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
