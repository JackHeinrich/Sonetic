# Reference the input CHOPs
base_note_chop = op('BaseNote')
index_chop = op('IndexFingerUp')
middle_chop = op('MiddleFingerUp')
ring_chop = op('RingFingerUp')
pinky_chop = op('PinkyUp')

# Reference the output CHOP
chord_chop = op('chord')

# Define the intervals for a seventh chord
seventh_chord_intervals = [0, 4, 7, 10]  # Root, major third, perfect fifth, minor seventh

def calculate_chord(base_note):
    # Calculate the notes of the seventh chord
    return [base_note + interval for interval in seventh_chord_intervals]

def update_chord():
    # Get the base note value
    base_note = base_note_chop[0]  # Assuming the base note is in the first channel

    # Calculate the seventh chord notes
    chord_notes = calculate_chord(base_note)

    # Update the chord CHOP if it exists
    if chord_chop is not None:
        chord_chop.par.value0 = chord_notes[0] if index_chop[0] == 1 else 0  # Root note or 0
        chord_chop.par.value1 = chord_notes[1] if middle_chop[0] == 1 else 0  # Major third or 0
        chord_chop.par.value2 = chord_notes[2] if ring_chop[0] == 1 else 0  # Perfect fifth or 0
        chord_chop.par.value3 = chord_notes[3] if pinky_chop[0] == 1 else 0  # Minor seventh or 0
    else:
        print("chord_chop is None. Please check the operator name.")

# Run the update function
def onCook(dat):
    update_chord()
