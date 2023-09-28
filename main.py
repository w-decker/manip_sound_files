#!usr/bin/ env python

# imports 
from pydub import AudioSegment
import pandas as pd

# load in list of files 
d = pd.read_csv('files2read.csv')
d.describe
d.columns

# test with two sounds
sounds = []
for i in range(0):
    sounds[i] = AudioSegment.from_wav('sounds/' + d['sounds'][i] + '.wav')
    sounds[i + 1] = AudioSegment.from_wav('sounds/' + d['sounds'][i+1] + '.wav')
    sounds.append(sounds[i] + sounds[i+1])
