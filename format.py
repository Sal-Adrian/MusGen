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