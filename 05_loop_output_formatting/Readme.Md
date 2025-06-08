# 🔢 Print Numbers Without Spaces

This Python script reads an integer `n` and prints all integers from 1 through `n` consecutively without spaces or newlines between them.

---

## 🧠 Problem Statement

Given a positive integer `n`, print the sequence of integers from 1 up to `n` as a single continuous string without any spaces or newline characters in between.

---

## 🧾 Input Format

A single integer `n`.

---

## 📤 Output Format

Print the integers from 1 to `n` concatenated together without spaces or newlines.

---

## 🧪 Sample Input

```

3

```

### Sample Output

```

123

````

---

## 🧱 Code Explanation

```python
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')
````

* `range(1, n + 1)` generates integers from 1 through `n`.
* `print(i, end='')` prints each integer without adding a space or newline, resulting in a continuous sequence.

---

## 📁 Project Structure

```bash
python-mastery-hackerrank-practice/
└── 05_loop_output_formatting/
    ├── print_numbers_no_space.py
    └── README.md
```

---

## 🙌 Tips

* Use the `end` parameter of `print()` to control output formatting.
* Avoid string concatenation or string methods to solve the problem.

---

## 🔐 License

MIT

```
