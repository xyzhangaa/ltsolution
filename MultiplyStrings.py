###Given two numbers represented as strings, return multiplication of the numbers as a string.

###Note: The numbers can be arbitrarily large and are non-negative.
# Time:  O(m * n)
# Space: O(m + n)

def MultiplyStrings(A,B):
  if A == '0' or B=='0':
    return '0'
	A = A[::-1]
	B = B[::-1]
	arr = [0 for _ in range(len(A)+len(B))]
	for i in range(len(A)):
		for j in range(len(B)):
			arr[i+j] += int(A[i])*int(B[j])
	res = []
	for i in range(len(arr)):
		carry = arr[i]//10
		digit = arr[i]%10
		if i < len(arr)-1:
			arr[i+1] += carry
		res.insert(0,str(digit))
	while res[0] == '0' and len(res)>1:
		del res[0]
	return ''.join(res)
