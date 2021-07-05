# Artificial Perturbations

Artificial Perturbations is the lovingly coined term I have given these notebooks, for they are the most 'by hand' method currently available to try and increase the sampling points of the dataset.

# Methodology

Through the use of pythons ase module, we can quickly get the bonding vector between two atoms, and as a function of its component vectors, we can then decrease or increase this length as a function
of length only through the change of the magnitude of this vector. This is particularly useful for the linear shortening and lengthing of a bond, and allows for the creations of data which will (hopefully)
aid in the sample space coverage of the model. 
