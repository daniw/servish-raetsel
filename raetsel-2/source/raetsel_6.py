import time

def printresult(starttime, i, j, k, l):
	print 'Time:    {}'.format(time.time() - starttime)
	print 'Numbers: {}, {}, {}, {}'.format(i, j, k, l)
	print 'Sum:     {}'.format(i + j + k + l)
	print 'Product: {}'.format(i * j * k * l)
	print 

starttime = time.time()

aarray = [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]
barray = [[0,0,0,0]]
for tempa in range(7):
	for tempb in range(7):
		for tempc in range(7):
			for tempd in range(7):
				if tempa + tempb + tempc + tempd == 6:
					barray.append([tempa, tempb, tempc, tempd])

for b in aarray:
	for c in barray:
		for d in aarray:
			for e in barray:
				i = 37 * 7 ** b[0] * 5 ** c[0] * 3 ** d[0] * 2 ** e[0]
				j = 7 ** b[1] * 5 ** c[1] * 3 ** d[1] * 2 ** e[1]
				k = 7 ** b[2] * 5 ** c[2] * 3 ** d[2] * 2 ** e[2]
				l = 7 ** b[3] * 5 ** c[3] * 3 ** d[3] * 2 ** e[3]
				if i + j + k + l == 777:
					if i * j * k * l == 777000000:
						printresult(starttime, i, j, k, l)

print 'Time:    {}'.format(time.time() - starttime)
