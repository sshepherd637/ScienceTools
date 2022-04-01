# -*- coding: utf-8 -*-

""" Defines all the input output functions used by s4n2p2 """

""" Define constant data above class definition """

from ase import symbols 
import numpy as np

cutoff_types = {
    '0': 'Hard Cutoff Function',
    '1': 'Cosine Cutoff Function',
    '2': 'Hyperbolic Tangent Cutoff Function',
    '3': 'Hyperbolic Tangent (Unit) Cutoff Function',
    '4': 'Exponential Cutoff Function',
    '5': 'Polynomial (Order 2) Cutoff Function',
    '6': 'Polynomial (Order 3) Cutoff Function',
    '7': 'Polynomial (Order 4) Cutoff Function',
    '8': 'Polynomial (Order 5) Cutoff Function',
}

symmetry_function_types = {
    '2': 'Exponential Radial Symmetry Function',
    '3': 'Exponential Angular Symmetry Function (Narrow)',
    '9': 'Exponential Angular Symmetry Function (Wide)',
    '12': 'Elementally Weighted Exponential Radial Symmetry Function',
    '13': 'Elementally Weighted Exponential Angular Symmetry Function (Narrow)',
    '20': 'Radial Symmetry Function with Compact Support',
    '21': 'Angular Symmetry Function (Narrow) with Compact Support',
    '22': 'Angular Symmetry Function (Wide) with Compact Support',
    '23': 'Elementally Weighted Radial Symmetry Function with Compact Support',
    '24': 'Elementally Weighted Angular Symmetry Function (Narrow) with Compact Support',
    '25': 'Elementally Weighted Angular Symmetry Function (Wide) with Compact Support',
}

class SymmetryFunctionReader():
    """ Parser for all symmetry function data """

    """ creates parser for all necessary files within symmetry functions """
    def __init__(self, nnIn, scaleIn):
        self.nnIn = nnIn
        self.scaleIn = scaleIn
        self.details = {}
        self.symmetryFunctions = {
            'Functions': [],
            'Values': 0,
        }

    """ determines all required information from nnIn """
    def nnInparser(self):
        with open(self.nnIn, 'r') as handle:
            inputData = handle.readlines()
            SymFuncCounter = 0 
            for line in inputData:
                if 'number_of_elements' in line:
                    self.details['number_of_atoms'] = line.split()[1]
                if 'elements' in line: 
                    self.details['elements'] = [x for x in (line.split('#')[0]).split()[1:]]
                if 'cutoff_type' in line:
                    self.details['cutoff_function'] = cutoff_types['line.split()[1]']
                if 'symfunction_short' in line and '#' not in line:
                    SymFuncCounter += 1
                    ImportantParts = line.split()[1:]
                    ImportantParts.insert(0, SymFuncCounter)
                    for ii, ele in enumerate(ImportantParts):
                        if ii == 0:
                            continue
                        elif ele in self.details['elements']:
                            ImportantParts[ii] = symbols.atomic_numbers[ele]
                        else:
                            ImportantParts[ii] = float(ii)
                    self.symmetryFunctions['Functions'].append(ImportantParts)
            
            for ele in self.details['elements']:
                atomNumber = symbols.atomic_numbers[ele]
                keyString = f'{ele}_functions'
                eleFunction = 0
                for ii in range(len(self.symmetryFunctions['Functions'])):
                    if self.symmetryFunctions['Functions'][ii][1] == atomNumber:
                        eleFunctions += 1
                self.details['symmetry_functions'][keystring] = eleFunctions

            self.details['symmetry_functions']['number_of_symmetry_functions'] = SymFuncCounter
        
    
     """ determines all required information from scalingIn """
    def scalingInparser(self):
        values = np.genfromtxt(self.scaleIn)
        self.symmetryFunctions['Values'] = values
