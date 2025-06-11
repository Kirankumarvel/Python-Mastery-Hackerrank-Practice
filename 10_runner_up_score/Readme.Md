# 🥈 Runner-Up Score – Python

This Python script reads a list of scores from standard input and prints the **runner-up score** — the second highest unique value in the list.

---

## 📝 Problem Description

Given the participants' score sheet for a university sports day, you are required to find the **runner-up score**.

---

## 📥 Input Format

* The first line contains an integer `n`: the number of scores.
* The second line contains `n` space-separated integers representing the scores.

---

## 📤 Output Format

Print the runner-up score (second highest unique score).

---

## ✅ Constraints

* `2 <= n <= 10`
* `-100 <= score <= 100`
* No duplicate values for the top two scores.

---

## 🔍 Example

**Input**

```
5  
2 3 6 6 5
```

**Output**

```
5
```

**Explanation**

* Scores: `[2, 3, 6, 6, 5]`
* Highest score: `6`
* Runner-up: `5` (second highest)

---

## 🧠 Code Explanation

```python
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    highest = max(arr)
    filtered = [x for x in arr if x != highest]
    print(max(filtered))
```

### 🔹 Step-by-step:

* `n = int(input())`: reads the number of scores.
* `arr = list(map(int, input().split()))`: reads and converts scores to a list of integers.
* `highest = max(arr)`: finds the maximum score.
* `filtered = [x for x in arr if x != highest]`: removes all instances of the highest score.
* `print(max(filtered))`: prints the second highest score.

---

## 🗂️ File Structure

```
10_runner_up_score/
├── runner_up.py
└── README.md
```

---

## 🚀 How to Run

```bash
python runner_up.py
```

Provide input when prompted or pipe it from a file.

---
