try:
  fname = input("Enter a file name: ")
  with open(fname, "r") as f:
    line = 1
    for i in f:
      print(f"LINE NUMBER : {line}")
      print(line.upper())
      line += 1
except FileNotFoundError:
  print("Error!")