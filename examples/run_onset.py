import argparse
from pathlib import Path

from src.cv_functions import get_df
from src.onset_functions import determine_onset


def main():

    parser = argparse.ArgumentParser(
        description="Determine onset potential from BioLogic CV data"
    )

    parser.add_argument(
        "file",
        help="Path to .mpr file"
    )

    parser.add_argument(
        "--pH",
        type=float,
        required=True,
        help="Electrolyte pH"
    )

    parser.add_argument(
        "--Eshift",
        type=float,
        default=-0.2727,
        help="Reference electrode shift"
    )

    parser.add_argument(
        "--left",
        type=float,
        required=True,
        help="Left bound of double-layer region (V vs RHE)"
    )

    parser.add_argument(
        "--right",
        type=float,
        required=True,
        help="Right bound of double-layer region (V vs RHE)"
    )

    args = parser.parse_args()

    file_path = Path(args.file)

    sample_folder = file_path.parent
    mpr_filename = file_path.name

    df = get_df(
        sample_folder,
        mpr_filename,
        args.pH,
        args.Eshift
    )

    onset = determine_onset(
        df,
        left_bound=args.left,
        right_bound=args.right
    )

    if onset is None:
        print("Onset potential not detected")
    else:
        print(f"Onset potential: {onset:.4f} V vs RHE")


if __name__ == "__main__":
    main()