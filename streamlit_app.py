import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from music21 import note, stream

s = stream.Stream()

# Add some notes to the stream
s.append(note.Note('C4', quarterLength=1))
s.append(note.Note('E4', quarterLength=1))
s.append(note.Note('G4', quarterLength=1))
s.append(note.Note('C5', quarterLength=1))

def draw_staff():
    
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Draw the staff lines
    for i in range(5):
        ax.plot([0, 10], [i, i], color='black')

    return ax

def draw_notes(ax, notes):
    positions = {'C4': 0, 'D4': 0.5, 'E4': 1, 'F4': 1.5, 'G4': 2, 'A4': 2.5, 'B4': 3, 'C5': 3.5}
    x = 1
    for n in notes:
        y = positions[n.nameWithOctave]
        ax.plot(x, y, 'o', color='black')
        x += 2

#ax = draw_staff()
#draw_notes(ax, s.notes)
plt.show()
