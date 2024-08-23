fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)

student_scores = [123, 43, 234, 15, 254, 23, 56, 73, 126, 754, 324, 43]

total_exam_score = sum(student_scores)
print(total_exam_score)

for_total_exam_score = 0
for score in student_scores:
    for_total_exam_score += score
print(for_total_exam_score)

print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

num_sum = 0
for num in range(101):  # True range in 0 - 100. Also, valid solution is range(1, 101)
    num_sum += num

print(num_sum)
