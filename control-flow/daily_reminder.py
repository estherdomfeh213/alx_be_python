while True:
  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ").lower()
  time_bound = input("Is it time-bound? (yes/no): ").lower()
  
  match priority:
    case "high":
      if time_bound == "yes":
        print("Reminder:",task ,"is a", priority, "priority task that requires immediate attention today!")
    
    case "low":
      if time_bound == "no":
        print("Note:", task, "is a", priority, "priority task. Consider completing it when you have free time.")
        
    case _:
      print("Invalid input")
  break