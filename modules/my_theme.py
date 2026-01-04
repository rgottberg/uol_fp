#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 20:47:20 2025

@author: cod
"""

# import libraries
from pathlib import Path
from shiny import ui

# pre-built theme
my_theme = (
    ui.Theme("flatly")
    )

# create css file
with open(Path(__file__).parent / "my_theme.css", "w") as f:
    f.write(my_theme.to_css())