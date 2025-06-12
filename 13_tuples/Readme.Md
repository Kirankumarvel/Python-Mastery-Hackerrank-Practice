# 🧮 Tuple Hash Calculator

This simple Python script reads a list of integers from input, stores them in a tuple, and prints the hash of the tuple using Python's built-in `hash()` function.

---

## 📝 Problem Statement

**Task**  
Given an integer `n` and `n` space-separated integers, create a tuple of those integers. Then compute and print the result of `hash(tuple)`.

---

## 🧠 Concepts Covered

- Reading and parsing input
- Using tuples in Python
- The `hash()` built-in function

---

## 📥 Input Format

- The first line contains an integer, `n`, the number of elements.
- The second line contains `n` space-separated integers.

---

## 📤 Output Format

- Print the result of `hash(tuple)` on a new line.

---

## 🧾 Example

### ✅ Sample Input
```

2
1 2

```

### ✅ Sample Output
```

3713081631934410656

````

*(Note: Hash output may vary based on Python version unless hash randomization is disabled)*

---

## ✅ Constraints

- `1 <= n <= 10^5`
- The integers provided will be within the 32-bit signed integer range.

---

## 💡 How It Works

- Input is read from standard input using `input()`.
- `map(int, input().split())` converts input strings to integers.
- `tuple()` converts the mapped integers to a tuple.
- `hash()` computes the hash of the tuple for use in hash-based data structures or comparison.

---

## 💻 Example Code: `tuple_hash.py`

```python
if __name__ == '__main__':
    n = int(input())  # Read number of elements
    integer_list = tuple(map(int, input().split()))  # Read and convert input to tuple
    print(hash(integer_list))  # Print hash of the tuple
````

---

## 📌 Usage

Run the script and provide input as prompted:

```bash
$ python tuple_hash.py
```

---

## 🏁 Output

You’ll get the hash value of the tuple as an integer.

---

## 🔒 Notes

* `hash()` ensures immutability and fast access for data structures like sets and dictionaries.
* Tuples are hashable only if all elements inside are also hashable (e.g., integers).

---

---

Let me know if you’d like this converted into a blog post or integrated into a learning series!
```
