#!/usr/bin/env python3

""" 
    Script created to compute the centre of mass vector (COMv) between a two layer system.
    Each layer possesses a unique centre of mass, rather than trying to work with the over
    -all COM. This allows for computation to take place that allows us to get a measure of
    the 'mobility' of the layers independantly.
"""

# Import modules for use later within script
import numpy as np

from ase import Atoms
from ase.io import read
from ase.units import Bohr

# Define functions that are used within this script
def getLayers(frame):
    """ Function to separate large frames into individual layers 
    It achieves this by calculating the middle of the C vector and 
    using the Z component as the 1/2 height point and separating based
    atomic positions relative to this. """
    TopLayer = []
    BottomLayer = []
    LargestZ = np.max(frame.positions[:,2])
    for atom in frame:
        if atom.position[2] > LargestZ / 2:
            TopLayer.append(atom)
        else:
            BottomLayer.append(atom)
    return TopLayer, BottomLayer

def getCOM(Layer):
    """ Function to return the centre of masses for the layer provided to
    it. This is done through a function within ase but I'm wrapping it within
    a function for clarity. """
    ASELayer = Atoms(Layer, pbc=[1,1,1])
    COM = ASELayer.get_center_of_mass()
    return np.array(COM)

# This script is called on individual frames to allow quick I/O on python's part
with open("COMv.dat", 'a') as handle:
    input = read('cur-frames.pdb', ':')
    no_atoms = len(input[0])

# Convert Bohr to Å for ease of use later.
    for frame in input:
        frame.set_cell(frame.cell * Bohr)
        frame.set_positions(frame.positions * Bohr)

# Feed the frame to the above functions to get separation of layers and perform sanity checks
        TopLayer, BotLayer = getLayers(frame)
        if len(TopLayer) != int(no_atoms) / 2:
            raise ValueError(f'Number of atoms in individual layers is not correct: \nTotal Atoms: {no_atoms}\nTop Layer: {len(TopLayer)}\nBottom Layer: {len(BotLayer)}')
        TopCOM, BotCOM = getCOM(TopLayer), getCOM(BotLayer)

# The vector mathematics is very simple, TopCOM - BotCOM = COMv
        COMv = TopCOM - BotCOM
        handle.write(f'{COMv[0]:<14.8f}{COMv[1]:<14.8f}{COMv[2]:<14.8f}{TopCOM[0]:<14.8f}{TopCOM[1]:<14.8f}{TopCOM[2]:<14.8f}{BotCOM[0]:<14.8f}{BotCOM[1]:<14.8f}{BotCOM[2]:<14.8f}\n')

