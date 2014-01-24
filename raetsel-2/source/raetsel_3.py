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

for i in range(777/4):
	for j in range(777/3):
		for k in range(777/2):
			if (i * j * k * (777 - i - j - k)) == 777000000:
				for l in range(774):
					if i + j + k + l == 777:
						if i * j * k * l == 777000000:
							printresult(starttime, i, j, k, l)

print time.time() - starttime