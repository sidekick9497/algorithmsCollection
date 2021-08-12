def anagram(s1,s2):
	s1list = sorted(list(s1.lower().replace(" ","")))
	s2list = sorted(list(s2.lower().replace(" ", "")))
	print(s1list, s2list)
	if(s1list == s2list):
		return True
	return False
if anagram("hello hi", "hi Hello") == True:
	print("sucess")
else:
	print("fail")	
if anagram("hello heee", "hiee aGGEEEoge") == False:
	print("sucess")
else:
	print("fail")	


def anagramManual(s1,s2):
	s1list = sorted(s1.lower().replace(" ",""))
	s2list = sorted(s2.lower().replace(" ",""))

	count = {}
	for i in s1list:
		if(i in count):
			count[i] +=1
		else:
			count[i] = 1 
	for j in s2list:
		if(j in count):
			count[j] -=1
		else:
			count[j] = 1

	for k in count:
		if(count[k] != 0):
			return False
		return True				

if anagramManual("hello hi", "hi Hello") == True:
	print(" anagramManual sucess")
else:
	print("anagramManual fail")	
if anagramManual("hello heee", "hiee aGGEEEoge") == False:
	print("anagramManual sucess")
else:
	print("anagramManual fail")	
