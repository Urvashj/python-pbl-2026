import csv 

 

data = [ 

  ["Name", "Age", "Course"], 

  ["Urvashi", 20, "Computer Engineering"], 

  ["Rahul", 21, "Computer Engineering"] 

] 

 

with open("students.csv", "w", newline="") as file: 

  writer = csv.writer(file) 

  writer.writerows(data) 

 

with open("students.csv", "r") as file: 

  reader = csv.reader(file) 

 

  for row in reader: 

      print(row) 