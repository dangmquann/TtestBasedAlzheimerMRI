import argparse
import nibabel as nib
from utils import plot_sliceMRIimage, plot_slicesMRIimage
from data_setup import load_group_data
from ttest import PerformTtest

def main(args):
    # Read/Visual MRI image using Nibabel
    plot_sliceMRIimage(args.mri_image_path)
    # Plotting a series of slices through a volume
    plot_slicesMRIimage(args.mri_image_path, 4, 4)

    # Perform T-test
    mri_image = nib.load(args.mri_image_path)
    map_p, map_t = PerformTtest(mri_image, args.group_ad, args.group_cn)
    # Save the t-statistic and p-value maps as .nii files
    nib.save(nib.Nifti1Image(map_p, mri_image.affine), args.output_p_map)
    nib.save(nib.Nifti1Image(map_t, mri_image.affine), args.output_t_map)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='T-test based Alzheimer Disease Detection in MRI')
    parser.add_argument('--mri_image_path', type=str, help='Path to the MRI image')
    parser.add_argument('--group_ad', type=str, nargs='+', help='List of paths to the group AD data')
    parser.add_argument('--group_cn', type=str, nargs='+', help='List of paths to the group CN data')
    parser.add_argument('--output_p_map', type=str, help='Path to save the p-value map')
    parser.add_argument('--output_t_map', type=str, help='Path to save the t-statistic map')
    args = parser.parse_args()
    main(args)