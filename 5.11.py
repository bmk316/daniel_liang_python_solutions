#Highest and second highest Score

num_of_students = eval(input("Enter the number of students: "))
num_of_scores = 0
scores = []

while num_of_scores < num_of_students:
    for i in range(num_of_scores):
        score = eval(input("\nEnter student",i,"'s", "scores: "))
        scores.append(score)
        num_of_scores += 1

print("\nThe maximum score is " + str(max(scores)))
scores.pop(num_of_students - 1)
print("\nThe second highest is " + str(max(scores)))









