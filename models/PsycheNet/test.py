import mne
import numpy as np

# Load BrainVision dataset
raw = mne.io.read_raw_brainvision(
    '/home/execphantasmagoria/Code/uni/PsycheProcessor/PsycheNet/data/ds006033/sub-01/ses-02/eeg/sub-01_ses-02_task-innerspeech_eeg.vhdr',
    preload=True
)

# Print basic info
print(raw.info)
print(raw.ch_names)