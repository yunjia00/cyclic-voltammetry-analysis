import argparse
import matplotlib.pyplot as plt
from pathlib import Path

from src.cv_functions import get_df, Plot_Allcycle_J_vs_EvsRHE


parser = argparse.ArgumentParser()

parser.add_argument("file")
parser.add_argument("--pH", type=float, required=True)
parser.add_argument("--ECSA", type=float, required=True)
parser.add_argument("--Eshift", type=float, default=-0.2727)

args = parser.parse_args()


file_path = Path(args.file)

sample_folder = file_path.parent
mpr_filename = file_path.name


df = get_df(sample_folder, mpr_filename, args.pH, args.Eshift)

fig, ax = plt.subplots(figsize=(10, 6))

Plot_Allcycle_J_vs_EvsRHE(df, ax, args.ECSA)

plt.show()