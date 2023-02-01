from scipy.fft import fft, fftfreq
from scipy.io.wavfile import read
from matplotlib import pyplot as plt
import numpy as np

import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 44100  # Hertz0
DURATION = 5  # Seconds

# fs = SAMPLE_RATE  # Sample rate
# seconds = DURATION  # Duration of recording
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# sd.wait()  
# write('output.wav', fs, myrecording)
#DURATION =  5

sample_rate , normalized_tone =  read("input.wav")
print( normalized_tone.shape )
x = np.array_split(normalized_tone,10)

#Number of samples in normalized_tone
for i in x : 
    N = SAMPLE_RATE
    yf = fft(i)
    xf = fftfreq( N , 1 / SAMPLE_RATE)
    yf = np.abs(yf)
    plt.plot(xf, yf)
    plt.show()
    
    #for j in range(len(yf)) : 
    #  if yf[j] >= 1000 : 
    #    print(xf[j])
   