while True:
  task = input("Enter your task: ")
  is_priority = input("Priority (high/medium/low): ").lower()
  is_time = input("Is it time-bound? (yes/no): ").lower()
  
  match is_priority:
    case "high":
      if is_time == "yes":
        print("Reminder:",task ,"is a", is_priority, "priority task that requires immediate attention today!")
    
    case "low":
      if is_time == "no":
        print("Note:", task, "is a", is_priority, "priority task. Consider completing it when you have free time.")
        
    case _:
      print("Invalid input")
  break