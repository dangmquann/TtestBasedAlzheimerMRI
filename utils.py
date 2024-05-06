import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

def plot_sliceMRIimage(path):
  mri_image = nib.load(path)
  mri_image_data = mri_image.get_fdata()
  plt.imshow(mri_image_data[:,:,mri_image_data.shape[2] // 2], cmap="bone")
  plt.show()


#Generate a series of slices of the MRI image
def plot_slicesMRIimage(path, n_row, n_col):
    mri_image = nib.load(path)
    mri_image_data = mri_image.get_fdata()
    fig_rows = n_row
    fig_cols = n_col
    n_subplots = fig_rows * fig_cols

    n_slice = mri_image_data.shape[0]
    step_size = n_slice // n_subplots
    plot_range = n_subplots * step_size
    start_stop = int((n_slice - plot_range) / 2)

    fig, axs = plt.subplots(fig_rows, fig_cols, figsize=[10, 10])

    for idx, img in enumerate(range(start_stop, plot_range, step_size)):
        axs.flat[idx].imshow(mri_image_data[:, :, img], cmap='gray')
        axs.flat[idx].axis('off')

    plt.tight_layout()
    plt.show()

