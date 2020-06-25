# PIMD_for_fermions_data
Raw data for arXiv:2003.10317, published in https://doi.org/10.1063/5.0008720

NOTE: found a minor bug in error estimation in the python script.
The reported error is too large by a factor of (Neff-1)^(1/4), which is smaller than 2 for all cases considered.
I am keeping the original script here for reproducibility but to get the correct error, as described in the SI, replace all "np.sqrt(Neff-1)" in the python script with "(Neff-1)".

Also added analyze_fermions_fixed.py for the corrected script.
