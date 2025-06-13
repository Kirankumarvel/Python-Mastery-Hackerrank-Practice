# 🎓 Student Marks Average Calculator

## 📝 Problem Statement

You are given the names and scores of students in a class. Your task is to store them in a dictionary and calculate the average of a selected student's marks, then print that average rounded to **2 decimal places**.

This problem tests your understanding of:
- List and dictionary usage
- Input/output formatting
- Basic statistical computation

---

## 📥 Input Format

1. The first line contains an integer `n`, the number of students' records.
2. The next `n` lines each contain:
   - A string: the student’s name
   - Followed by three space-separated floats: the student's scores.
3. The last line contains the name of a student to query.

---

## 📤 Output Format

Print the average of the marks obtained by the queried student, rounded to **2 decimal places**.

---

## 🔒 Constraints

- `2 <= n <= 10`
- Each student has exactly 3 marks.
- All student names are unique.
- The queried student will always exist in the input.

---

## 🧪 Sample Input 0

```

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

```

## ✅ Sample Output 0

```

56.00

```

---

## 🧪 Sample Input 1

```

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

```

## ✅ Sample Output 1

```

26.50

````

---

## 🚀 How the Program Works

### Python Code:
```python
if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    marks = student_marks.get(query_name, [])
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")
````

### Breakdown:

* Reads `n` lines and stores each student's name and scores into a dictionary.
* Queries the name and retrieves the corresponding scores.
* Calculates the average using `sum()` and `len()`.
* Prints the result with `.2f` formatting for two decimal precision.

---

## 📂 Folder Structure

```
15_student_average/
├── average_marks.py
└── README.md
```

---

## 🏁 How to Run

```bash
python average_marks.py
```

Enter inputs as per the format to get the result.

---

## 🔑 Key Concepts Covered

* Dictionary operations
* List unpacking
* Type casting
* Average calculation
* Formatted output

---

## 💡 Tip

When using `f"{value:.2f}"`, it ensures that even if the result is a whole number (like `56`), it will still be printed as `56.00`, meeting the requirement for 2 decimal places.

---

