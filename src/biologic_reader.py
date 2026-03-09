from pathlib import Path
from galvani import BioLogic
import pandas as pd


def read_mpr(file_path, pH, E_shift):
    """
    Read BioLogic .mpr file and convert potential to RHE scale.
    """

    file_path = Path(file_path)

    mpr = BioLogic.MPRfile(file_path)

    df = pd.DataFrame(mpr.data)

    df["E_vs_RHE_V"] = df["Ewe/V"] - E_shift + 0.059 * (pH - 1)

    return df