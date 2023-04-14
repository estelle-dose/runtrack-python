def arrondir_notes(notes):
    arrond = []
    for n in notes:
        if n >= 40:
            multiple_de_5 = ((n // 5) + 1) * 5
            if multiple_de_5 - n < 3:
                note_arrondie = multiple_de_5
            else:
                note_arrondie = n
        else:
            note_arrondie = n
        arrond.append(note_arrondie)
    return arrond

notes = [55, 82, 73, 39, 94]
print(arrondir_notes(notes))