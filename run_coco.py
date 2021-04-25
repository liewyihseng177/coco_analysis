import os
os.system('pip install cocopp')

import cocopp
import webbrowser

cocopp.main('DEPSOdatamax50000 SimpleDEdatamax50000')

webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")