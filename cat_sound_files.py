import numpy as np
from pydub import AudioSegment
import pandas as pd
import os

# get directory
SOUND_DIR = 'D:\decker_honors_thesis_paradigm\exposure'

# parse sound files within directory
SOUNDS = []
for file in os.listdir(SOUND_DIR):
    file.split()
    if file.endswith('.wav') and file[0][0] != '.':
        SOUNDS.append(file)
# check that all and only sound files were added   
print(SOUNDS)

# check if 'empty.wav exists
SOUNDS.index('empty.wav') # will raise ValueError if 'empty.wav' is not in directory

# get list of emperical sound files
SOUND_LIST = SOUND_DIR + '\s_2_wordlist.csv'

# name the order
ORDER = 2

# create data frame
d = pd.read_csv(SOUND_LIST)
d.describe # check that d is valid
d.columns # check that column names are valid

# combine sounds to list
sound_combn = []
EMPTY_SOUND =  AudioSegment.from_wav(SOUND_DIR + '\empty.wav')
for i in range(len(d['words'])):
    sound = AudioSegment.from_wav(SOUND_DIR + '\\' + d['words'][i] + '.wav')
    sound_combn.append(sound)
    sound_combn.append(EMPTY_SOUND)

# concatenate list into single sound file
sound2write = sound_combn[0]
for i in range(1, len(sound_combn)):
    sound2write += sound_combn[i]

# write sound file
sound2write.export(SOUND_DIR + f'\grandsound_{ORDER}.wav', format="wav")