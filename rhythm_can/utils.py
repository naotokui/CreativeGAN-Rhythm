from .constants import *
from IPython.display import clear_output
import matplotlib.pyplot as plt
#%matplotlib inline

import random
import pretty_midi
from IPython.display import Audio
from scipy.io import wavfile
import numpy as np

from tensorboard_logger import configure, log_value

from datetime import datetime

import matplotlib
matplotlib.rcParams.update({'font.size': 14})

def start_tfboard_log(logdir_prefix = "/tmp/tf_logs/"):
    now = datetime.now()
    logdir = logdir_prefix + now.strftime("%Y%m%d-%H%M%S") 
    cmd = "tensorboard --logdir=" + logdir_prefix
    print (cmd)
    configure(logdir, flush_secs=5)

# Create Z for generator
def get_noise(batch_size, len_input):
#    noise = np.random.uniform(-1.0, 1.0, size=[batch_size, len_input])
    
    # better to use a spherical Z. according to https://github.com/soumith/ganhacks
    noise = np.random.normal(0.0, 1.0, size=[batch_size, len_input])
    return noise

def plot_drum_matrix(a):
    if a is not None:
        a = np.transpose(np.squeeze(a))
        
        fig = plt.figure(figsize=(12,5))
        ax = fig.add_subplot(111)
        ax.set_xticklabels(["1.1","1.2","1.3","1.4","2.1","2.2","2.3","2.4"] )
        ax.set_yticklabels([""]+DRUM_CLASSES)
        for i in range(8):
            plt.axvline(x=i*4-0.5,  color='0.7', linewidth=0.5)
        plt.axvline(x=15.5, color='0.5', linewidth=1.0)
        
        ax.matshow(a, cmap="YlOrRd")
        plt.xticks(np.arange(0, 32, 4.0))
        plt.show() 
        
def play_drum_matrix(mat, tempo=120.0, threshold=0.0):
    # generate audio
    audio_data = get_audio_from_drum_matrix(mat, tempo=tempo, threshold=threshold)
    display(Audio(audio_data, rate=44100))
    return audio_data

def get_audio_from_drum_matrix(mat, tempo=120., threshold=0.0):
    # ignore weak onsets
    mat[mat < threshold] = threshold    
    
    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo) # midi object
    pm_inst = pretty_midi.Instrument(0, is_drum=True) # midi instrument
    
    timestep = (60./tempo) / 4. # duration of a 16th note
    for position, timeslot in enumerate(mat):
        for inst, onset in enumerate(timeslot):
            if onset > 0.:
                note_number = DRUM_MIDI_MAP[inst]
                velocity = int(onset * 127.)
                start = timestep * position
                end = timestep * (position + 0.5)
                
                # create a midi note
                note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)
                pm_inst.notes.append(note)
    pm.instruments.append(pm_inst)

    # midi -> audio
    audio_data = pm.fluidsynth()
    return audio_data



