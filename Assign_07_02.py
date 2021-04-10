# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("ERROR: Unable to open this file",fname)
count = 0
all_values = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    count = count + 1
    all_values = all_values + float(line[line.find(':')+1:])
avg = all_values/count
print('Average spam confidence:',avg)
