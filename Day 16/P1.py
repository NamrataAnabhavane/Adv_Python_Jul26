import re
text = "Hello world! This is a test. Phone: 123-456-7890. Email:r@r.com"

#pattern = r"\d{3}-\d{3}-\d{4}"
#match = re.search(pattern,text)
#print(match.group())

match = re.search(r"\d{3}-\d{3}-\d{4}",text)
for match in re.finditer(r"\w+",text):
    print(f"World: {match.group()} at position {match.start()} - {match.end()}")

cleaned = re.sub(r"\d{3}-\d{3}-\d{4}","XXX-XXX-XXXX",text)
print(cleaned)

words = re.split(r"\s+",text)
print(words)