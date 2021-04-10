# Use words.txt as the file name
fname = input("Enter file name: ")

#using try to handle the wrong file name or extension
try:
    fh = open(fname)
except:
    print("ERROR: Cannot Open file .",fname)
    quit()

# using loop For loop
for line in fh:
  # Removing the blank lines
  line = line.rstrip()
  # convering into Upper case latters
  line = line.upper()
    print(line)
