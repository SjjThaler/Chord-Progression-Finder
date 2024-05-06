
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

print(f"Progression {progression}")

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
						("4", "7", "8"): f"{progression[i][0]}maj7",
						("7", "4", "5"): f"{progression[i][0]}maj7",
						("7", "9", "7"): f"{progression[i][0]}maj7",
						("11", "5", "3"): f"{progression[i][0]}maj7",
						("11", "8", "9"): f"{progression[i][0]}maj7",
						("1", "4", "3"): f"{progression[i][1]}/{progression[i][0]}maj7",
						("4", "1", "4"): f"{progression[i][2]}/{progression[i][0]}maj7",
						#("3", "4", "1"): f"{progression[i][3]}/{progression[i][0]}maj7",
						# Moll sept
						("3", "4", "3"): f"{progression[i][0]}m7",
						# Dominant 7th
						("4", "3", "3"): f"{progression[i][0]}7",
						# Minor major 7th
						("3", "4", "4"): f"{progression[i][0]}minmaj7",
						# Augmented
						("4", "4"): f"{progression[i][0]}aug",
						# Diminished
						("3", "3"): f"{progression[i][0]}dim"

						}
	if len(progression_intervalls[i]) >= 3:
		chord_names_dict.update({("3", "4", "1"): f"{progression[i][3]}/{progression[i][0]}maj7"})
	chord_names.append(chord_names_dict[tuple(progression_intervalls[i])])


print(f"Chord names {chord_names}")

# identify chord-root-note
chord_root = []
for i in range(len(progression_intervalls)):
	chord_root_dict = {	("4", "3"): f"{progression[i][0]}",
					   	("7", "9"): f"{progression[i][0]}",
						("5", "4"): f"{progression[i][1]}",
						("8", "7"): f"{progression[i][1]}",
						("3", "5"): f"{progression[i][2]}",
						("9", "8"): f"{progression[i][2]}",
						# Moll
						("3", "4"): f"{progression[i][0]}",
						("5", "3"): f"{progression[i][1]}",
						("9", "7"): f"{progression[i][1]}",
						("4", "5"): f"{progression[i][2]}",
						("8", "9"): f"{progression[i][2]}",
						("7", "8"): f"{progression[i][0]}",
						# Dur Maj-sept
						("4", "3", "4"): f"{progression[i][0]}",
						("4", "7", "8"): f"{progression[i][0]}",
						("7", "4", "5"): f"{progression[i][0]}",
						("7", "9", "7"): f"{progression[i][0]}",
						("11", "5", "3"): f"{progression[i][0]}",
						("11", "8", "9"): f"{progression[i][0]}",
						("1", "4", "3"): f"{progression[i][1]}",
						("4", "1", "4"): f"{progression[i][2]}",
						#("3", "4", "1"): f"{progression[i][3]}",
						# Moll sept
						("3", "4", "3"): f"{progression[i][0]}",
						# Dominant 7th
						("4","3","3"):f"{progression[i][0]}",
						# Minor major 7th
						("3","4","4"):f"{progression[i][0]}",
						# Augmented
						("4","4"):f"{progression[i][0]}",
						# Diminished
						("3","3"):f"{progression[i][0]}"



	}
	if len(progression_intervalls[i]) >= 3:
		chord_root_dict.update({("3", "4", "1"): f"{progression[i][3]}"})
	chord_root.append(chord_root_dict[tuple(progression_intervalls[i])])

print(f"Chord root {chord_root}")

# scale estimator
all_notes = [item for sublist in progression for item in sublist] # fasst alle Noten der Akkorde in eine Liste
print(all_notes)
scale = []
all_scale = []
for i_root in chord_root: # i_root ist die root-note der eingegebenen Akkorde
	for i_all in all_notes: # i_all sind alle gegebenen Noten
		scale.append(str(intervall(i_root, i_all))) # fügt das intervall von einer root-note zu allen gegebenen hinzu
	uni_scale = list(map(int, list(set(scale)))) # nachdem alle intervall in scale = [] gespeichert wurden, filtert es mit einem set alle mehrfachen raus, wandelt alle intervalle mit map in int um, um sie zu ordnen
	uni_scale.sort() # hier wird geordnet
	all_scale.append(list(map(str, uni_scale))) # hier wird wieder alles in str umgewandelt und die skala(aus intervallen) einer liste zugefügt
	scale = [] # reset... man muss anmerken dass das obige ordnen irrelevant für den nächsten schritt ist und keinen negativen einfluss auf das outcome hat :)

print(all_scale)
scale_dict = {	("0", "2", "4", "5", "7", "9", "11"): "Ionisch",
				("0", "2", "3", "5", "7", "8", "10"): "Aeolisch",
				("0", "2", "3", "5", "7", "8", "11"): "Harmonisch-Moll",
				("0", "2", "4", "5", "7", "9", "10"): "Mixolydisch",
				("0", "2", "3", "6", "7", "8", "11"): "Zigeuner-Moll",
				("0", "2", "4", "6", "7", "9", "11"): "Lydisch"
}
scale_name = []
#scale_root_index = -1 # der index damit chord root notes mit der scale verbunden werden kann ...
for i_index, i_scale in enumerate(all_scale): # ... hier könnte man enumerate() hernehmen - for x, y in enumerate(all_scale):
	#scale_root_index += 1
	for key, value in scale_dict.items(): # hier wird durch das obige scale dict mit .items() mit den jeweiligen key und value iteriert
		if all(i in key for i in i_scale): # all() gibt True, wenn alle booleans darin True sind. i sind hier die ermittelten intervalle des scale estimators. dann wird überprüft ob i in dem key (der intervall-struktur der modis) is und gibt einen bool aus.
			scale_name.append([chord_root[i_index], value]) # wenn alle gegebenen intervalle in einem modus auch vorkommen ...



print(scale_name)

# scale struktur
scale_structure = {
				"Ionisch": ("1", "2", "3", "4", "5", "6", "7"),
				"Aeolisch": ("1", "2", "3b", "4", "5", "6b", "7b"),
				"Harmonisch-Moll": ("1", "2", "3b", "4", "5", "6b", "7"),
				"Mixolydisch": ("1", "2", "3", "4", "5", "6", "7b"),
				"Zigeuner-Moll": ("1", "2", "3b", "4#", "5", "6b", "7"),
				"Lydisch": ("1", "2", "3", "4#", "5", "6", "7")
}

# root to scale_structure
root_scale_structure = [[i_root, scale_structure[scale]]for i_root, scale in scale_name]
print(root_scale_structure)



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

if len(sharp) >= 1 or len(flat) >= 1:
	keylist = leadest()

print(keylist)

if len(keylist) >= 1:
	if (keylist== chord_root[-1]):
		print(f"Leadtone and chord root indicate the key of: {chord_root[-1]}") # Das funktioniert noch nicht, weil chord root immer nur eine einzelne Note ist
	else:
		print(f"Chord root indicates key of: {chord_root[-1]}")
else:
	print(f"Chord root indicates key of: {chord_root[-1]}")


# Stufen estimator => I-IV-I
# if 1ster Akkord von 2ten Akkord 4 drüber, dann ?
# alle modis überprüfen ob der modi dem letzten akkord entspricht
