#import io

with open('c:/Users/admin/Desktop/test_file.txt','r') as rf:
	with open('c:/Users/admin/Desktop/test_copy_file.txt','w') as wf:
		for line in rf:
			wf.write(line)
	
#a = open('c:/Users/admin/Desktop/test_file.txt','r')

#print(a.mode)

#a.close()