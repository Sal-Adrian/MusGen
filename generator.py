from music21 import *

def chrd (n1, n2, n3, n4, dur):
    result = chord.Chord([n1, n2, n3, n4])
    result.duration.quarterLength = dur
    return result

def nte (n, dur):
    result = note.Note(n) if (n != "R") else note.Rest()
    result.duration.quarterLength = dur
    return result

def nteD (n, dur, dot):
    result = note.Note(n)
    result.duration.quarterLength = dur
    result.duration.dots = dot
    return result

mel = [#nte('B-4', 0.5), nte('G4', 0.5), 
nteD('D4', 2, 1), nte('B-3', 0.5), nte('C4', 0.5), 
nte('D-4',0.5), nte('C5',0.5), nte('C5',0.5), nte('C5',0.5), nte('C5',0.5), nte('B-4',0.5), nte('G4',0.5), nte('E-4',0.5),
nte('C4', 2), nte('R', 1/3), nte('G3', 1/3), nte('A-3', 1/3), nte('C4', 1/3), nte('E-4', 1/3), nte('G-4', 1/3),
nte('B-4', 0.5), nte('B-4', .5), nte('B-4', .5), nte('A-4', .5), nte('B-4', 1), nte('A-4', .5), nte('B-4', .5),
nte('G4', 1+1/3), nte('A-4', 1/3), nte('B-4', 1/3), nte('E-4', 1+1/3), nte('F4', 1/3), nte('G4', 1/3),
nte('A-4', .5), nte('C4', 1), nte('C4', .5), nte('D4', 2/3), nte('E-4', 2/3), nte('F4', 2/3), 
nte('G4', 7), nte('B-4', .5), nte('G4', .5)]

prog = [#nte('R', 1), 
chrd("E-2", "G2", "B-2", "D3", 4), chrd("F2", "A-2", "B-2", "D-3", 2), 
chrd("E-2", "G2", "B-2", "D-3", 2), chrd("G2", "A-2", "C3", "E-3", 4), chrd("G-2", "A-2", "B2", "E-3", 2), 
chrd("F2", "A-2", "B2", "D-3", 2), chrd("E-2", "G2", "B-2", "D3", 2), chrd("E-2", "G2", "B-2", "C3", 2),
chrd("F2", "A-2", "C3", "E-3", 2), chrd("F2", "A-2", "B-2", "D3", 2), chrd("F2", "G2", "B-2", "D3", 2),
chrd("G2", "B-2", "C3", "E3", 2), chrd("A-2", "C3", "E-3", "F3", 2), chrd("A-2", "B-2", "D3", "F3", 2)]

score = stream.Score()
melody = stream.Part()
chords = stream.Part()

for elt in mel:
    melody.append(elt)
for elt in prog:
    chords.append(elt)

score.insert([0, melody])
score.insert([0, chords])

score.show()