#!/usr/bin/env python3

"""
    Script created to compute the interlayer distance between a two layer system.
    The interlayer distance at any time T is dependant on the interlayer interactions between
    the two layers. By computing this interlayer distance (Simply the Z component) we can gather 
    a comparative measure of the mobility of the clay layers, i.e. weaker interlayer interactions
    would allow for larger fluctuations in the interlayer distance and vice-versa.
"""

# Import modules for use later within script
import numpy as np

from ase import Atoms
from ase.io import read
from ase.units import Bohr

# Define functions that are used within this script
def getLayers(frame):
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
    TOP = Atoms(TopLayer)
    BOT = Atoms(BottomLayer)
    return TOP, BOT

def getInterlayerDistance(top, bot):
    """ 
        Function to compute the average C component of a layer of atoms, then find the distance 
        between two layers. We will compute this from the Al of the bottom and the Si of the top
    """
    Al_bot = []
    Si_top = []
    for atom in top:
        if atom.symbol == 'Si':
            Si_top.append(atom.position[2])
    
    for atom in bot:
        if atom.symbol == 'Al':
            Al_bot.append(atom.position[2])

    AlavgC = np.mean(np.array(Al_bot))
    SiavgC = np.mean(np.array(Si_top))
    return SiavgC - AlavgC

# This script is called on individual frames to allow quick I/O on python's part
with open("InterD.dat", 'a') as handle:
    input = read('cur-frames.pdb', ':')
    no_atoms = len(input[0])

# Convert Bohr to Å for ease of use later.
    for frame in input:
        if len(frame) == 272:
            frame.set_cell(frame.cell * Bohr)
            frame.set_positions(frame.positions * Bohr)
            
# Feed the frame to the above functions to get separation of layers and perform sanity checks
            Top, Bot = getLayers(frame)
            InterC = getInterlayerDistance(Top, Bot)
            handle.write(f'{InterC:<14.8f}\n')