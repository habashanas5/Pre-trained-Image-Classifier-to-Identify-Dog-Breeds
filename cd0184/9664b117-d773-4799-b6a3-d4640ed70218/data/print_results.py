#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Anas Habash
# DATE CREATED: 2-3-2025                         
# REVISED DATE: 2-3-2025
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results from classification and can print misclassified dogs and misclassified breeds.

    Parameters:
      results_dic: Dictionary containing image details with each key being the image filename.
      results_stats_dic: Dictionary containing statistical results like number of images, percentages, etc.
      model: The CNN model architecture used for classification (e.g., 'resnet', 'alexnet', 'vgg').
      print_incorrect_dogs: If True, will print the dogs that were misclassified (default is False).
      print_incorrect_breed: If True, will print the breeds of dogs that were misclassified (default is False).

    Returns:
      None. The function prints the results.
    """

    # Print the CNN model being used
    print(f"\nUsing Model: {model.upper()}")

    # Print the general statistics of classification results
    print("\nGeneral Statistics:")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of Not-a-Dog Images: {results_stats_dic['n_notdogs_img']}")

    # Print percentage-based statistics
    print("\nPercentage Statistics:")
    print(f"% Correctly Classified Dogs: {results_stats_dic['pct_correct_dogs']:.2f}%")
    print(f"% Correctly Classified Breeds: {results_stats_dic['pct_correct_breed']:.2f}%")
    print(f"% Correctly Classified Not-a-Dog: {results_stats_dic['pct_correct_notdogs']:.2f}%")
    print(f"% Match: {results_stats_dic['pct_match']:.2f}%")

    # Print misclassified dogs if requested
    if print_incorrect_dogs:
        print("\nMisclassified Dogs:")
        for key in results_dic:
            # Check if the image is classified incorrectly as a dog
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                print(f"Pet Image: {results_dic[key][0]}, Classifier: {results_dic[key][1]}")

    # Print misclassified breeds if requested
    if print_incorrect_breed:
        print("\nMisclassified Breeds:")
        for key in results_dic:
            # Check if the image is a dog but classified under the wrong breed
            if results_dic[key][3] == 1 and results_dic[key][2] == 0:
                print(f"Pet Image: {results_dic[key][0]}, Classifier: {results_dic[key][1]}")