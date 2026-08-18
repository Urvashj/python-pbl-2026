student = { 

  "name": "Urvashi", 

  "age": 20, 

  "course": "Computer Engineering" 

} 

 

print("Student details:", student) 

print("Name:", student["name"]) 

 

student["age"] = 21 

student["semester"] = 5 

 

print("Updated dictionary:", student) 

 

del student["semester"] 

print("After deletion:", student) 