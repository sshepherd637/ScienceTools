# -*- coding: utf-8 -*-

""" Defines all functional forms of the cutoff functions """
import math 


""" Shared quick functions for quickness later in time"""
def X(distances, atom1, atom2, innercut, cutoff):
    interatomic_distance = distance[atom1,atom2]
    return (interatomic_distance - innercut)/(cutoff - innercut)

""" Function 0: Hard Cutoff Function"""
def cutoffFunc0():
    return 1

""" Function 1: Cosine Cutoff Function """
def cutoffFunc1(distances, atom1, atom2, innercut, cutoff):
    x = X(distances, atom1, atom2, innercut, cutoff)
    return 0.5 * (math.cos(math.pi * x) + 1)

""" Function 2: Hyperbolic Tangent Cutoff Function """
def cutoffFunc2(distances, atom1, atom2, cutoff):
    return 

    '3': 'Hyperbolic Tangent (Unit) Cutoff Function',
    '4': 'Exponential Cutoff Function',
    '5': 'Polynomial (Order 2) Cutoff Function',
    '6': 'Polynomial (Order 3) Cutoff Function',
    '7': 'Polynomial (Order 4) Cutoff Function',
    '8': 'Polynomial (Order 5) Cutoff Function',