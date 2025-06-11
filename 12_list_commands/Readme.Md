# 🧾 List Operations – HackerRank Challenge

This project implements a basic list command interpreter in Python. It reads a series of commands (e.g., `insert`, `append`, `remove`, etc.) and performs these operations on a dynamic list. This challenge is inspired by HackerRank’s *“Python List Operations”* problem.

---

## 📂 File Structure

```

12\_list\_commands/
├── list\_operations.py
└── README.md

```

---

## 🧠 Problem Statement

You are given a number of commands to perform on an initially empty list. Your task is to process these commands in order and print the list whenever the `print` command is encountered.

### 📥 Input Format

- The first line contains an integer **N**, the number of commands.
- The next **N** lines each contain a command, one of the following:

```

insert i e   # Insert e at index i
print        # Print the current list
remove e     # Delete the first occurrence of e
append e     # Append e at the end
sort         # Sort the list
pop          # Pop the last element
reverse      # Reverse the list

```

> ⚠️ All added elements are integers.

---

### 🧾 Sample Input

```

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

```

### 📤 Sample Output

```

\[6, 5, 10]
\[1, 5, 9, 10]
\[9, 5, 1]

````

---

## 📌 Constraints

- 1 ≤ N ≤ 1000
- All elements are integers and within reasonable bounds for list operations.

---

## 🧰 Features Implemented

| Command   | Description                                |
|-----------|--------------------------------------------|
| `insert`  | Inserts an element at a specific position  |
| `append`  | Adds an element at the end                 |
| `remove`  | Removes the first occurrence of an element |
| `sort`    | Sorts the list in ascending order          |
| `pop`     | Removes the last element                   |
| `reverse` | Reverses the order of the list             |
| `print`   | Outputs the current list state             |

---

## 🧑‍💻 How It Works

Each input line is split into tokens. The first token is the command, and the rest are treated as arguments.

The logic uses:

- `.insert(i, e)`
- `.append(e)`
- `.remove(e)`
- `.sort()`
- `.pop()`
- `.reverse()`
- `print(list)`

to manipulate the list dynamically.

---

## ✅ Example Usage

```bash
$ python list_operations.py
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
````

---

## 🚀 Learning Objectives

* Practice list operations in Python.
* Learn command parsing using `split()`.
* Understand control flow using conditional statements.
* Improve problem-solving using basic data structures.

---
