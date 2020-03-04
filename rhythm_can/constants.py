
MIDI_DRUM_MAP = {
     36: 0, # bass drum 1
     38: 1, # acoustic snare
     40: 1, # electric snare
     42: 2, # closed hihat
     44: 3, # pedal hihat
     46: 3, # open hihat
     41: 4, # low floor tom -> Tom low
     45: 4, # low tom
     47: 4, # low-mid tom -> Tom low
     43: 5, # high floor tom -> Tom high
     48: 5, # high-mid tom -> Tom high
     49: 6, # crash symbal 1
     51: 6, # ride  cymbal 1
     57: 6, # crash symbal 2
     39: 7, # hand clap
     56: 7, # cowbell -> clap
     53: 7, # ride bell ->  clap
     37: 8, # side stick
}

DRUM_CLASSES = [
   'Kick',             # 0
   'Snare',            # 1
   'Hi-hat closed',    # 2
   'Hi-hat open',      # 3
   'Low Tom',          # 4
   'High Tom',         # 5
   'Cymbal',           # 6 
   'Clap/Cowbell',     # 7
   'Rim',              # 8
]

DRUM_MIDI_MAP = [ # pianoroll to MIDI - reverse
    36, # 0 Kick / Bass Drum 1
    40, # 1 Snare / Electric Snare
    42, # 2 Hihat Closed
    46, # 3 Hihat Open
    47, # 4 Low Tom
    66, # 5 High Tom
    51, # 6 Cymbal
    63, # 7 Clap / Cowbell
    39  # 8 Rim / Side Stick
]
    
       
resolution  = 4 # separate quater into 4  = 16 notes per bar

nb_bars = 2 

len_seq = resolution * 4 * nb_bars # length of drumloops in training data - 2 bars
    
nb_notes = len(DRUM_CLASSES) # number of possible MIDI notes  - max_drum_note - min_drum_note


len_input = 100  # dimentionality of random input vector z to the generator network