from timeit import default_timer as timer

# Notes Input (idealerweise später über Django)
	# Hier irgendwie mehrere Chords? Nicht nur einen oder?
notes = input("Please give your notes in format: xyz ")
notes = notes.upper()
print(notes)

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
	# Zurzeit völlig verwirrter Algorithmus
def chord_calc():
	dictlist.sort()
	for i in range(len(dictlist)):
		x = dictlist[i]
		y = dictlist[i-3]
		print("x =",x)
		print("y =",y)
		z = y - x
		print("z =",z)
		if z == 3 or z == -5 or z == 2:
			print("Terz")


chord_calc()

# Chord Progression Calculation
	# Hier müsste ein Algorithmus hin, welcher Akkorde in Skalen einordnet und darüber hinaus
	# wohl auch Spezialbeziehungen erkennt (Secondary Dominant, Tritonus Substitution)