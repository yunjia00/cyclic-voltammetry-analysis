import numpy as np


def determine_onset(df, left_bound, right_bound, n_sigma=3):

    df_window = df[
        (df["E vs RHE / V"] >= left_bound)
        & (df["E vs RHE / V"] <= right_bound)
    ]

    baseline = df_window["<I>/mA"].mean()

    noise = df_window["<I>/mA"].std()

    threshold = baseline + n_sigma * noise

    df_after = df[df["E vs RHE / V"] > right_bound]

    onset = df_after[df_after["<I>/mA"] > threshold]

    if onset.empty:
        return None

    return onset.iloc[0]["E vs RHE / V"]