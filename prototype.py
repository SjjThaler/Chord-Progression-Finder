from timeit import default_timer as timer

# Notes Input (idealerweise später über Django)
	# Hier irgendwie mehrere Chords? Nicht nur einen oder?
n1 = input("Gib N1 ein: ")
n2 = input("Gib N2 ein: ")

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

    note1 = notdict[n1]
    note2 = notdict[n2]

    if note1 > note2:
        note2+=12

    return note2-note1

print(intervall("c", "g"))
