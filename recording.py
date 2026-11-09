import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100 #sampling frequency
duration = 5




print("Recording Started")

audio = sd.rec(int(fs * duration),samplerate=fs,channels = 1)

sd.wait()

print("Recording Stopped")
print(audio)

write("./mini-wispr/output.wav",fs,audio)


