import sounddevice as sd
from scipy.io.wavfile import write

fs = 8000  # Sample rate
# 11 sec for 25 bits * 12 rep 
seconds =  20 # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  
write('output.wav', fs, myrecording)
print(" recording done ")