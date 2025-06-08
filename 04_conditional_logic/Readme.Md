# 🗓️ Leap Year Checker

This script determines whether a given year is a **leap year** based on Gregorian calendar rules.

---

## 🧠 Problem Statement

A leap year contains an extra day (February 29) to correct the difference between the calendar year and the Earth's orbit. According to the Gregorian calendar, a year is a leap year if it meets the following criteria:

- ✅ The year is divisible by 4  
  **AND**
- ❌ Not divisible by 100  
  **UNLESS**
- ✅ It is also divisible by 400

---

## 🧾 Input Format

A single integer representing the year.

```

year = int(input())

```

---

## 📤 Output Format

Returns a Boolean:

- `True` → if the year is a leap year  
- `False` → if the year is **not** a leap year

Output is handled by the code stub using `print()`.

---

## ✅ Constraints

- `1900 <= year <= 10^5`

---

## 🧪 Sample Input

```

1990

```

### Sample Output

```

False

````

---

## 🧱 Code Breakdown

```python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
````

### 🔍 Explanation

| Year | Divisible by 4 | Div. by 100 | Div. by 400 | Leap Year? |
| ---- | -------------- | ----------- | ----------- | ---------- |
| 1990 | ❌              | -           | -           | No         |
| 2000 | ✅              | ✅           | ✅           | Yes        |
| 1900 | ✅              | ✅           | ❌           | No         |
| 2024 | ✅              | ❌           | -           | Yes        |

---

## 📁 Project Structure

```bash
python-mastery-hackerrank-practice/
└── 04_conditional_logic/
    ├── leap_year_check.py
    └── README.md
```

---

## 🙌 Notes

* This is a popular beginner-level Python task.
* Mastering these kinds of logic checks helps build strong foundations for coding interviews.

---

## 🔐 License

MIT

```


