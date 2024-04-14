#!/bin/bash
# Required >= Python 3.12.1
pyinstaller main.py --hidden-import='PIL._tkinter_finder' --noconfirm -n CTPlot -w