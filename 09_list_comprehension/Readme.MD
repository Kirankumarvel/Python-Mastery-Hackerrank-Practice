# 🧮 3D Grid List Comprehension

## 📘 Problem Statement

You're given three integers `x`, `y`, and `z` representing the dimensions of a cuboid, and an integer `n`.

Your task is to print a list of all possible coordinates `[i, j, k]` on a 3D grid such that:

- `0 <= i <= x`
- `0 <= j <= y`
- `0 <= k <= z`
- `i + j + k != n`

Use **list comprehension** instead of multiple nested loops, as a learning exercise.

---

## 🧠 Input Format

The input contains 4 lines:
```

x
y
z
n

```

Each line contains one integer.

---

## 📌 Constraints

```

0 < x, y, z <= 7
0 <= n <= x + y + z

```

---

## 📤 Output Format

Print a list of all valid `[i, j, k]` coordinates that do **not** sum to `n`, in **lexicographic increasing order**.

---

## ✅ Sample Input 0

```

1
1
1
2

```

### ➕ All possible combinations:
```

\[0, 0, 0]  => sum = 0
\[0, 0, 1]  => sum = 1
\[0, 1, 0]  => sum = 1
\[0, 1, 1]  => sum = 2 ❌
\[1, 0, 0]  => sum = 1
\[1, 0, 1]  => sum = 2 ❌
\[1, 1, 0]  => sum = 2 ❌
\[1, 1, 1]  => sum = 3

```

### ✅ Valid Output:
```

\[\[0, 0, 0], \[0, 0, 1], \[0, 1, 0], \[1, 0, 0], \[1, 1, 1]]

```

---

## 🧪 Sample Input 1

```

2
2
2
2

```

### 🎯 Sample Output 1
```

\[\[0, 0, 0], \[0, 0, 1], \[0, 1, 0], \[0, 1, 2], \[0, 2, 1], \[0, 2, 2],
\[1, 0, 0], \[1, 0, 2], \[1, 1, 1], \[1, 1, 2], \[1, 2, 0], \[1, 2, 1],
\[1, 2, 2], \[2, 0, 1], \[2, 0, 2], \[2, 1, 0], \[2, 1, 1], \[2, 1, 2],
\[2, 2, 0], \[2, 2, 1], \[2, 2, 2]]

```

---

## 🗂️ File Structure

```

09\_list\_comprehension/
├── 3d\_grid.py       # Main Python script to generate coordinates using list comprehension
└── README.md        # Problem description, input/output formats, examples, and explanation

````

---

## 🧑‍💻 Usage

Run the script using Python 3:

```bash
python 3d_grid.py
````

Provide the input as 4 lines (x, y, z, n), and the output will be printed accordingly.

---

## 🏁 Learning Goals

* Practice list comprehensions in Python.
* Understand how to work with multidimensional iteration.
* Improve problem-solving using concise and readable code.

---

