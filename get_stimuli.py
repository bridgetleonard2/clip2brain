import numpy as np

subj = 1
project_output_dir = 'output'

# stimuli_dir is from config
stimuli_dir = 'data/NSD_images/images'
all_coco_ids = np.load("%s/coco_ID_of_repeats_subj%02d.npy" %
                       (project_output_dir, subj))

all_images_paths = ["%s/%s.jpg" % (stimuli_dir, id) for id in all_coco_ids]
print("Number of Images: {}".format(len(all_images_paths)))
