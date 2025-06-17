### 📁 Folder: `18_mutate_string`

# 🧬 Mutate a String

## 📝 Problem Description

In Python, strings are immutable—meaning you cannot directly modify characters using indexing. However, you can achieve string mutation by converting the string to a list or using slicing.

In this task, you're given:

* A string
* An index position
* A character

Your goal is to replace the character at the given position with the provided character and print the new string.

---

## ✅ Example

### 🧾 Input

```
abracadabra
5 k
```

### ✅ Output

```
abrackdabra
```

---

## 📚 Function Signature

```python
def mutate_string(string: str, position: int, character: str) -> str:
```

---

## 📥 Input Format

* The first line contains the string `s`.
* The second line contains the integer `position`, followed by the new `character`, separated by a space.

---

## 📤 Output Format

* A single line containing the modified string.

---

## 🧠 Sample Walkthrough

Given the string:

```
abracadabra
```

And you need to mutate the character at position 5 with `'k'`:

```python
string[:5] => 'abrac'
string[6:] => 'dabra'
```

Result:

```python
'abrac' + 'k' + 'dabra' => 'abrackdabra'
```

---

## 💡 Implementation

```python
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```

---

## 🔒 Constraints

* `0 <= position < len(string)`
* The input string is non-empty and contains only printable characters.


