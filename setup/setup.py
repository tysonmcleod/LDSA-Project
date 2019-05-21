import os

os.system("conda env create -f env.yml")
os.system("conda activate pyspark")
os.system("python -m retro.import ROMs")