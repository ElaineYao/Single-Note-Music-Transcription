import seaborn
import numpy, scipy, IPython.display as ipd, matplotlib.pyplot as plt
import librosa, librosa.display
from music21 import *
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
from utils import *

root = tk.Tk()

def xz():
    global answer
    answer = filedialog.askopenfilename(parent=root,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:"
                                    )

lb = Label(root,text = '')
lb.pack()
btn = Button(root,text="弹出选择文件对话框",command=xz)
btn.pack()
root.mainloop()


plt.rcParams['figure.figsize'] = (14, 5)

x, sr = librosa.load(answer)
#CQT of the signal
bins_per_octave = 36
cqt = librosa.cqt(x, sr=sr, n_bins=300, bins_per_octave=bins_per_octave)
log_cqt = librosa.amplitude_to_db(cqt)

librosa.display.specshow(log_cqt, sr=sr, x_axis='time', y_axis='cqt_note',
                         bins_per_octave=bins_per_octave)

#To identify the pitch of each note and replace each note with a pure tone of that pitch.
#Step 1 Detect Onsets
hop_length = 100
onset_env = librosa.onset.onset_strength(x, sr=sr, hop_length=hop_length)

plt.plot(onset_env)
plt.xlim(0, len(onset_env))

onset_samples = librosa.onset.onset_detect(x,
                                           sr=sr, units='samples',
                                           hop_length=hop_length,
                                           backtrack=False,
                                           pre_max=20,
                                           post_max=20,
                                           pre_avg=100,
                                           post_avg=100,
                                           delta=0.2,
                                           wait=0)

#pad the onsets with the beginning and end of the signal.
onset_boundaries = numpy.concatenate([[0], onset_samples, [len(x)]])

print (onset_boundaries)

# Convert the onsets to units of seconds:
onset_times = librosa.samples_to_time(onset_boundaries, sr=sr)

plt.vlines(onset_times, -1, 1, color='r')

# stream1 = stream.Stream()
tsThreeFour = meter.TimeSignature('4/4')
stream1 = stream.Stream()
stream1.append(tsThreeFour)
for i in range(len(onset_boundaries) - 1):
    # estimate_pitch_final(x, onset_boundaries, 1, 22050)
    stream1.append(estimate_pitch_final(x, onset_boundaries, i, sr))
# 计算tempo
tempo = librosa.beat.tempo(x, sr=sr)
# t0秒为一拍
t0 = 60 / tempo
print(tempo)

#show
beats = estimate_beats(onset_times,t0)
print (beats)
stream2 = stream.Stream()
stream1 = add_beats(stream1,stream2,beats)
#stream2 = stream1.makeMeasures()
stream2.show('musicxml')







