import random

sum = 0
count = 0
loops = 0

while loops < 10000000000:
	loops += 1
	sum = 0
	while sum <= 1:
		sum += random.random()
		count += 1

print float(count) / loops