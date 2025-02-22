from music21 import *

TONES = ["C", "D-", "D", "E-", "E", "F", "G-", "G", "A-", "A", "B-", "B"]

def singleChord (chrd, dur, octve, playNotes):
    if chrd == "R":
        return nte(elt[0], elt[1])

    tone = TONES.index(chrd[0])
    if chrd[1] == 'b':
        tone -= 1
    n1 = TONES[tone] + octve
    
    type = chrd[2]
    tone += 3
    if type == 'M' or type == '7':
        tone += 1
    tone %= 12
    n2 = TONES[tone] + octve

    tone += 3
    if type == 'm':
        tone += 1
    tone %= 12
    n3 = TONES[tone] + octve

    tone += 3
    if type == 'M' or type == '0':
        tone += 1
    tone %= 12
    n4 = TONES[tone] + octve

    ntes = [n1, n2, n3, n4]
    playChrd = []
    for i in range(4):
        if playNotes[i] is not None:
            playChrd.append(ntes[i])
    result = chord.Chord(playChrd)
    result.duration.quarterLength = dur
    return result

def progression (chords):
    prog = []
    for elt in chords:
        prog.append(singleChord(elt[0], elt[1], '2', [1,1,1,1]))
    return prog

def nte (n, dur):
    result = note.Note(n) if (n != "R") else note.Rest()
    result.duration.quarterLength = dur
    return result

def nteD (n, dur, dot):
    result = note.Note(n)
    result.duration.quarterLength = dur
    result.duration.dots = dot
    return result