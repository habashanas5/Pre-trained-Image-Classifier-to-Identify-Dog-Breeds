#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Anas Habash
# DATE CREATED: 2-3-2025                         
# REVISED DATE: 2-3-2025
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##

import argparse

def get_input_args(): 
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 3 command line arguments as mentioned above using add_argument() from ArgumentParser method
    parser.add_argument('--dir', type=str, default='/workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images/', 
                        help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', 
                        help='CNN model architecture to use (vgg, alexnet, resnet)')
    parser.add_argument('--dogfile', type=str, default='/workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/dognames.txt', 
                        help='file that contains the list of valid dognames')

    return parser.parse_args()