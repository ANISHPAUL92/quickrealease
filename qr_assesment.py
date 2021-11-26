#!/usr/bin/env python
# coding: utf-8
# -----------------------------------------------------------
# This file can be used to fetch request from
# https://interviewbom.herokuapp.com/bom/ and details 
# of parts and quatities.
#
# (C) 2021 Anish Paul Thekkan.
# Released under GNU Public License (GPL)
# email anishpaul92@gmail.com
# -----------------------------------------------------------


import json 
import requests
import sys
from xlwt import Workbook


def check_for_correct_arguments(arguments):
    """Method for checking the number of arguments sent to the script"""

    if (arguments > 2 or arguments <= 1):
        print("Incorrect Arguments sent, Please check and execute the script again")
        exit()
        
def write_and_save_to_excel(total_quantity_dictionary, excel_name):
    """Method to write in excel and save it on .xls"""

    
    wb = Workbook()
    excel_sheet = wb.add_sheet('Part Name and Quantity')
    column_value = 0 
    excel_sheet.write(0,0,'Part_Name')
    excel_sheet.write(0,1,'Part_Quantities')
    #Creating a counter to increment row while writing in the excel
    i = 0
    
    for key in total_quantity_dictionary:
        excel_sheet.write(i + 1, column_value, key)
        excel_sheet.write(i + 1, column_value + 1, total_quantity_dictionary[key])
        i += 1
        
    wb.save(excel_name)    
    
def create_parts_dictionary_with_quantity(partsdescription):
    """Method for creating dictionary with each part and quantities"""
    
    parent_part_key = "parent_part_id"
    part_name_key = "part_id"
    part_quantity_key = "quantity"
    
    #Creating 3 different lists, first one containing all the parents
    #Second one containing all the part names and the third one for the quantites
    parent_parts = [parent_id[parent_part_key] for parent_id in partsdescription]
    part_names = [part_name[part_name_key] for part_name in partsdescription ]
    quantity_values = [quantity[part_quantity_key] for quantity in partsdescription]
    
    #Creating 3 different dictionaries, first one containing part names and it's quantities
    #Second one containing parent parts and it's children and 
    #Initialising the third one to empty which will contain the final total count
    parent_parts_with_part = dict(zip(parent_parts,part_names))
    part_name_with_quantities = dict(zip(part_names,quantity_values))
    total_quantity_dictionary = dict()
    
    #Initialising a flag to 0 so that we can ignore the first part who does not have a parent
    flag = 0    
    #Loop for filling the total_quantity_dictionary with quantities of parent parts
    for parent_key in parent_parts_with_part:
        if flag == 0:
            flag = 1
        else:
            total_quantity_dictionary[parent_key] = part_name_with_quantities[parent_key]
    
    #Sorting the total_quantity_dictionary in ascending order for computing the right values of parent parts
    total_quantity_dictionary = dict(sorted(total_quantity_dictionary.items(), key=lambda item: item[1]))

    #Initialising a flag to 0 so that we can ignore the first part who does not have a parent    
    flag = 0
    #Computing the initial quantity values of parent parts 
    for parent_key in parent_parts_with_part:
        if flag == 0:
            flag = 1
        else:
            for part_key in total_quantity_dictionary:
                i = 0
                if parent_parts_with_part[parent_key] == part_key:
                    total_quantity_dictionary[part_key] = total_quantity_dictionary[parent_key] * total_quantity_dictionary[part_key]
                    i += 1
                    break

    #Initialising a flag to 0 so that we can ignore the first part who does not have a parent    
    flag = 0
    #Computing the final quantity values for every part
    for parent_key in parent_parts_with_part:
        if flag == 0:
           flag = 1
        else:
            for part_key in part_name_with_quantities:
                if parent_parts_with_part[parent_key] == part_key:
                    total_quantity_dictionary[part_key] = total_quantity_dictionary[parent_key] * part_name_with_quantities[part_key]
                    break
    
    return total_quantity_dictionary

def fetch_data_from_URL( url ):
    """Method to fetch data from the URl"""

    response_api = requests.get(url)
    data = response_api.text
    parse_json = json.loads(data)
    partsdescription = parse_json["data"]

    return partsdescription
    

##############################    
########  START HERE  ########
##############################
def main():
    arguments = len(sys.argv)
    #Method to check whether the arguments sent to the script are correct
    check_for_correct_arguments(arguments)
    
    excel_name = sys.argv[1]
    URL = "https://interviewbom.herokuapp.com/bom/"    

    #Method to fetch data from the URL 
    partsdescription = fetch_data_from_URL(URL)

    #Method to create dictionary with parts and correct quantities     
    total_quantity_dictionary = create_parts_dictionary_with_quantity(partsdescription)

    #Method to write the parts and quantites in the dictionary
    write_and_save_to_excel(total_quantity_dictionary, excel_name)
    print(f"**********\nPlease check the excel {excel_name} for the part name and final quantities\n**********")


if __name__ == "__main__":
    main()
    




