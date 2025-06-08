# 🧮 Integer and Float Division in Python

This script reads two integers from the user and prints the result of:

1. Integer Division (`//`)
2. Float Division (`/`)

---

## 📘 Problem Statement

**Task:**  
The provided code reads two integers, `a` and `b`, from input.

You need to:
- Print the result of **integer division**: `a // b`
- Print the result of **float division**: `a / b`

**Note:**  
- Do **not** round or format the output.
- Print the result on **two separate lines**.

---

## 🧾 Input Format

```

First line: integer a
Second line: integer b

```

---

## 📤 Output Format

```

First line: result of integer division a // b
Second line: result of float division a / b

```

---

## 🧪 Sample Input

```

4
3

```

### ✅ Sample Output

```

1
1.3333333333333333

````

---

## 🧠 Explanation

| Expression | Description                            | Result              |
|------------|----------------------------------------|---------------------|
| `4 // 3`   | Integer division → quotient only       | `1`                 |
| `4 / 3`    | Float division → full decimal result   | `1.3333333333333333`|

---

## 🧱 Code Breakdown

```python
if __name__ == '__main__':
    a = int(input())   # Read first integer from input
    b = int(input())   # Read second integer from input

    print(a // b)      # Integer division: no decimals
    print(a / b)       # Float division: includes decimals
````

---

### 🔍 What Each Line Does

* `int(input())`: Reads user input and converts it from a string to an integer.
* `a // b`: Performs integer division (e.g., `4 // 3 = 1`).
* `a / b`: Performs float division (e.g., `4 / 3 = 1.333...`).
* `print(...)`: Outputs the results on separate lines.

---

## 📁 File Location

```bash
python-mastery-hackerrank-practice/
└── 02_basic_input_output/
    └── integer_float_division.py
```

---

## 🙌 Tips

* Use `//` when you only want the whole number result.
* Use `/` when you need precision with decimals.
* This concept is often tested in coding interviews to check understanding of operators.

---

## 🔐 License

This script is open-sourced under the MIT License.


---

Let me know if you'd like this saved as an actual `.md` file or if you want to add automated test cases next!
```
