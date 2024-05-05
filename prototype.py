
# Input of musical notes
print("Chord indentifier\nStopp with X")
notes = []
note = ""
progression = []
end="y"

# Input loop to allow:
# 1. input of multiple musical notes
# 2. input of several groups of notes
while end == "y":
	while note != "X":
		note = input("Input notes (C#/Cb):").capitalize()
		if note != "X":
			notes.append(note)

	progression.append(notes)
	note = ""
	notes = []
	end = input("Continue y")

print(progression)

# Unique sharp counter
sharp = set()
flat = set()
for i_sublist in progression:
	for i in i_sublist:
		if "#" in i:
			sharp.add(i)
		if "b" in i:
			flat.add(i)

# Analytic sharp counter? Not yet coded...


# Intervall calculation method
def intervall (n1, n2):
    notdict = {
	"C": 1,
	"C#":2,
	"Db":2,
	"D": 3,
	"D#":4,
	"Eb":4,
	"E": 5,
	"E#":6,
	"Fb":5,
	"F": 6,
	"F#":7,
	"Gb":7,
	"G": 8,
	"G#":9,
	"Ab":9,
	"A":10,
	"A#":11,
	"Bb":11,
	"B":12,
	"B#":1,
	"Cb":12
}

    note1 = notdict[n1]
    note2 = notdict[n2]

    if note1 > note2:
        note2+=12

    return note2-note1


print(notes)


chord_intervalls = []
progression_intervalls = []
for i_chord in progression:
	for i in range(len(i_chord)-1):
		chord_intervalls.append(str(intervall(i_chord[i], i_chord[i+1]))) # Uses intervall function to create chord intervalls for each input group and adds the intervalls to chord_intervalls
	progression_intervalls.append(chord_intervalls) # Appends the intervall combination of each chord to the progression_intervalls list
	print(chord_intervalls)
	chord_intervalls = [] # Cleans the chord_intervalls list for the next loop iteration

print(progression_intervalls)


# convert intervalls to Chord-Name
chord_names = []
for i in range(len(progression_intervalls)):
	chord_names_dict = {("4", "3"): f"{progression[i][0]} Dur",
						("7", "9"): f"{progression[i][0]} Dur",
					("5", "4"): f"{progression[i][1]}/{progression[i][0]} Dur",
						("8", "7"): f"{progression[i][1]}/{progression[i][0]} Dur",
					("3", "5"): f"{progression[i][2]}/{progression[i][0]} Dur",
						("9", "8"): f"{progression[i][2]}/{progression[i][0]} Dur",
					# Moll
					("3", "4"): f"{progression[i][0]} Moll",
					("5", "3"): f"{progression[i][1]}/{progression[i][0]} Moll",
						("9", "7"): f"{progression[i][1]}/{progression[i][0]} Moll",
					("4", "5"): f"{progression[i][2]}/{progression[i][0]} Moll",
						("8", "9"): f"{progression[i][2]}/{progression[i][0]} Moll",
					("7", "8"): f"{progression[i][0]} Moll",
					# Dur Maj-sept
					("4", "3", "4"): f"{progression[i][0]}maj7",
					("1", "4", "3"): f"{progression[i][1]}/{progression[i][0]}maj7",
					("4", "1", "4"): f"{progression[i][2]}/{progression[i][0]}maj7",
					# Moll sept
					("3", "4", "3"): f"{progression[i][0]}m7",
				   	# Dominant 7th
				   ("4","3","3"):f"{progression[i][0]}7",
					# Minor major 7th
						("3","4","4"):f"{progression[i][0]}minmaj7",
				   # Augmented
				   ("4","4"):f"{progression[i][0]}aug",
				   # Diminished
				   ("3","3"):f"{progression[i][0]}dim"



	}
	chord_names.append(chord_names_dict[tuple(progression_intervalls[i])])

print(f"Chord names {chord_names}")

# identify chord-root-note
chord_root = []
for i in range(len(progression_intervalls)):
	# chord-root dict
	chord_root_dict = {("4", "3"): progression[i][0],
				  ("5", "4"): progression[i][1],
				  ("3", "5"): progression[i][2],
				  # Moll
				  ("3", "4"): progression[i][0],
				  ("5", "3"): progression[i][1],
				  ("4", "5"): progression[i][2],
				  # Dur Maj-sept
				  ("4", "3", "4"): progression[i][0],
				  ("1", "4", "3"): progression[i][1]
				  }

	chord_root.append(chord_root_dict[tuple(progression_intervalls[i])])

print(f"Chord root {chord_root}")


# Leading tone key estimator

sharpcircle = ["F#", "C#", "G#", "D#", "A#", "E#", "B#"]
flatcircle = ["Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]
keylist = []

def leadest():
	if len(sharp) > len(flat):
		for i in sharpcircle:
			if i in sharp:
				keylist.append(i)
	else:
		for i in flatcircle:
			if i in flat:
				keylist.append(i)

	keydict = {
		"F#": "G-Dur",
		"C#": "D-Dur",
		"G#": "A-Dur",
		"D#": "E-Dur",
		"A#": "B-Dur",
		"E#": "F#-Dur",
		"B#": "C#-Dur",
		"Bb": "F-Dur",
		"Eb": "Bb-Dur",
		"Ab": "Eb-Dur",
		"Db": "Ab-Dur",
		"Gb": "Db-Dur",
		"Cb": "Gb-Dur",
		"Fb": "Cb-Dur",
	}
	return keydict[keylist[-1]]

keyest = leadest()

if len(keylist) >= 1:
	print("Key of chord progression is: ",keyest)
else:
	print(f"Key of chord progression is: {chord_root[-1]}")

# Stufen estimator => I-IV-I
# if 1ster Akkord von 2ten Akkord 4 drüber, dann ?
# alle modis überprüfen ob der modi dem letzten akkord entspricht
