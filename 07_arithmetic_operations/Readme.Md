# ➕ Arithmetic Operations

This Python script performs basic arithmetic operations—**sum**, **difference**, and **product**—on two user-provided integers.

---

## 🧠 Problem Statement

You are given two integers. Write a Python program that prints three lines:

1. The **sum** of the two numbers
2. The **difference** (first - second)
3. The **product** (first × second)

Each result should be printed on a new line.

---

## 🧾 Input Format

- The first line contains an integer `a`.
- The second line contains an integer `b`.

---

## 📤 Output Format

Print three lines:

- Line 1 → `a + b`
- Line 2 → `a - b`
- Line 3 → `a * b`

---

## 🔍 Example

### ✅ Sample Input
```

3
2

```

### ✅ Sample Output
```

5
1
6

````

---

## 🧱 Code Breakdown

```python
if __name__ == '__main__':
    a = int(input())  # Read first number
    b = int(input())  # Read second number

    print(a + b)      # Sum
    print(a - b)      # Difference
    print(a * b)      # Product
````

---

## 📁 Project Structure

```bash
python-mastery-hackerrank-practice/
└── 07_arithmetic_operations/
    ├── arithmetic_operations.py
    └── README.md
```

---

## 🧠 Concepts Covered

* Input handling
* Arithmetic operations (`+`, `-`, `*`)
* Standard output formatting

---

## 🔐 License

MIT


