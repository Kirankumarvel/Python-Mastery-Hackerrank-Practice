# 🏫 Second Lowest Grade Finder – Python

This script reads a list of students with their grades and prints the names of the student(s) who have the **second lowest grade**, sorted alphabetically.

---

## 📌 Problem Statement

Given the names and grades for each student in a class of `N` students, your task is to:

* Identify the **second lowest grade**.
* Print the name(s) of **student(s) having the second lowest grade**, each on a new line.
* If multiple students share the same second lowest grade, **print their names alphabetically**.

---

## 🧾 Input Format

* The first line contains an integer `N`, the number of students.
* The next `2 × N` lines alternate between student names and their grades.

### Example Input

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

---

## ✅ Output Format

* Print the name(s) of student(s) with the **second lowest grade**.
* If multiple, print each name on a new line in **alphabetical order**.

### Example Output

```
Berry
Harry
```

---

## 📚 Example Explanation

The list of student records:

```python
[
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39]
]
```

* Unique sorted scores: `[37.2, 37.21, 39.0, 41.0]`
* Second lowest score is `37.21`
* Students with that score: `['Harry', 'Berry']`
* Sorted alphabetically: `['Berry', 'Harry']`

---

## 🧠 How It Works

```python
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1]

    names = sorted([name for name, score in students if score == second_lowest])

    for name in names:
        print(name)
```

### Breakdown

1. **Read Inputs**: Collect `N` student records.
2. **Extract Scores**: Remove duplicates and sort to find the second lowest.
3. **Filter Names**: Identify students with the second lowest score.
4. **Sort Alphabetically**: Print names in lexicographic order.

---

## 🧪 Constraints

* There will **always be at least two different scores**.
* Student names are case-sensitive (e.g., `Harry` ≠ `harry`).
* Duplicate grades are handled using `set()`.

---

## 🗂️ File Structure Suggestion

```
11_second_lowest_score/
├── second_lowest.py
└── README.md
```

---

## 🚀 How to Run

Save the code in a file like `second_lowest.py` and run:

```bash
python second_lowest.py
```

Then enter input as per the format.

---

## ✍️ Author

**Kumar** – Python & Logic Practice


