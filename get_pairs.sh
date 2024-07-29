#!/bin/bash
subj=1

python src/extract_image_list.py --subj $subj --type trial
python src/extract_image_list.py --subj $subj --type cocoId

python src/extract_cortical_voxel.py --zscore_by_run --subj $subj

# extract ROI mask to apply on cortical data
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi prf-eccrois
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi prf-visualrois
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi floc-faces
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi floc-words
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi floc-places
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi floc-bodies
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi Kastner2015
python src/extract_cortical_voxel.py --subj $subj --mask_only --roi HCP_MMP1


# computer explainable variance for the data and output data averaged by repeats
python src/compute_ev.py --subj $subj --zscored_input --compute_ev
