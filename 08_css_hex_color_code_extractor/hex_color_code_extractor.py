import re

css_lines = []
n = int(input())
for _ in range(n):
    css_lines.append(input())

# Regex to match valid hex color codes (not as selectors)
pattern = re.compile(r'(?<!^)(?<![\w])#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})(?![\w])')

for line in css_lines:
    matches = pattern.findall(line)
    for match in matches:
        print(match)
