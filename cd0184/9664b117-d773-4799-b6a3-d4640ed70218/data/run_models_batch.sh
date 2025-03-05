#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch.sh
#                                                                             
# PROGRAMMER: Anas Habash
# DATE CREATED: 3-5-2025                                  
# REVISED DATE: 3-5-2025  - 
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch.sh    -- will run program from commandline within Project Workspace
#  
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images/ --arch resnet  --dogfile /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/dognames.txt > resnet_pet-images.txt
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images/ --arch alexnet --dogfile /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/dognames.txt > alexnet_pet-images.txt
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images/ --arch vgg  --dogfile /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/dognames.txt > vgg_pet-images.txt


