subj = $1

python src/extract_image_list.py --subj $subj --type trial
python src/extract_image_list.py --subj $subj --type cocoId

