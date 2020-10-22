import numpy as np
import random
import sys
import os
import glob
from flask import Flask
from board import Board
from cell import Cell


app = Flask(__name__)

#@app.route('/gameoflife', method='GET', 'POST')
#def gameoflife():
