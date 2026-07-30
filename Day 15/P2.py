import re

pattern = r"ab*"
text = "a ab abb abbb"
matches = re.findall(pattern,text)
print(matches)

pattern = r"ab+"
text = "a ab abb abbb"
matches = re.findall(pattern,text)
print(matches)

pattern = r"ab?"
text = "a ab abb abbb"
matches = re.findall(pattern,text)
print(matches)

pattern = f"a{3}"
text = "aa aaa aaaa"
matches = re.findall(pattern,text)
print(matches)

pattern = r"a{2,}"
text = "a aa aaa aaaa"
matches = re.findall(pattern,text)
print(matches)

pattern = "a{2,3}"
text = "a aa aaa aaaa"
matches = re.findall(pattern,text)
print(matches)