# Notes Input (idealerweise später über Django)
	# Hier irgendwie mehrere Chords? Nicht nur einen oder?
notes = input("Please give your notes in format: xyz ")
notes = notes.upper()
print(notes)

# Listenlösung
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
	if i == "H":
		trans.append(7)

print(trans)

# Dictionary Lösung
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
	print(notdict[x])



# Chord Calculation
	# Hier müsste ein Algorithmus hin, welcher Noten in Nummern umwandelt
	# und in Terzen auftürmt


# Chord Progression Calculation
	# Hier müsste ein Algorithmus hin, welcher Akkorde in Skalen einordnet und darüber hinaus
	# wohl auch Spezialbeziehungen erkennt (Secondary Dominant, Tritonus Substitution)