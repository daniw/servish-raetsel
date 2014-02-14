# Servish Raetsel 3

# Groesste Zahl
maxnumber = 1000

# Liste mit allen Kombinationen
a = [(i, j) for i in range(maxnumber + 1) for j in range(i,maxnumber + 1)]

"""
Sam: Ich weiss die beiden Zahlen nicht.
"""
# Zaehlvariable fuer die Anzahl vorkommender Produkte
countprod = [0]*(maxnumber*maxnumber+1)

# Zaehle Vorkommen jedes Produkts
for i in a:
	countprod[i[0]*i[1]] += 1

# Nur mehrfach vorkommende Produkte
b = [i for i in a if countprod[i[0]*i[1]] != 1]

"""
Samantha: Das wusste ich doch schon.
"""
# Liste mit Summen
checksum = [True]*(2*maxnumber+1)

# Pruefe fuer jede Summe, ob es ausschliesslich einmal vorhandene Produkte gibt
for i in a:
	if countprod[i[0]*i[1]] == 1:
		checksum[i[0]+i[1]] = False

# Nur Kombinationen bei welchen es fuer jede Summe ausschliesslich einmal vorhandene Produkte gibt
c = [i for i in b if (checksum[i[0]+i[1]] == True)]

"""
Sam: Ich kenne die Zahlen jetzt.
"""
# Zaehlvariable fuer die Anzahl vorkommender Produkte
countprod = [0]*(maxnumber*maxnumber+1)

# Zaehle Vorkommen jedes Produkts
for i in c:
	countprod[i[0]*i[1]] += 1

# Nur einfach vorkommende Produkte
d = [i for i in c if countprod[i[0]*i[1]] == 1]

"""
Samantha: Ich auch.
"""
# Zaehlvariable fuer die Anzahl vorkommender Summen
countsum = [0]*(2*maxnumber+1)

# Zaehle Vorkommen jeder Summe
for i in d:
	countsum[i[0]+i[1]] += 1

# Nur einfach vorkommende Summen
e = [i for i in d if countsum[i[0]+i[1]] == 1]

"""
Stan: Ich noch nicht. Eine Zahl kann ich vermuten. Sicher bin ich mir aber nicht.
"""
# Zaehlvariable fuer die Anzahl vorkommender Differenzen
countdiff = [0]*(maxnumber+1)

# Zaehle Vorkommen jeder Differenz
for i in e:
	countdiff[i[1]-i[0]] += 1

# Nur mindestens 3 fach vorkommende Differenzen
f = [i for i in e if countdiff[i[1]-i[0]] >= 3]

# Alle noch in Frage kommenden Differenzen
diffs = []
for i in f:
	if i[1]-i[0] not in diffs:
		diffs.append(i[1]-i[0])

# Liste mit den Werten fuer jede Differenz
fdiff = [[i] for i in diffs]
felements = [[i] for i in diffs]
for i in f:
	for j in range(len(diffs)):
		if fdiff[j][0] == i[1] - i[0]:
			fdiff[j].append(i)
			felements[j].append(i[0])
			felements[j].append(i[1])

# Nur Differenzen mit mehrfach vorhandenen Werten
diffs = []
gelements = []
for i in range(len(fdiff)):
	for j in range(1,len(fdiff[i])):
		if (fdiff[i][j][0] in felements[i][2*j+1:]):
			diffs.append(fdiff[i][0])
			gelements.append(fdiff[i][j][0])
		else:
			if (fdiff[i][j][1] in felements[i][2*j+1:]):
				diffs.append(fdiff[i][0])
				gelements.append(fdiff[i][j][1])
g = [i for i in f if i[1]-i[0] in diffs]

"""
Sam: Deine Vermutung ist falsch.
"""

h = [i for i in g if (i[1] not in gelements) & (i[0] not in gelements)]

"""
Stan: Jetzt kenne ich sie auch.
"""
print h
