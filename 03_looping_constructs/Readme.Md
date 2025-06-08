# 🔁 Square of Non-Negative Integers

This Python script reads a single non-negative integer `n` and prints the square of each integer from `0` to `n - 1`, each on a new line.

---

## 🧠 Problem Statement

**Task:**  
Given an integer `n`, print the square of all non-negative integers less than `n`.

---

## 🧾 Input Format

- A single line containing an integer `n`.

---

## 📤 Output Format

- `n` lines of output.
- Each line contains the square of `i` where `0 <= i < n`.

---

## ✅ Constraints

```

0 <= n <= 20

```

---

## 🧪 Sample Input

```

5

```

### ✅ Sample Output

```

0
1
4
9
16

````

---

## 🧱 Code Explanation

```python
if __name__ == '__main__':
    n = int(input())       # Step 1: Read integer input
    for i in range(n):     # Step 2: Loop from 0 to n-1
        print(i * i)       # Step 3: Print square of each i
````

### 🔍 Breakdown:

| Step         | Description                                               |
| ------------ | --------------------------------------------------------- |
| `input()`    | Reads user input from the console                         |
| `int(...)`   | Converts the string input to an integer                   |
| `range(n)`   | Generates a sequence from 0 up to (but not including) `n` |
| `i * i`      | Calculates the square of each value of `i`                |
| `print(...)` | Outputs each result on a new line                         |

---

## 📁 File Location

```bash
python-mastery-hackerrank-practice/
└── 03_looping_constructs/
    ├── square_non_negative.py
    └── README.md
```

---

## 🙌 Tips

* `range(n)` is exclusive of `n`, so it will loop from `0` to `n - 1`.
* Squaring numbers is a great way to practice basic math with loops.
* This is a common warm-up problem in coding interviews and contests.

---

## 🔐 License

This project is licensed under the [MIT License](../LICENSE).

```

