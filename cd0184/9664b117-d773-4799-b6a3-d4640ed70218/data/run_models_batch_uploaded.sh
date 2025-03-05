#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch_uploaded.sh
#                                                                             
# PROGRAMMER: Anas Habash
# DATE CREATED: 3-5-2025                                
# REVISED DATE: 3-5-2025  - 
# PURPOSE: Runs all three models to test which provides 'best' solution on the Uploaded Images.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch_uploaded.sh    -- will run program from commandline within Project Workspace
#  
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/uploaded_images/ --arch resnet  --dogfile /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/dognames.txt > /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/resnet_uploaded-images.txt
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/uploaded_images/ --arch alexnet --dogfile /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/dognames.txt > /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/alexnet_uploaded-images.txt
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/uploaded_images/ --arch vgg  --dogfile /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/dognames.txt > /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/vgg_uploaded-images.txt

