import sounddevice as sd
from scipy.io.wavfile import write

fs = 8000  # Sample rate
seconds = 6 # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  
write('output.wav', fs, myrecording)