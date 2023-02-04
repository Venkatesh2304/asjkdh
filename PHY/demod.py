import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import sounddevice as sd

def sound_to_bits(modulated, fs, fc):
    t = np.linspace(0, len(modulated)/fs, int(fs*len(modulated)/fs), endpoint=False)
    carrier = np.sin(2*np.pi*fc*t)
    demodulated = modulated * carrier
    bits = np.zeros(len(demodulated))
    bits[demodulated > 0] = 1
    bits[demodulated < 0] = -1
    return bits

fs = 44100  # Sample rate
seconds = 1 # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
demodulated = sound_to_bits(myrecording, 44100, 2000)
print( demodulated )
