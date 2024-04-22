# Notes Input (idealerweise später über Django)
	# Hier irgendwie mehrere Chords? Nicht nur einen oder?
notes = input("Please give your notes in format: xyz ")
notes = notes.upper()
print(notes)

trans = []

for i in notes:
	if i == C:
		trans.append(1)

print(trans)

# Chord Calculation
	# Hier müsste ein Algorithmus hin, welcher Noten in Nummern umwandelt
	# und in Terzen auftürmt


# Chord Progression Calculation
	# Hier müsste ein Algorithmus hin, welcher Akkorde in Skalen einordnet und darüber hinaus
	# wohl auch Spezialbeziehungen erkennt (Secondary Dominant, Tritonus Substitution)

input("Please press any key to close the application.")