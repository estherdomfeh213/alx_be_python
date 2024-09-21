while True:
  pattern_size = int(input("Enter the size of the pattern:"))
  
  if pattern_size > 0: 
    row = 0
    
    while row < pattern_size:
      for cols in range(pattern_size):
        print("*", end="")
      print()
      row += 1
    break
  else:
    print("Please enter a positive integer.")