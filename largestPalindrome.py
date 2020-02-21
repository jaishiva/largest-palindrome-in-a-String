palindrome = ""
def largestPalindrome(inputArray):
	index =0 
	loop = 0
	length = len(inputArray)
	global palindrome
	while(index < length-1):
		checkForPalindrome(inputArray[:length-index])
		index += 1
		
	loop +=1
	if loop < length-1:
		largestPalindrome(inputArray[loop:])
	else:
		print(f'largest palindrome is {palindrome}')

def checkForPalindrome(checkingArray):
	length = len(checkingArray)
	global palindrome
	for i in range(int((length)/2)):
		if checkingArray[i] != checkingArray[length-i-1]:
			return False
		if i == int(length/2)-1:
			if len(palindrome) < length:
				palindrome = checkingArray


if __name__ == '__main__':
	largestPalindrome('bandoaaadfmfopfknlsidffghfdhnsdfhbdfhfjuajndajfhahfhfahfkalsgsg')