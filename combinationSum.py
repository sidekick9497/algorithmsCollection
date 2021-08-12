
def combinationSum(listarray,total):
	seen = set()
	output = set()
	for x in listarray:
		difference = total-x
		if difference not in seen:
			seen.add(x)
			print(difference)
			print(seen)
		else:
			output.add( (min(x,difference),max(x,difference)) )

	print(output)
combinationSum([1,2,3,4],4)	

