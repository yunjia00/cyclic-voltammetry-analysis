# cyclic-voltammetry-analysis
Python scripts for processing and analyzing cyclic voltammetry (CV) data from EC-Lab. 
This repository contains scripts for common electrochemical data analysis tasks used in catalysis and electrochemistry research, including:

CV plotting (current density vs potential)

  ECSA estimation from CV
  
  Onset potential detection
  
  The scripts read BioLogic .mpr files using the galvani package and perform analysis with pandas, numpy, and matplotlib.

Usage
  All scripts use BioLogic .mpr files as input.

  CV Plotting
  
  Plot current density versus potential (vs RHE):
  
  python scripts/run_cv.py file.mpr --pH 6.0 --ECSA 0.18

  Parameters
  
  file - Path to the BioLogic .mpr file.
    
  pH - Electrolyte pH used for conversion to the RHE scale.
    
  ECSA - Electrochemical surface area of the electrode (cm²).

  This script converts current to current density and generates a CV plot.

ECSA Calculation
  Estimate the double-layer capacitance (Cdl) from CV measurements.
  
  python scripts/run_ecsa.py file.mpr --pH 7 --potential 0.1

  Parameters
  file - Path to the BioLogic .mpr file.
  
  pH - Electrolyte pH.
  
  potential - Potential at which capacitive current is extracted.

  The script automatically detects scan rates from the BioLogic file and performs a linear fit of capacitive current versus scan rate to estimate Cdl.

Onset Potential Detection

  Determine the onset potential based on baseline noise in the double-layer region.
  
  python scripts/run_onset.py file.mpr --pH 6.5 --left -0.8 --right -0.5

  Parameters
  
  file - Path to the BioLogic .mpr file.
  
  pH - Electrolyte pH.
  
  left - Left boundary of the double-layer region used to calculate the baseline.
  
  right - Right boundary of the double-layer region used to calculate the baseline.

  The onset potential is defined as the first potential where the current exceeds the baseline plus a noise threshold.
