#!/bin/python3

import numpy as np
import cv2
import os, sys
import time
import operator

from string import ascii_uppercase

import tkinter as tk
from PIL import Image, ImageTk
from gtts import gtts
from playsound import playsound
from keras.models import model_from_json
