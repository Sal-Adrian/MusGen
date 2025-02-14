from music21 import *

def nte (n, dur):
    result = note.Note(n) if (n != "R") else note.Rest()
    result.duration.quarterLength = dur
    return result

def nteD (n, dur, dot):
    result = note.Note(n)
    result.duration.quarterLength = dur
    result.duration.dots = dot
    return result

melody = []


play = stream.Stream()
for i in melody:
    play.append(i)


play.show('midi')

# play.show()