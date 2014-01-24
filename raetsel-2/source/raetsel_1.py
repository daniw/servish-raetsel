import time

def printresult(starttime, i, j, k, l):
	print time.time() - starttime
	print i
	print j
	print k
	print l
	print i + j + k + l
	print i * j * k * l
	print 

starttime = time.time()

for i in range(774):
	for j in range(774):
		for k in range(774):
			for l in range(774):
				if i * j * k * l == 777000000:
					if (i + j + k + l) == 777:
						printresult(starttime, i, j, k, l)

print time.time() - starttime