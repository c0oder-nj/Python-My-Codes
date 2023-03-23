def is_palindrome(input_string):
	new_string = input_string.replace(" ","").lower()
	reverse_string = new_string[::-1]
	# Traverse through each letter of the input string
 
	if(new_string == reverse_string):
		return True
	else:
		return False
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True