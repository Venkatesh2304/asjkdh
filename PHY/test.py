import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import sounddevice as sd

def bits_to_sound(bits, fs, fc):
    t = np.linspace(0, len(bits)/fs, int(fs*len(bits)/fs), endpoint=False)
    carrier = np.sin(2*np.pi*fc*t)
    modulated = carrier * bits
    return modulated

def sound_to_bits(modulated, fs, fc):
    t = np.linspace(0, len(modulated)/fs, int(fs*len(modulated)/fs), endpoint=False)
    carrier = np.sin(2*np.pi*fc*t)
    demodulated = modulated * carrier
    bits = np.zeros(len(demodulated))
    bits[demodulated > 0] = 1
    bits[demodulated < 0] = -1
    return bits


def play_and_record(signal, fs):
    recorded = sd.playrec(signal, fs, channels=1, blocking=True)
    return recorded

def main():
    # Input bits
    bits = np.array([1, -1, -1, 1, -1] * 100)
    fs = 8000 # Sample rate
    fc = 1000 # Carrier frequency

    # Modulation
    modulated = bits_to_sound(bits, fs, fc)
    wavfile.write('modulated.wav', fs, modulated)

    # Play and Record
    # recorded = play_and_record(modulated, fs)
    # wavfile.write('recorded.wav', fs, recorded)
    import os 
    os.system("play modulated.wav & python demod.py")
    # Demodulation
    #demodulated = sound_to_bits(modulated, fs, fc)
    #print(demodulated)

if __name__ == '__main__':
    main()
