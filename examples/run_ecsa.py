import argparse
from pathlib import Path

from src.cv_functions import get_df
from src.ecsa_functions import calculate_Cdl


parser = argparse.ArgumentParser()

parser.add_argument("file")
parser.add_argument("--pH", type=float, required=True)
parser.add_argument("--potential", type=float, required=True)

args = parser.parse_args()


file_path = Path(args.file)

sample_folder = file_path.parent
mpr_filename = file_path.name


df = get_df(sample_folder, mpr_filename, args.pH)

cdl = calculate_Cdl(df, args.potential)

print("Cdl =", cdl)