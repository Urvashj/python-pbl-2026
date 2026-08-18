import pickle 

 

student = { 

  "name": "Urvashi", 

  "age": 20, 

  "course": "Computer Engineering" 

} 

 

with open("student.dat", "wb") as file: 

  pickle.dump(student, file) 

 

with open("student.dat", "rb") as file: 

  data = pickle.load(file) 

 

print("Data retrieved from binary file:") 

print(data) 