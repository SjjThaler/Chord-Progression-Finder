print("Chord indentifier\nStopp with X")
notes = []
note = ""
while note != "X":
	note = input("Input notes (C#/Cb):").capitalize()
	notes.append(note)
notes.remove("X")




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
for i in range(len(notes)-1):
	chord_intervalls.append(str(intervall(notes[i], notes[i+1])))
print(chord_intervalls)

chord_names = {("4", "3"): f"{notes[0]} Dur",
			   ("5", "4"): f"{notes[1]}/{notes[0]} Dur",
			   ("3", "5"): f"{notes[2]}/{notes[0]} Dur",
			   #Moll
			   ("3", "5"): f"{notes[2]}/{notes[0]} Dur",

}

print(chord_names[tuple(chord_intervalls)])
