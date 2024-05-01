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
	"C#":2,
	"Db":2,
	"D": 3,
	"D#":4,
	"Eb":4,
	"E": 5,
	"E#":6,
	"Fb":6,
	"F": 6,
	"F#":7,
	"Gb":7,
	"G": 8,
	"G#":9,
	"Ab":10,
	"A":11,
	"A#":12,
	"B":12,
}

for x in notes:
	dictlist.append(notdict[x])

dend = timer()
print("Dictionary time = ", dend-dstart)

# Chord Calculation
	# Hier müsste ein Algorithmus hin, welcher Noten in Terzen auftürmt und dann den Chord bestimmt
	# Zurzeit völlig verwirrter Algorithmus
def interval_calc():
	dictlist.sort()
	for i in range(len(dictlist)):
		x = dictlist[i]
		y = dictlist[i-3]
		if x > y:
			y += 12

		z = x - y
		print(z)



interval_calc()

# Chord Progression Calculation
	# Hier müsste ein Algorithmus hin, welcher Akkorde in Skalen einordnet und darüber hinaus
	# wohl auch Spezialbeziehungen erkennt (Secondary Dominant, Tritonus Substitution)

def intervall (n1, n2):
    notes = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
    note1 = notes.index(n1)
    note2 = notes.index(n2)

    if note1 > note2:
        note2+=12

    return note2-note1

print(intervall("c", "g"))
