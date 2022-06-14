#!/usr/bin/env python3

"""
    Script created to compute the interlayer distance between a two layer system.
    The interlayer distance at any time T is dependant on the interlayer interactions between
    the two layers. By computing this interlayer distance (Simply the Z component) we can gather 
    a comparative measure of the mobility of the clay layers, i.e. weaker interlayer interactions
    would allow for larger fluctuations in the interlayer distance and vice-versa.
"""

# Import modules for use later within script
from tkinter import TOP
import numpy as np

from ase import Atoms
from ase.io import read
from ase.units import Bohr

# Define functions that are used within this script
def getInterlayerDistance(frame):
    """ 
        Function to select the important atoms (highest of BOT and lowest of TOP) 
        It achieves this by calculating the middle of the C vector and 
        using the Z component as the 1/2 height point, then selecting the atoms that are
        closest to this both greater than and less than 
    """
    TopLayer = []
    BottomLayer = []
    LargestZ = np.max(frame.positions[:,2])
    for atom in frame:
        if atom.position[2] > LargestZ / 2:
            TopLayer.append(atom)
        else:
            BottomLayer.append(atom)
    TOPLowAtom = sorted(Atoms(TopLayer).positions[:,2])[0]
    BOTHighAtom = sorted(Atoms(BottomLayer).positions[:,2])[-1]
    Interlayer_Z = TOPLowAtom - BOTHighAtom
    return Interlayer_Z

# This script is called on individual frames to allow quick I/O on python's part
with open("InterD.dat", 'a') as handle:
    input = read('cur-frames.pdb', ':')
    no_atoms = len(input[0])

# Convert Bohr to Å for ease of use later.
    for frame in input:
        frame.set_cell(frame.cell * Bohr)
        frame.set_positions(frame.positions * Bohr)

# Feed the frame to the above functions to get separation of layers and perform sanity checks
        Interlayer_D = getInterlayerDistance(frame)
        handle.write(f'{Interlayer_D:<14.8f}\n')