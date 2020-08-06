import librosa, librosa.display
from music21 import *

# Estimate Pitch
def estimate_pitch(segment, sr, fmin=50.0, fmax=2000.0):
    # Compute autocorrelation of input segment.
    r = librosa.autocorrelate(segment)

    # Define lower and upper limits for the autocorrelation argmax.
    i_min = sr / fmax
    i_max = sr / fmin
    r[:int(i_min)] = 0
    r[int(i_max):] = 0

    # Find the location of the maximum autocorrelation.
    i = r.argmax()
    f0 = float(sr) / i
    return f0

# Step3 justify the range
def estimate_range(f):
    if f>=32.7 and f<65.4:
        r=1
    elif f>=65.4 and f< 130.8:
        r=2
    elif f>=130.8 and f<261.6:
        r=3
    elif f>=261.6 and f<523.26:
        r=4
    elif f>=523.26 and f<1046.5:
        r=5
    elif f>=1046.5 and f<2093:
        r=6
    elif f>=2093 and f<4186:
        r=7
    else:
        r=0
        print ('Out of range')
    return r

b0 = note.Note('b0');
c1 = note.Note('c1');
cf1 = note.Note('c#1');
d1 = note.Note('d1');
df1 = note.Note('d#1');
e1 = note.Note('e1');
f1 = note.Note('f1');
ff1 = note.Note('f#1');
g1 = note.Note('g1');
gf1 = note.Note('g#1');
a1 = note.Note('a1');
af1 = note.Note('a#1');
b1 = note.Note('b1');
c2 = note.Note('c2');

# Step4 determine the exact tone
def estimate_tone1(f):
    s = 'c1'
    if f>(b0.pitch.frequency+c1.pitch.frequency )/1 and f<(c1.pitch.frequency+cf1.pitch.frequency )/1:
        s = 'c1'
    elif f>(c1.pitch.frequency+cf1.pitch.frequency )/1 and f<(cf1.pitch.frequency+d1.pitch.frequency )/1:
        s = 'cf1'
    elif f>(cf1.pitch.frequency+d1.pitch.frequency )/1 and f<(d1.pitch.frequency+df1.pitch.frequency )/1:
        s = 'd1'
    elif f>(d1.pitch.frequency+df1.pitch.frequency )/1 and f<(df1.pitch.frequency+e1.pitch.frequency )/1:
        s = 'd#1'
    elif f>(df1.pitch.frequency+e1.pitch.frequency )/1 and f<(e1.pitch.frequency+f1.pitch.frequency )/1:
        s = 'e1'
    elif f>(e1.pitch.frequency+f1.pitch.frequency )/1 and f<(f1.pitch.frequency+ff1.pitch.frequency )/1:
        s = 'f1'
    elif f>(f1.pitch.frequency+ff1.pitch.frequency )/1 and f<(ff1.pitch.frequency+g1.pitch.frequency )/1:
        s = 'f#1'
    elif f>(ff1.pitch.frequency+g1.pitch.frequency )/1 and f<(g1.pitch.frequency+gf1.pitch.frequency )/1:
        s = 'g1'
    elif f>(g1.pitch.frequency+gf1.pitch.frequency )/1 and f<(gf1.pitch.frequency+a1.pitch.frequency )/1:
        s = 'g#1'
    elif f>(gf1.pitch.frequency+a1.pitch.frequency )/1 and f<(a1.pitch.frequency+af1.pitch.frequency )/1:
        s = 'a1'
    elif f>(a1.pitch.frequency+af1.pitch.frequency )/1 and f<(af1.pitch.frequency+b1.pitch.frequency )/1:
        s = 'a#1'
    elif f>(af1.pitch.frequency+b1.pitch.frequency )/1 and f<(b1.pitch.frequency+c2.pitch.frequency )/1:
        s = 'b1'
    return s

b1 = note.Note('b1');
c2 = note.Note('c2');
cf2 = note.Note('c#2');
d2 = note.Note('d2');
df2 = note.Note('d#2');
e2 = note.Note('e2');
f2 = note.Note('f2');
ff2 = note.Note('f#2');
g2 = note.Note('g2');
gf2 = note.Note('g#2');
a2 = note.Note('a2');
af2 = note.Note('a#2');
b2 = note.Note('b2');
c3 = note.Note('c3');


def estimate_tone2(f):
    s = 'c2'
    if f>(b1.pitch.frequency+c2.pitch.frequency )/2 and f<(c2.pitch.frequency+cf2.pitch.frequency )/2:
        s = 'c2'
    elif f>(c2.pitch.frequency+cf2.pitch.frequency )/2 and f<(cf2.pitch.frequency+d2.pitch.frequency )/2:
        s = 'c#2'
    elif f>(cf2.pitch.frequency+d2.pitch.frequency )/2 and f<(d2.pitch.frequency+df2.pitch.frequency )/2:
        s = 'd2'
    elif f>(d2.pitch.frequency+df2.pitch.frequency )/2 and f<(df2.pitch.frequency+e2.pitch.frequency )/2:
        s = 'd#2'
    elif f>(df2.pitch.frequency+e2.pitch.frequency )/2 and f<(e2.pitch.frequency+f2.pitch.frequency )/2:
        s = 'e2'
    elif f>(e2.pitch.frequency+f2.pitch.frequency )/2 and f<(f2.pitch.frequency+ff2.pitch.frequency )/2:
        s = 'f2'
    elif f>(f2.pitch.frequency+ff2.pitch.frequency )/2 and f<(ff2.pitch.frequency+g2.pitch.frequency )/2:
        s = 'f#2'
    elif f>(ff2.pitch.frequency+g2.pitch.frequency )/2 and f<(g2.pitch.frequency+gf2.pitch.frequency )/2:
        s = 'g2'
    elif f>(g2.pitch.frequency+gf2.pitch.frequency )/2 and f<(gf2.pitch.frequency+a2.pitch.frequency )/2:
        s = 'g#2'
    elif f>(gf2.pitch.frequency+a2.pitch.frequency )/2 and f<(a2.pitch.frequency+af2.pitch.frequency )/2:
        s = 'a2'
    elif f>(a2.pitch.frequency+af2.pitch.frequency )/2 and f<(af2.pitch.frequency+b2.pitch.frequency )/2:
        s = 'a#2'
    elif f>(af2.pitch.frequency+b2.pitch.frequency )/2 and f<(b2.pitch.frequency+c3.pitch.frequency )/2:
        s = 'b2'
    return s

b2 = note.Note('b2');
c3 = note.Note('c3');
d_3 = note.Note('d-3');
d3 = note.Note('d3');
df3 = note.Note('d#3');
e3 = note.Note('e3');
f3 = note.Note('f3');
ff3 = note.Note('f#3');
g3 = note.Note('g3');
gf3 = note.Note('g#3');
a3 = note.Note('a3');
af3 = note.Note('a#3');
b3 = note.Note('b3');
c4 = note.Note('c4');


def estimate_tone3(f):
    s = 'c3'
    if f>(b2.pitch.frequency+c3.pitch.frequency )/2 and f<(c3.pitch.frequency+d_3.pitch.frequency )/2:
        s = 'c3'
    elif f>(c3.pitch.frequency+d_3.pitch.frequency )/2 and f<(d_3.pitch.frequency+d3.pitch.frequency )/2:
        s = 'd-3'
    elif f>(d_3.pitch.frequency+d3.pitch.frequency )/2 and f<(d3.pitch.frequency+df3.pitch.frequency )/2:
        s = 'd3'
    elif f>(d3.pitch.frequency+df3.pitch.frequency )/2 and f<(df3.pitch.frequency+e3.pitch.frequency )/2:
        s = 'd#3'
    elif f>(df3.pitch.frequency+e3.pitch.frequency )/2 and f<(e3.pitch.frequency+f3.pitch.frequency )/2:
        s = 'e3'
    elif f>(e3.pitch.frequency+f3.pitch.frequency )/2 and f<(f3.pitch.frequency+ff3.pitch.frequency )/2:
        s = 'f3'
    elif f>(f3.pitch.frequency+ff3.pitch.frequency )/2 and f<(ff3.pitch.frequency+g3.pitch.frequency )/2:
        s = 'f#3'
    elif f>(ff3.pitch.frequency+g3.pitch.frequency )/2 and f<(g3.pitch.frequency+gf3.pitch.frequency )/2:
        s = 'g3'
    elif f>(g3.pitch.frequency+gf3.pitch.frequency )/2 and f<(gf3.pitch.frequency+a3.pitch.frequency )/2:
        s = 'g#3'
    elif f>(gf3.pitch.frequency+a3.pitch.frequency )/2 and f<(a3.pitch.frequency+af3.pitch.frequency )/2:
        s = 'a3'
    elif f>(a3.pitch.frequency+af3.pitch.frequency )/2 and f<(af3.pitch.frequency+b3.pitch.frequency )/2:
        s = 'a#3'
    elif f>(af3.pitch.frequency+b3.pitch.frequency )/2 and f<(b3.pitch.frequency+c4.pitch.frequency )/2:
        s = 'b3'
    return s

b3 = note.Note('b3');
c4 = note.Note('c4');
d_4 = note.Note('d-4');
d4 = note.Note('d4');
df4 = note.Note('d#4');
e4 = note.Note('e4');
f4 = note.Note('f4');
ff4 = note.Note('f#4');
g4 = note.Note('g4');
gf4 = note.Note('g#4');
a4 = note.Note('a4');
af4 = note.Note('a#4');
b4 = note.Note('b4');
c5 = note.Note('c5');


def estimate_tone4(f):
    s = 'c4'
    if f>(b3.pitch.frequency+c4.pitch.frequency )/2 and f<(c4.pitch.frequency+d_4.pitch.frequency )/2:
        s = 'c4'
    elif f>(c4.pitch.frequency+d_4.pitch.frequency )/2 and f<(d_4.pitch.frequency+d4.pitch.frequency )/2:
        s = 'd-4'
    elif f>(d_4.pitch.frequency+d4.pitch.frequency )/2 and f<(d4.pitch.frequency+df4.pitch.frequency )/2:
        s = 'd4'
    elif f>(d4.pitch.frequency+df4.pitch.frequency )/2 and f<(df4.pitch.frequency+e4.pitch.frequency )/2:
        s = 'd#4'
    elif f>(df4.pitch.frequency+e4.pitch.frequency )/2 and f<(e4.pitch.frequency+f4.pitch.frequency )/2:
        s = 'e4'
    elif f>(e4.pitch.frequency+f4.pitch.frequency )/2 and f<(f4.pitch.frequency+ff4.pitch.frequency )/2:
        s = 'f4'
    elif f>(f4.pitch.frequency+ff4.pitch.frequency )/2 and f<(ff4.pitch.frequency+g4.pitch.frequency )/2:
        s = 'f#4'
    elif f>(ff4.pitch.frequency+g4.pitch.frequency )/2 and f<(g4.pitch.frequency+gf4.pitch.frequency )/2:
        s = 'g4'
    elif f>(g4.pitch.frequency+gf4.pitch.frequency )/2 and f<(gf4.pitch.frequency+a4.pitch.frequency )/2:
        s = 'g#4'
    elif f>(gf4.pitch.frequency+a4.pitch.frequency )/2 and f<(a4.pitch.frequency+af4.pitch.frequency )/2:
        s = 'a4'
    elif f>(a4.pitch.frequency+af4.pitch.frequency )/2 and f<(af4.pitch.frequency+b4.pitch.frequency )/2:
        s = 'a#4'
    elif f>(af4.pitch.frequency+b4.pitch.frequency )/2 and f<(b4.pitch.frequency+c5.pitch.frequency )/2:
        s = 'b4'
    return s

b4 = note.Note('b4');
c5 = note.Note('c5');
d_5 = note.Note('d-5');
d5 = note.Note('d5');
df5 = note.Note('d#5');
e5 = note.Note('e5');
f5 = note.Note('f5');
ff5 = note.Note('f#5');
g5 = note.Note('g5');
gf5 = note.Note('g#5');
a5 = note.Note('a5');
af5 = note.Note('a#5');
b5 = note.Note('b5');
c6 = note.Note('c6');

def estimate_tone5(f):
    s = 'c5'
    if f>(b4.pitch.frequency+c5.pitch.frequency )/2 and f<(c5.pitch.frequency+d_5.pitch.frequency )/2:
        s = 'c5'
    elif f>(c5.pitch.frequency+d_5.pitch.frequency )/2 and f<(d_5.pitch.frequency+d5.pitch.frequency )/2:
        s = 'd-5'
    elif f>(d_5.pitch.frequency+d5.pitch.frequency )/2 and f<(d5.pitch.frequency+df5.pitch.frequency )/2:
        s = 'd5'
    elif f>(d5.pitch.frequency+df5.pitch.frequency )/2 and f<(df5.pitch.frequency+e5.pitch.frequency )/2:
        s = 'd#5'
    elif f>(df5.pitch.frequency+e5.pitch.frequency )/2 and f<(e5.pitch.frequency+f5.pitch.frequency )/2:
        s = 'e5'
    elif f>(e5.pitch.frequency+f5.pitch.frequency )/2 and f<(f5.pitch.frequency+ff5.pitch.frequency )/2:
        s = 'f5'
    elif f>(f5.pitch.frequency+ff5.pitch.frequency )/2 and f<(ff5.pitch.frequency+g5.pitch.frequency )/2:
        s = 'f#5'
    elif f>(ff5.pitch.frequency+g5.pitch.frequency )/2 and f<(g5.pitch.frequency+gf5.pitch.frequency )/2:
        s = 'g5'
    elif f>(g5.pitch.frequency+gf5.pitch.frequency )/2 and f<(gf5.pitch.frequency+a5.pitch.frequency )/2:
        s = 'g#5'
    elif f>(gf5.pitch.frequency+a5.pitch.frequency )/2 and f<(a5.pitch.frequency+af5.pitch.frequency )/2:
        s = 'a5'
    elif f>(a5.pitch.frequency+af5.pitch.frequency )/2 and f<(af5.pitch.frequency+b5.pitch.frequency )/2:
        s = 'a#5'
    elif f>(af5.pitch.frequency+b5.pitch.frequency )/2 and f<(b5.pitch.frequency+c6.pitch.frequency )/2:
        s = 'b5'
    return s


b5 = note.Note('b5');
c6 = note.Note('c6');
d_6 = note.Note('d-6');
d6 = note.Note('d6');
df6 = note.Note('d#6');
e6 = note.Note('e6');
f6 = note.Note('f6');
ff6 = note.Note('f#6');
g6 = note.Note('g6');
gf6 = note.Note('g#6');
a6 = note.Note('a6');
af6 = note.Note('a#6');
b6 = note.Note('b6');
c7 = note.Note('c7');

def estimate_tone6(f):
    s = 'c6'
    if f>(b5.pitch.frequency+c6.pitch.frequency )/2 and f<(c6.pitch.frequency+d_6.pitch.frequency )/2:
        s = 'c6'
    elif f>(c6.pitch.frequency+d_6.pitch.frequency )/2 and f<(d_6.pitch.frequency+d6.pitch.frequency )/2:
        s = 'd-6'
    elif f>(d_6.pitch.frequency+d6.pitch.frequency )/2 and f<(d6.pitch.frequency+df6.pitch.frequency )/2:
        s = 'd6'
    elif f>(d6.pitch.frequency+df6.pitch.frequency )/2 and f<(df6.pitch.frequency+e6.pitch.frequency )/2:
        s = 'd#6'
    elif f>(df6.pitch.frequency+e6.pitch.frequency )/2 and f<(e6.pitch.frequency+f6.pitch.frequency )/2:
        s = 'e6'
    elif f>(e6.pitch.frequency+f6.pitch.frequency )/2 and f<(f6.pitch.frequency+ff6.pitch.frequency )/2:
        s = 'f6'
    elif f>(f6.pitch.frequency+ff6.pitch.frequency )/2 and f<(ff6.pitch.frequency+g6.pitch.frequency )/2:
        s = 'f#6'
    elif f>(ff6.pitch.frequency+g6.pitch.frequency )/2 and f<(g6.pitch.frequency+gf6.pitch.frequency )/2:
        s = 'g6'
    elif f>(g6.pitch.frequency+gf6.pitch.frequency )/2 and f<(gf6.pitch.frequency+a6.pitch.frequency )/2:
        s = 'g#6'
    elif f>(gf6.pitch.frequency+a6.pitch.frequency )/2 and f<(a6.pitch.frequency+af6.pitch.frequency )/2:
        s = 'a6'
    elif f>(a6.pitch.frequency+af6.pitch.frequency )/2 and f<(af6.pitch.frequency+b6.pitch.frequency )/2:
        s = 'a#6'
    elif f>(af6.pitch.frequency+b6.pitch.frequency )/2 and f<(b6.pitch.frequency+c7.pitch.frequency )/2:
        s = 'b6'
    return s

b6 = note.Note('b6');
c7 = note.Note('c7');
d_7 = note.Note('d-7');
d7 = note.Note('d7');
df7 = note.Note('d#7');
e7 = note.Note('e7');
f7 = note.Note('f7');
ff7 = note.Note('f#7');
g7 = note.Note('g7');
gf7 = note.Note('g#7');
a7 = note.Note('a7');
af7 = note.Note('a#7');
b7 = note.Note('b7');
c8 = note.Note('c8');


def estimate_tone7(f):
    s = 'c7'
    if f>(b6.pitch.frequency+c7.pitch.frequency )/2 and f<(c7.pitch.frequency+d_7.pitch.frequency )/2:
        s = 'c7'
    elif f>(c7.pitch.frequency+d_7.pitch.frequency )/2 and f<(d_7.pitch.frequency+d7.pitch.frequency )/2:
        s = 'd-7'
    elif f>(d_7.pitch.frequency+d7.pitch.frequency )/2 and f<(d7.pitch.frequency+df7.pitch.frequency )/2:
        s = 'd7'
    elif f>(d7.pitch.frequency+df7.pitch.frequency )/2 and f<(df7.pitch.frequency+e7.pitch.frequency )/2:
        s = 'd#7'
    elif f>(df7.pitch.frequency+e7.pitch.frequency )/2 and f<(e7.pitch.frequency+f7.pitch.frequency )/2:
        s = 'e7'
    elif f>(e7.pitch.frequency+f7.pitch.frequency )/2 and f<(f7.pitch.frequency+ff7.pitch.frequency )/2:
        s = 'f7'
    elif f>(f7.pitch.frequency+ff7.pitch.frequency )/2 and f<(ff7.pitch.frequency+g7.pitch.frequency )/2:
        s = 'f#7'
    elif f>(ff7.pitch.frequency+g7.pitch.frequency )/2 and f<(g7.pitch.frequency+gf7.pitch.frequency )/2:
        s = 'g7'
    elif f>(g7.pitch.frequency+gf7.pitch.frequency )/2 and f<(gf7.pitch.frequency+a7.pitch.frequency )/2:
        s = 'g#7'
    elif f>(gf7.pitch.frequency+a7.pitch.frequency )/2 and f<(a7.pitch.frequency+af7.pitch.frequency )/2:
        s = 'a7'
    elif f>(a7.pitch.frequency+af7.pitch.frequency )/2 and f<(af7.pitch.frequency+b7.pitch.frequency )/2:
        s = 'a#7'
    elif f>(af7.pitch.frequency+b7.pitch.frequency )/2 and f<(b7.pitch.frequency+c8.pitch.frequency )/2:
        s = 'b7'
    return s

def estimate_tone(r,f):
    if r==1:
        st = estimate_tone1(f)
    elif r==2:
        st = estimate_tone2(f)
    elif r==3:
        st = estimate_tone3(f)
    elif r==4:
        st = estimate_tone4(f)
    elif r==5:
        st = estimate_tone5(f)
    elif r==6:
        st = estimate_tone6(f)
    elif r==7:
        st = estimate_tone7(f)
    else:
        print('Error in estimate_tone function')
        st = 'b8'
    return st

#Step
def estimate_pitch_final(x, onset_samples, i, sr):
    n0 = onset_samples[i]
    n1 = onset_samples[i+1]
    f0 = estimate_pitch(x[n0:n1], sr)
    r0 = estimate_range(f0)
    print(f0,r0)
    f_note = estimate_tone(r0,f0)
    print(f_note)
    n_note = note.Note(f_note)
    print(n_note.pitch)
    return n_note

# calculate the beats 1/4 is one beat
def estimate_beats(onset_times, t0):

    len_m = len(onset_times)
    print(len_m)
    beats = []
    for i in range(len_m - 2):
        t = onset_times[i + 1] - onset_times[i]
        t0 = 0.25
        beats.append(numpy.round(2 * t / t0) / 4)
        # print(beats)
        # print (t/t0)
        # print (np.around(2*t/t0)/2)
        # print (beats)

    s = sum(beats) % 4
    # print (s)
    # s1 = s%4
    if (s != 0):
        beats.append(4 - s)
    return beats

# add beats to notes
def add_beats(stream1,stream2,beats):
    for i in range(len(beats)):
        note = stream1[i+1]
        note.duration.quarterLength = beats[i]
        stream2.append(note)
    return stream2
