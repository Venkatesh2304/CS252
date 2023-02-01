import numpy as np
from matplotlib import pyplot as plt
import os 

SAMPLE_RATE = 44100  # Hertz
DURATION = 0.5  # Seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, int(sample_rate * duration) , endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

_, nice_tone_1  = generate_sine_wave(10000 , SAMPLE_RATE, DURATION)
_, nice_tone_2  = generate_sine_wave(2000 , SAMPLE_RATE, DURATION)


_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = np.concatenate( [nice_tone_1 , nice_tone_2]*5 )  #+ noise_tone

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

from scipy.io.wavfile import write
write("input.wav", SAMPLE_RATE, normalized_tone)
os.system("play input.wav")