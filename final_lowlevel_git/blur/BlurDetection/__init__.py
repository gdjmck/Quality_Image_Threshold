#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in modules
# Standard modules
# Custom modules
import sys
missing_path = '/home/chk/Documents/data/Quality_Image_Threshold/final_lowlevel_git/blur/BlurDetection'
sys.path.append(missing_path)
print('Add ', missing_path)

from main import *
from FocusMask import *
import scripts