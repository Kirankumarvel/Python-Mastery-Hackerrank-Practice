# 📝 Problem: String Case Swap

## 🔧 Task
You are given a string and your task is to **swap cases** — convert all lowercase letters to uppercase and all uppercase letters to lowercase.

### ✨ Examples
- `Www.HackerRank.com` → `wWW.hACKERrANK.COM`
- `Pythonist 2` → `pYTHONIST 2`

---

## 📥 Input Format
A single line containing a string `s`.

## 📤 Output Format
Print the modified string after case-swapping.

---

## 🔁 Function Signature

```python
def swap_case(s: str) -> str:
````

---

## 🧪 Sample Input

```
HackerRank.com presents "Pythonist 2".
```

## ✅ Sample Output

```
hACKERrANK.COM PRESENTS "pYTHONIST 2".
```

---

## 🚧 Constraints

* The length of `s` is within \[1, 1000].

---

## 📚 Built-in Functions Used

* `str.swapcase()`: Returns a copy of the string with uppercase characters converted to lowercase and vice versa.

---

## 🗂 File Structure

```
16_string_case_swap/
├── swap_case.py       # Solution Code
├── README.md          # Problem explanation and usage
```
