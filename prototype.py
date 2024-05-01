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
def interval_calc():
	dictlist.sort()
	n1 = dictlist.index(1)
	n2 = dictlist.index(3)


chord_calc()

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
