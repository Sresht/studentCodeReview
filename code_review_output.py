
'''
This does a Caesar Cipher of the input list. 
In other words, every element in lst is moved forwards by k elements.
'''

def caesarCipher(lst, k):
	out = []
	for i in xrange(0, len(lst)):
		out.append(lst[( i + k ) % len(lst)])
	return out


studentsList = ["student", "names", "here"]

numRequiredReviews = 3
numOptionalReviews = 8

# hard-coded cipher transformations
cipherTransformationKeys = [3, 12, 20, 33, 42, 57, 81, 92]
studentsMap = {}
	
ciphers = [caesarCipher(studentsList, 3), caesarCipher(studentsList, 12), caesarCipher(studentsList, 20), caesarCipher(studentsList, 33), caesarCipher(studentsList, 42), caesarCipher(studentsList, 57), caesarCipher(studentsList, 81), caesarCipher(studentsList, 92)]

for i in xrange(0, len(studentsList)):
	codeReviewRequiredStudents = []
	codeReviewExtraCreditStudents = []

	for j in xrange(0, numRequiredReviews):
		codeReviewRequiredStudents.append(ciphers[j][i])

	for j in xrange(numRequiredReviews, numOptionalReviews):
		codeReviewExtraCreditStudents.append(ciphers[j][i])

	studentsMap[studentsList[i]] = (codeReviewRequiredStudents, codeReviewExtraCreditStudents)

for student in sorted(studentsMap.keys()):
	print student + ", you are required to review the following people for full credit on the code review: " + str(studentsMap[student][0])
	print student + ", you are required to review the following additional people for extra credit on the code review: " + str(studentsMap[student][1]) + "\n"
