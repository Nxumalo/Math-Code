input_string = input("Please enter a binary number: ")

for charactr in input_string:
		if charactr != '0' and charactr != '1':
				print("Error: Must contain only 0 and 1 characters.")
				exit()				    


result = 0									
power_two = 1	    
index_in_input_string = len(input_string)-1 

while index_in_input_string >= 0:
		if input_string[index_in_input_string] == '1':
				result += power_two
		
		power_two *= 2 		
		index_in_input_string -= 1		

print("Your number writes", result, "in decimal format.")
