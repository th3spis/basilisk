import sys
import re

# flag a registry key with heavily mixed casing

print("arg = " + r"{}".format(sys.argv[1]))

for word in re.split("\\\\|/", sys.argv[1]):
	print(word)
	switches = 0
	for i in range(1, len(word)):
	    if word[i].islower() != word[i-1].islower():
	        switches += 1

	print("Length: " + str(len(word)))
	print("Total: " + str(switches))

	print("Heavily mixed: " + str(switches > len(word) / 2))
	print("\n")

