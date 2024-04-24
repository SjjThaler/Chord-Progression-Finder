from timeit import default_timer as timer

# Notes Input (idealerweise später über Django)
	# Hier irgendwie mehrere Chords? Nicht nur einen oder?
notes = input("Please give your notes in format: xyz ")
notes = notes.upper()
print(notes)

# Listenlösung
lstart = timer()

trans = []

for i in notes:
	if i == "C":
		trans.append(1)
	if i == "D":
		trans.append(2)
	if i == "E":
		trans.append(3)
	if i == "F":
		trans.append(4)
	if i == "G":
		trans.append(5)
	if i == "A":
		trans.append(6)
	if i == "B":
		trans.append(7)

print(trans)
lend = timer()
print("Listentime = ", lend-lstart)

# Dictionary Lösung
dstart = timer()

dictlist = []
notdict = {
	"C": 1,
	"D": 2,
	"E": 3,
	"F": 4,
	"G": 5,
	"A": 6,
	"B": 7,
}

for x in notes:
	dictlist.append(notdict[x])

dend = timer()
print("Dictionary time = ", dend-dstart)

# Chord Calculation
	# Hier müsste ein Algorithmus hin, welcher Noten in Terzen auftürmt und dann den Chord bestimmt

def chord_calc():
	dictlist.sort()
	for i in dictlist:
		x = dictlist[i]
		y = dictlist[i+3]
		print("x =",x)
		print("y =",y)
		if x - y == 3:
			print("6,3")


chord_calc()

# Chord Progression Calculation
	# Hier müsste ein Algorithmus hin, welcher Akkorde in Skalen einordnet und darüber hinaus
	# wohl auch Spezialbeziehungen erkennt (Secondary Dominant, Tritonus Substitution)