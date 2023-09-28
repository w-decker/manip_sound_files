#!usr/bin/ env python

# imports 
from pydub import AudioSegment
import pandas as pd
import numpy as np

# load in list of files 
d = pd.read_csv('files2read.csv')
d.describe
d.columns

# test with two sounds
sounds1 = AudioSegment.from_wav('sounds/' + d['sounds'][1] + '.wav')
sounds2 = AudioSegment.from_wav('sounds/' + d['sounds'][2] + '.wav')
sounds = sounds1 + sounds2
sounds.export("cat_sound_test.wav", format='wav')

# fullscale
sounds = []
for i in range(len(d['sounds'])):
    sound = AudioSegment.from_wav('sounds/' + d['sounds'][i] + '.wav')
    sounds.append(sound)

for i in range(1, len(sounds)):
    sound2write = sounds[0] + sounds[i]
    
sound2write.export('grandsound.wav', format="wav")


