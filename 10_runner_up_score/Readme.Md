# 🥈 Runner-Up Score Finder

This Python script takes a list of participant scores from a sports event and determines the **runner-up** (second highest) score.

---

## 📌 Problem Statement

You're given the scores of participants in a sports competition. Your task is to:

* Read `n` scores from input.
* Print the second-highest (runner-up) score.

---

## 🧾 Input Format

* The first line contains an integer `n` — the number of scores.
* The second line contains `n` space-separated integers — the participant scores.

---

## ✅ Constraints

* `2 <= n <= 100`
* `-100 <= score <= 100`

---

## 🧮 Output Format

Print the **runner-up score** (second highest unique value).

---

## ▶️ Sample Input

```
5
2 3 6 6 5
```

## 🟢 Sample Output

```
5
```

---

## 🧠 Explanation

* The list of scores: `[2, 3, 6, 6, 5]`
* The highest score is `6`, appearing twice.
* The second-highest score is `5`, so that's the runner-up.

---

## 🛠️ How It Works

The script:

1. Reads the input.
2. Converts the scores to a list.
3. Removes all instances of the highest score.
4. Finds the new highest score (runner-up).

---

## 💻 File Structure

```
10_runner_up_score/
├── README.md
└── runner_up.py
```

---

## 🚀 Usage

Run the script in a terminal:

```bash
python runner_up.py
```

Then input the number of participants and their scores when prompted.

