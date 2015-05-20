#How would you print just the 10th line of a file?
#Hint:
#1. If the file contains less than 10 lines, what should you output?
#2. There's at least three different solutions. Try to explore all possibilities.

# Read from the file file.txt and output the tenth line to stdout.
awk 'NR == 10' file.txt

# Read from the file file.txt and output the tenth line to stdout.
sed -n '10p' file.txt

# Read from the file file.txt and output the tenth line to stdout.
tail -n+10 file.txt | head -n1
