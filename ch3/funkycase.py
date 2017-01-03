import sys
def funky_case(s):
	letters = [];
	capitalize = False
	for letter in s:
		if capitalize:
			letters.append(letter.upper())
		else:
			letters.append(letter.lower())
		#print(letters)
		capitalize = not capitalize
	return "".join(letters)		
	
if __name__ == "__main__":
	#print("this should work")
	if len(sys.argv) != 2:
		print("input string required")
	else:
		s = sys.argv[1]
		print(funky_case(s))

