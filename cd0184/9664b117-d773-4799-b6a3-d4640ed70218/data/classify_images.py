#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Anas Habash
# DATE CREATED: 2-3-2025                         
# REVISED DATE: 2-3-2025
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 

def classify_images(images_dir, results_dic, model):
    # Iterate through the results dictionary
    for key in results_dic:
        # Get the full path to the image
        image_path = images_dir + key

        # Use the classifier function to get the classifier label
        classifier_label = classifier(image_path, model)

        # Format the classifier label (lowercase and strip whitespace)
        classifier_label = classifier_label.lower().strip()

        # Get the pet image label from the results dictionary
        pet_label = results_dic[key][0]

        # Compare the pet label and classifier label
        # If the pet label is found in the classifier label, it's a match
        if pet_label in classifier_label:
            results_dic[key].extend([classifier_label, 1])  # Match
        else:
            results_dic[key].extend([classifier_label, 0])  # No match