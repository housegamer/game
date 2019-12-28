def simpleSymbols(string):
	string = '=' +string+ '='
	a = list(string)
	

	for i in range(0, len(a)):
		if a(i).isalpha():
			if a[i-1]== '+' and a[i+1] != '+':
				return False
	return "True"



print(simpleSymbols(input()))

