# Single-Note-Music-Transcription
-------------
This is a simple music transcription application based on Autocorrelation and Constanst Q Transform.

And I am planning to rewrite it with CNN to produce better performance.

# Usage Scenario
I'm an amateur music lover and love to play the violin on popular songs. However, not every piece has the corresponding music sheet.
This makes me quite confused since I can't transcript it by myself. This problem was partially solved when I took the Digital Signal Processing
class in 2019 Spring. I learnt that the music signal has its spectrum and the tone is defined by its frequency(exactly, a range of frequency). 
Also I learnt approaches to handle these digital signals. Then I came up with the idea of building a music transcription system.
For now, this system can only transcript simple single note songs(compared to chords), and the beat division is still a problem.
So I plan to use CNN to improve its accuracy.

# Dependencies
- librosa (Python package for music and audio analysis)
- music21 (Toolkit for computer-aided musicology)
- tkinter
- MuseScore (It's a music composition and notation software. Since the output of my project is .xml document of music sheet. It has to be sent to MuseScore to perform correctly.)

# File Structure
- **utils.py**: It first seperate the single note with short time energy detection. And it will calculate the autocorrelation of the spectrum of each note to get the approximated frequency.
At last by 'if...elif...' statement, it relate the frequency to the key name on piano.
- **main.py**: Run this file and a dialog will pop up to ask you which music file is to be chosen.

# Results
![image](https://github.com/ElaineYao/Single-Note-Music-Transcription/blob/master/Cmajor.PNG)
![image](https://github.com/ElaineYao/Single-Note-Music-Transcription/blob/master/Sir%20Duke%20Piano%20Slow.PNG)

# TODO
I come up with the idea of CNN because this network model is efficient in image classification. Music Transcription can be boiled down to a classification problem and, if we jump out of conventions 
and think it in spectrum, it turns out to be image classification. Therefore I aspire to get a try on it.

The input of the network should be the spectrum per note. The dataset is [MAPS datasets](https://www.tsi.telecom-paristech.fr/aao/en/2010/07/08/maps-database-a-piano-database-for-multipitch-estimation-and-automatic-transcription-of-music/)

I designed a CNN network as follows and I am still testing this. **And the unfinished code has not been presented in the github.**

![image](https://github.com/ElaineYao/Single-Note-Music-Transcription/blob/master/CNN%20network.PNG)
