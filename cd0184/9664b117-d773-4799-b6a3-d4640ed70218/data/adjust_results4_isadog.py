#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Anas Habash
# DATE CREATED: 2-3-2025                         
# REVISED DATE: 2-3-2025
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    # Read the dog names from the file into a dictionary
    dognames_dic = dict()
    with open(dogfile, 'r') as file:
        for line in file:
            dog_name = line.strip()  # Remove newline characters
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print(f"** Warning: Duplicate dog name found: {dog_name}")

    # Iterate through the results dictionary
    for key in results_dic:
        # Get the pet image label and classifier label
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Check if the pet image label is a dog
        if pet_label in dognames_dic:
            pet_label_is_dog = 1
        else:
            pet_label_is_dog = 0

        # Check if the classifier label is a dog
        if classifier_label in dognames_dic:
            classifier_label_is_dog = 1
        else:
            classifier_label_is_dog = 0

        # Add the results to the list in results_dic
        results_dic[key].extend([pet_label_is_dog, classifier_label_is_dog])