import os
os.system('pip install cocopp')

import cocopp
import webbrowser

cocopp.main('CMA-ES DE DEPSO PSO')

webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")