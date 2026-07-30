import re

pattern = r"^Hello"
text = "Hello World"
matches = re.search(pattern,text)
print(matches)

pattern = r"Hello$"
text = "Hello World"
matches = re.search(pattern,text)
print(matches)

pattern = r"\bword\b"
text = "word words wordy"
matches = re.findall(pattern,text)
print(matches)