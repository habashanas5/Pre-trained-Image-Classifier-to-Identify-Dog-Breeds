#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch_uploaded.sh
#                                                                             
# PROGRAMMER: Anas Habash
# DATE CREATED: 5-3-2025                                  
# REVISED DATE: 7-3-2025  
# PURPOSE: Runs all three models to test which provides 'best' solution on the Uploaded Images.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch_uploaded.sh    -- will run program from commandline within Project Workspace
#  

python check_images.py --dir uploaded_images/ --arch resnet  --dogfile dognames.txt > resnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch alexnet --dogfile dognames.txt > alexnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch vgg  --dogfile dognames.txt > vgg_uploaded-images.txt
