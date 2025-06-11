if __name__ == '__main__':
    students = []
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        students.append([name, score])

    # Find the second lowest score
    unique_scores = sorted({score for _, score in students})
    if len(unique_scores) > 1:
        second_lowest = unique_scores[1]
        # Get names of students with the second lowest score
        names = sorted([name for name, score in students if score == second_lowest])
        print("\nStudents with the second lowest score:")
        for name in names:
            print(name)
    else:
        print("There is no second lowest score.")
