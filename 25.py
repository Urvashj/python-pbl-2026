message = "Global Variable" 

 

def display(): 

  local_message = "Local Variable" 

  print("Inside function:", message) 

  print("Inside function:", local_message) 

 

display() 

 

print("Outside function:", message) 