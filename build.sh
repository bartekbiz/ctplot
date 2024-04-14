#!/bin/bash

pyinstaller main.py --hidden-import='PIL._tkinter_finder' --noconfirm