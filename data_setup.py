import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

def load_group_data(file_list):
  group_data = []
  for filename in file_list:
    img = nib.load(filename)
    data = img.get_fdata()
    group_data.append(data)
  return np.array(group_data)