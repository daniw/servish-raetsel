import time

def printresult(starttime, i, j, k, l):
	print 'Time:    {}'.format(time.time() - starttime)
	print 'Numbers: {}, {}, {}, {}'.format(i, j, k, l)
	print 'Sum:     {}'.format(i + j + k + l)
	print 'Product: {}'.format(i * j * k * l)
	print 

starttime = time.time()

for i in range(774):
	for j in range(774):
		for k in range(774):
			for l in range(774):
				if i * j * k * l == 777000000:
					if (i + j + k + l) == 777:
						printresult(starttime, i, j, k, l)

print 'Time:    {}'.format(time.time() - starttime)
