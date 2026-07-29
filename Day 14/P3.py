with open('output.txt','w') as file:
    file.write("India, officially the Republic of India,[j][19] is a country in South Asia.")
    file.write("It is the world's seventh-largest country by area and the largest by population.")

with open('output2.txt','w') as file:
    lines = ["Line 1\n","Line 2\n","Line 3\n"]
    file.writelines(lines)

name = "Namrata"
age = 20
with open('formatted.txt','w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write("Name: {}\nAge: {}\n".format(name,age))

with open('formatted.txt','a') as file:
    file.write("This line is appended")
