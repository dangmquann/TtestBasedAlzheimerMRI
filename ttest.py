import numpy as np
from data_setup import load_group_data

def PerformTtest(mri_image, group_ad, group_cn):
  from scipy.stats import ttest_ind

  AD_group = load_group_data(group_ad)
  CN_group = load_group_data(group_cn)
  N_voxel = AD_group[1] * AD_group[2] * AD_group[3]

  map_p = np.zeros((mri_image.shape))
  map_t = np.zeros((mri_image.shape))

  for i in range(AD_group.shape[1]):
    for j in range(AD_group.shape[2]):
      for k in range(AD_group.shape[3]):

        # collect voxel i of group AD, CN
        AD_values = AD_group[:, i, j, k]
        CN_values = CN_group[:, i, j, k]

        # t-test
        t_statistic, p_value = ttest_ind(AD_values, CN_values)

        map_p[i, j, k] = p_value
        map_t[i, j, k] = t_statistic

  return map_p, map_t

