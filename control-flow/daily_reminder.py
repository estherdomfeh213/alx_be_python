while True:
  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ").lower()
  is_time = input("Is it time-bound? (yes/no): ").lower()
  
  match priority:
    case "high":
      if is_time == "yes":
        print("Reminder:",task ,"is a", priority, "priority task that requires immediate attention today!")
    
    case "low":
      if is_time == "no":
        print("Note:", task, "is a", priority, "priority task. Consider completing it when you have free time.")
        
    case _:
      print("Invalid input")
  break