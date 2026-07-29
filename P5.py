import csv
data = [
    ['Name','Age',"City"],
    ['Namrata',20,"Mumbai"],
    ['Arpita',20,"Pune"],
    ['Poorva',19,"Devgad"]
]

with open('people.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

data_dicts = [
    {'Name':'Namrata','Age':'20','City':'Mumbai'},
    {'Name':'Poorva','Age':'19','City':'Devgad'}
] 
with open('people_dict.csv','w',newline='') as file:
    filenames = ['Name','Age','City']
    writer = csv.DictWriter(file, fieldnames=filenames)
    writer.writeheader()
    writer.writerows(data_dicts)

with open('people.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('people_dict.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} from {row['City']}")