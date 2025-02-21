import sqlite3
from format import *
from random import randrange

TONES = ["C", "D-", "D", "E-", "E", "F", "G-", "G", "A-", "A", "B-", "B"]
INTERVALS = ["b.II", "II", "b.III", "III", "IV", "b.V", "V", "b.VI", "VI", "b.VII", "VII" ]

def main():
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
    rand, total, progTotal = 0.0, 0.0, prog1[0][1]
    progIndex = 0
    songLength = 32
    while total < songLength:
        if progTotal <= total:
            progIndex += 1
            progTotal += prog1[progIndex][1]
        
        rand = 0.5 * (randrange(4) + 1)
        if rand + total > songLength:
            rand = songLength - total
        if rest:
            adapt.append(nte('R', rand))
        else:
            type = prog1[progIndex][0]
            # print(type)
            tone = TONES.index(type[0])
            if type[1] == 'b':
                tone -= 1

            if type[2] == 'M':
                type = "M7"
            elif type[2] == '7':
                type = "7"
            elif type[2] == 'm':
                type = "m7"
            elif type[2] == '0':
                type = "07"
            else:
                type = "o7"
            
            sql = '''SELECT Next, Type FROM ChordProg 
            WHERE Curr = '%s' AND DIST = 1 AND InCurrScale_1 = 1 AND 
            InCurrScale_2 = 1 AND InCurrScale_3 = 1 AND InCurrScale_4 = 1
            ORDER BY RANDOM() LIMIT 1'''
            nextChrd = cursor.execute(sql % type)
            nextChrd = nextChrd.fetchone()
            if not nextChrd:
                sql = '''SELECT Next, Type FROM ChordProg 
                WHERE Curr = '%s' AND DIST = 2 AND InCurrScale_1 = 1 AND 
                InCurrScale_2 = 1 AND InCurrScale_3 = 1 AND InCurrScale_4 = 1
                ORDER BY RANDOM() LIMIT 1'''
                nextChrd = cursor.execute(sql % type)
                nextChrd = nextChrd.fetchone()
            if len(nextChrd[0]) < 6:
                tone += INTERVALS.index(nextChrd[0]) + 1
            else:
                if nextChrd[0][:2] == "I/":
                    tone = 0
                elif nextChrd[0][0] == "b":
                    tone = 1
                else:
                    tone = 2
            tone %= 12
            # print(f"{str(progIndex)}  : {nextChrd}     : {tone}")
            nextChrdStr = TONES[tone]
            if len(nextChrdStr) < 2:
                nextChrdStr += '_'
            nextChrdStr += nextChrd[1][0]
            # print(nextChrdStr)
            adapt.append(singleChord([nextChrdStr, rand]))
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

if __name__=="__main__":
    main()