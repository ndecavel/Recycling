#pip install opencv, Keras, tensorflow

import pandas as pd
import numpy as np
import os
import zipfile as zp
import shutil
import re
import seaborn as sns

import cv2 as cv
import glob as gb
import matplotlib.pyplot as plt

files = zp.ZipFile("dataset-resized.zip",'r')
files.extractall('./')
files.close()

