file = open("student.txt", "w") 

file.write("Name: Urvashi\n") 

file.write("Course: Computer Engineering\n") 

file.close() 

 

file = open("student.txt", "a") 

file.write("Subject: Python for Data Science\n") 

file.close() 

 

file = open("student.txt", "r") 

content = file.read() 

file.close() 

 

print(content) 