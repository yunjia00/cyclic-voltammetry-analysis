from pathlib import Path
from galvani import BioLogic

import pandas as pd
import matplotlib.pyplot as plt


def get_df(sample_folder, mpr_filename, pH, E_shift=-0.2727):

    mpr_path = Path(sample_folder) / mpr_filename

    mpr_file = BioLogic.MPRfile(mpr_path)

    df = pd.DataFrame(mpr_file.data)

    df["E vs RHE / V"] = df["Ewe/V"] - E_shift + 0.059 * (pH - 1)

    return df


def Plot_J_vs_EvsRHE(df, ax, ECSA, Selected_CycleNumber, label=None):

    I_col = "<I>/mA"
    cycle_col = "cycle number"

    df_cyc = df[df[cycle_col] == Selected_CycleNumber].copy()

    if df_cyc.empty:
        print(f"Cycle {Selected_CycleNumber} 不存在")
        return

    df_cyc["j / mA·cm^-2"] = df_cyc[I_col] / ECSA

    ax.plot(df_cyc["E vs RHE / V"], df_cyc["j / mA·cm^-2"], label=str(label))

    ax.set_xlabel("E[V] vs. RHE")
    ax.set_ylabel("j[mA·cm$^{-2}$]")


def Plot_Allcycle_J_vs_EvsRHE(df, ax, ECSA, label=None):

    I_col = "<I>/mA"

    df = df.copy()

    df["j / mA·cm^-2"] = df[I_col] / ECSA

    ax.plot(df["E vs RHE / V"], df["j / mA·cm^-2"], label=str(label))

    ax.set_xlabel("E[V] vs. RHE")
    ax.set_ylabel("j[mA·cm$^{-2}$]")