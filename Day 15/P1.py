import re
pattern = "hello"
text = "hello world"

match = re.search(pattern, text)
print(match)

pattern = "h.llo"
text = "hello world"

match = re.search(pattern,text)
print(match)

pattern = r"\d{3}-\d{3}-\d{4}"
text = "call 996-473-1234 now"
match = re.search(pattern,text)
print(match.group())

pattern = r"\w+"
text = "Hello_123"
match = re.search(pattern,text)
print(match.group())

pattern = r"\s"
text = "Hello World"

match = re.search(pattern,text)
print(match)

pattern = f"[aeiou]"
text = "hello"
matches = re.findall(pattern,text)
print(matches)

pattern = f"[^aeiou]"
text = "hello"
matches = re.findall(pattern,text)
print(matches)