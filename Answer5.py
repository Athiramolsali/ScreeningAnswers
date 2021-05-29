#Answer5
s = 'String'
def fname(s):
	with open('myfile.txt') as myfile:
     		if 'String' in myfile.read():
            		print('String is found in file')
          	else:
	    		print('Not found')