import numpy as np
from PIL import Image

subj = 1
project_output_dir = 'output'

# stimuli_dir is from config
stimuli_dir = 'data/NSD_images/images'
all_coco_ids = np.load("%s/coco_ID_of_repeats_subj%02d.npy" %
                       (project_output_dir, subj))

all_images_paths = ["%s/%s.jpg" % (stimuli_dir, id) for id in all_coco_ids]
print("Number of Images: {}".format(len(all_images_paths)))

# check brain data shape
br_data = np.load('output/cortical_voxels/averaged_cortical_responses_zscored_by_run_subj%02d.npy' % subj)
print("Brain data shape:", br_data.shape)

# generate an image array
image_array = np.array([np.array(Image.open(img_path).convert('RGB'))
                        for img_path in all_images_paths])
print("Image array shape: {}".format(image_array.shape))

trial_mask = np.sum(np.isnan(br_data), axis=1) <= 0
br_data = br_data[trial_mask, :]

image_array = image_array[trial_mask, :, :, :]

print("remove dead trials; brain data shape:", br_data.shape)
print("image array shape:", image_array.shape)
