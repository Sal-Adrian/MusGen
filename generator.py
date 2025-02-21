import sqlite3
from format import *
from random import randrange

mel = [#nte('B-4', 0.5), nte('G4', 0.5), 
nteD('D4', 2, 1), nte('B-3', 0.5), nte('C4', 0.5), 
nte('D-4',0.5), nte('C5',0.5), nte('C5',0.5), nte('C5',0.5), nte('C5',0.5), nte('B-4',0.5), nte('G4',0.5), nte('E-4',0.5),
nte('C4', 2), nte('R', 1/3), nte('G3', 1/3), nte('A-3', 1/3), nte('C4', 1/3), nte('E-4', 1/3), nte('G-4', 1/3),
nte('B-4', 0.5), nte('B-4', .5), nte('B-4', .5), nte('A-4', .5), nte('B-4', 1), nte('A-4', .5), nte('B-4', .5),
nte('G4', 1+1/3), nte('A-4', 1/3), nte('B-4', 1/3), nte('E-4', 1+1/3), nte('F4', 1/3), nte('G4', 1/3),
nte('A-4', .5), nte('C4', 1), nte('C4', .5), nte('D4', 2/3), nte('E-4', 2/3), nte('F4', 2/3), 
nte('G4', 7), nte('B-4', .5), nte('G4', .5)]

prog1 = [["EbM", 4], ["BbM", 2], ["Eb7", 2], ["AbM", 4], ["Abm", 2], ["Db7", 2], ["EbM", 2], ["C_m", 2], ["F_m", 2],
["Bb7", 2], ["G_m", 2], ["C_7", 2], ["F_m", 2], ["Bb7", 2]]

prog = progression(prog1)


db = sqlite3.connect('Chord.db')
cursor = db.cursor()

adapt = []
rest = True
rand = 0.0
total = 0.0
songLength = 32
while total < songLength:
    rand = 0.5 * (randrange(4) + 1)
    if rand + total > songLength:
        rand = songLength - total
    if rest:
        adapt.append(nte('R', rand))
    else:
        adapt.append(nte('C', rand))
    total += rand
    rest = not rest


score = stream.Score()
adaptive = stream.Part()
melody = stream.Part()
chords = stream.Part()

for elt in adapt:
    adaptive.append(elt)
for elt in mel:
    melody.append(elt)
for elt in prog:
    chords.append(elt)

score.insert([0, adaptive])
score.insert([0, melody])
score.insert([0, chords])

score.show()

db.close()