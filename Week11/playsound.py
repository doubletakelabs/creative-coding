# to run, be sure to install:
# pip install sounddevice
# pip install soundfile
# pip install numpy

import sounddevice as sd
import soundfile as sf

filename = 'startup.wav' # change this to the name of the file you want to play
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing