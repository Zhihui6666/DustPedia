#!/usr/bin/env python
# -*- coding: utf8 -*-
# **********************************
# **       DUSTPEDIA API          **
# **********************************

# -----------------------------------------------------------------

# Ensure Python 3 functionality
from __future__ import absolute_import, division, print_function

# Import standard modules
import os
import argparse

# Import DustPedia API
from core.database import DustPediaDatabase

# -----------------------------------------------------------------

# Parse arguments
parser = argparse.ArgumentParser(description="show header")
parser.add_argument("username", type=str, help="DustPedia archive username")
parser.add_argument("password", type=str, help="DustPedia archive password")
parser.add_argument("name", type=str, help="the image name [galaxyname_instrument_band.fits]")
arguments = parser.parse_args()

# -----------------------------------------------------------------

# Create the database
database = DustPediaDatabase()

# Login
database.login(arguments.username, arguments.password)

# -----------------------------------------------------------------

path = os.getcwd()

# CORRECT
if not arguments.name.endswith("fits"): arguments.name = arguments.name + ".fits"

galaxy_name = arguments.name.split("_")[0]

# Download
header = database.get_header(galaxy_name, arguments.name, path)

for key in header: print(key + ": " + str(header[key]))

# -----------------------------------------------------------------
