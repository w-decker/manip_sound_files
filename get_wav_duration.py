########## getting duration of sounds ##########

# imports
import wave
import contextlib
import os
import pandas as pd


user = os.path.expanduser('~')
sound_dir = str(f'{user}/Desktop/sounds/') # set directory where sound (.wav) files are located
sound_files = os.listdir(sound_dir)

#remove .DS_store
sound_files.remove('.DS_Store') # remove 
print(sound_files)

# loop through files and get their lengths
sounds = pd.DataFrame(columns=['name', 'duration'])
sounds['name'] = sound_files
sound_lens = []

for i in range(len(sound_files)):
    with contextlib.closing(wave.open(sound_files[i],'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        sound_lens.append(round(duration,4))

sounds['duration'] = sound_lens

# save 
sounds.write_csv("sounds.csv")