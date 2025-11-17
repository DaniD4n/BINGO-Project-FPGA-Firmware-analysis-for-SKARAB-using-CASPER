from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py

# Load the .npz file
npz_name = '/home/bingo/Satellites/2025-09-10/ch1/Averages_CH1_2357.npz'
data = np.load(npz_name)

# Sort spectrum keys
keys = sorted(data.files)

# Process spectra
spectra_list = []
for k in keys:
    arr = np.array(data[k])
    arr = np.fft.fftshift(arr, axes=1).T
    spectra_list.append(arr)

# Concatenate
big_spectra = np.concatenate(spectra_list, axis=1)

# Build timestamps
start_dt = datetime.strptime(keys[0], '%H%M%S')
end_dt   = datetime.strptime(keys[-1], '%H%M%S')
total_time_steps = big_spectra.shape[1]
timestamps = pd.date_range(start=start_dt, end=end_dt, periods=total_time_steps)

# ---- Salvar em HDF5 ----
hdf5_name = "spectra_concatenated.h5"

with h5py.File(hdf5_name, "w") as f:
    f.create_dataset("spectra", data=big_spectra)
    ts_str = np.array(timestamps.astype(str), dtype="S26")
    f.create_dataset("timestamps", data=ts_str)

print("Arquivo HDF5 salvo como:", hdf5_name)
