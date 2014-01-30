import time

def printresult(starttime, i, j, k, l):
	print 'Time:    {}'.format(time.time() - starttime)
	print 'Numbers: {}, {}, {}, {}'.format(i, j, k, l)
	print 'Sum:     {}'.format(i + j + k + l)
	print 'Product: {}'.format(i * j * k * l)
	print 

starttime = time.time()

for i in range(777/4):
	for j in range(777/3):
		for k in range(777/2):
			if (i * j * k * (777 - i - j - k)) == 777000000:
				l = 777 - i - j - k
				if i + j + k + l == 777:
					if i * j * k * l == 777000000:
						printresult(starttime, i, j, k, l)

print 'Time:    {}'.format(time.time() - starttime)
