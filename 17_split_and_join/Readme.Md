### 📁 Folder: `17_split_and_join`

# 🧩 Problem: Split and Join a String in Python

## 📝 Task

You are given a string consisting of space-separated words. Your task is to:

* Split the string on spaces `" "`.
* Join the resulting list of words using a hyphen `"-"`.

---

## 🧠 Concept

In Python:

* `.split()` breaks a string into a list based on a delimiter (default is space).
* `.join()` combines elements of a list into a string using the given separator.

### 📌 Example:

```python
line = "this is a string"
line.split()        # ['this', 'is', 'a', 'string']
"-".join(line.split())  # 'this-is-a-string'
```

---

## 🔄 Function Signature

```python
def split_and_join(line: str) -> str:
```

### Parameters:

* `line`: a string of space-separated words.

### Returns:

* A string where words are joined by a hyphen.

---

## 🧪 Sample Input

```
this is a string
```

## ✅ Sample Output

```
this-is-a-string
```

---

## 🚀 How It Works

1. Read input string from the user.
2. Split the string using `.split()`.
3. Join the list of words using `"-".join(...)`.
4. Print the final string.

---

## 💡 Constraints

* Input is a single line of space-separated words.
* Words are alphabetic or numeric with no special characters beyond whitespace.

---

## 📂 File Structure

```
17_split_and_join/
│
├── split_and_join.py        # Main solution file
├── README.md                # This documentation
```

