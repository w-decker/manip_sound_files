import numpy as np
from pydub import AudioSegment
import pandas as pd
import os

# get directory
user = os.getlogin()
SOUND_DIR = f'/Users/{user}/Desktop/sounds/'

# parse sound files within directory
SOUNDS = []
for file in os.listdir(SOUND_DIR):
    file.split()
    if file.endswith('.wav') and file[0][0] != '.':
        SOUNDS.append(file)
# check that all and only sound files were added   
print(SOUNDS)

# check if 'empty.wav exists
if 'empty.wav' in SOUNDS: # will raise ValueError if 'empty.wav' is not in directory
    print(True)
else:
    print(False)

# get list of emperical sound files
SOUND_LIST = f'/Users/{user}/Box Sync/willdecker/LSU Undergrad/Honors-Thesis/github/statistical_learning_sequencing/strseq2.csv'

# name the order
ORDER = 2

# create data frame
d = pd.read_csv(SOUND_LIST)
d.describe # check that d is valid
d.columns # check that column names are valid

# combine sounds to list
sound_combn = []
EMPTY_SOUND =  AudioSegment.from_wav(SOUND_DIR + 'empty.wav')
for i in range(len(d['words'])):
    sound = AudioSegment.from_wav(SOUND_DIR + d['words'][i])
    sound_combn.append(sound)
    sound_combn.append(EMPTY_SOUND)

# concatenate list into single sound file
sound2write = sound_combn[0]
for i in range(1, len(sound_combn)):
    sound2write += sound_combn[i]

# write sound file
sound2write.export(SOUND_DIR + f'str_grandsound_{ORDER}.wav', format="wav")