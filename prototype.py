print("Chord indentifier\nStopp with X")
notes = []
note = ""
progression = []
end="y"
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

# Sharp counter
sharp = set()
for sublist in progression:
    for i in sublist:
        if "#" in i:
            sharp.add(i)


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
for chord in progression:
	for i in range(len(chord)-1):
		chord_intervalls.append(str(intervall(chord[i], chord[i+1])))
	progression_intervalls.append(chord_intervalls)
	print(chord_intervalls)
	chord_intervalls = []

print(progression_intervalls)



for i in range(len(progression_intervalls)):
	chord_names = {("4", "3"): f"{progression[i][0]} Dur",
					("5", "4"): f"{progression[i][1]}/{progression[i][0]} Dur",
					("3", "5"): f"{progression[i][2]}/{progression[i][0]} Dur",
					# Moll
					("3", "4"): f"{progression[i][0]} Moll",
					("5", "3"): f"{progression[i][1]}/{progression[i][0]} Moll",
					("4", "5"): f"{progression[i][2]}/{progression[i][0]} Moll",
					# Dur sept
					("4", "3", "4"): f"{progression[i][0]}maj7",
					("1", "4", "3"): f"{progression[i][1]}/{progression[i][0]}maj7"
	}


	print(chord_names[tuple(progression_intervalls[i])])
