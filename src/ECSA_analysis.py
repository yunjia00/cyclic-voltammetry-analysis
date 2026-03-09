import pandas as pd
import numpy as np
from scipy.stats import linregress


def get_scan_rates(df):

    if "scan rate" not in df.columns:
        raise ValueError("scan rate column not found")

    scan_rates = sorted(df["scan rate"].unique())

    return scan_rates


def extract_current(df, potential, window=0.005):

    mask = (df["E vs RHE / V"] > potential - window) & (
        df["E vs RHE / V"] < potential + window
    )

    sub = df[mask]

    return sub["<I>/mA"].mean()


def calculate_Cdl(df, potential):

    scan_rates = get_scan_rates(df)

    anodic = []
    cathodic = []

    for rate in scan_rates:

        df_rate = df[df["scan rate"] == rate]

        current = extract_current(df_rate, potential)

        anodic.append(current)

        cathodic.append(-current)

    delta_j = [(a - c) / 2 for a, c in zip(anodic, cathodic)]

    slope, intercept, r, p, stderr = linregress(scan_rates, delta_j)

    return slope