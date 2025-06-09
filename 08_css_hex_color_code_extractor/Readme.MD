# 🎨 CSS HEX Color Code Extractor

This Python script extracts valid **HEX color codes** from CSS property values, ignoring any CSS selectors that start with a `#`.

---

## 📘 Problem Statement

You're given multiple lines of CSS code. Your task is to extract all **valid HEX color codes** that appear **inside property values**, not as selectors.

### ✅ A valid HEX color code:
- Must start with a `#`.
- Should have either **3** or **6** hexadecimal digits.
- Can include digits `0-9` and letters `a-f` or `A-F`.
- Letters can be lowercase or uppercase.
- **Must not be at the start of a CSS rule (i.e., not a selector).**

---

## 📥 Input Format

- The first line contains an integer `n`, the number of lines of CSS code.
- The next `n` lines contain valid CSS code (without comments).

---

## 📤 Output Format

Print each valid HEX color code (that appears in a CSS value) on a new line, in the order of their appearance.

---

## 🧪 Sample Input

```

11
\#BED
{
color: #FfFdF8; background-color:#aef;
font-size: 123px;
background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
\#Cab
{
background-color: #ABC;
border: 2px dashed #fff;
}

```

### ✅ Sample Output

```

\#FfFdF8
\#aef
\#f9f9f9
\#fff
\#ABC
\#fff

````

---

## 🧠 Explanation

- `#BED` and `#Cab` are CSS selectors, not property values — they are **excluded**.
- HEX codes inside `{}` blocks are **included**.

---

## 📜 Regex Pattern Used

```python
pattern = re.compile(r'(?<!^)(?<![\w])#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})(?![\w])')
````

| Component          | Description                                    |
| ------------------ | ---------------------------------------------- |
| `(?<!^)`           | Not at the start of a line (exclude selectors) |
| `(?<![\w])`        | Not preceded by a letter/number (isolated `#`) |
| `#`                | Match the literal `#`                          |
| `[0-9a-fA-F]{3,6}` | Exactly 3 or 6 hex digits                      |
| `(?![\w])`         | Not followed by letters/numbers                |

---

## 📁 Project Structure

```
python-mastery-hackerrank-practice/
└── 09_css_hex_color_code_extractor/
    ├── hex_color_code_extractor.py
    └── README.md
```

---

## 🛠️ Topics Covered

* Regular expressions (regex)
* Negative lookaheads and lookbehinds
* String parsing
* Pattern matching
* CSS syntax understanding

---

## 🔐 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
