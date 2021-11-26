#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:06:34 2021
# (C) 2021 Anish Paul Thekkan.
# Released under GNU Public License (GPL)
# email anishpaul92@gmail.com
"""

import qr_assesment
import pytest
import os.path


def test_check_for_correct_arguments(capfd):
    """Test to check for incorrect arguments sent to the method
    Passes if the method exits on incorrect arguments
    """
    
    with pytest.raises(SystemExit) as e:
        qr_assesment.check_for_correct_arguments(3)
    out, err = capfd.readouterr()
    assert out == "Incorrect Arguments sent, Please check and execute the script again\n"
    assert e.type == SystemExit
    
def test_create_parts_dictionary_with_quantity():
    """Test to check if data sent to calculate the correct quantity of parts is returning the correct values
    Passes if the method returns the expected quantity value
    """
    
    mocked_data = [{'id': 0, 'parent_part_id': None, 'part_id': 2399, 'quantity': 1}, {'id': 1, 'parent_part_id': 2399, 'part_id': 2095, 'quantity': 4}, {'id': 2, 'parent_part_id': 2399, 'part_id': 4895, 'quantity': 1}, {'id': 3, 'parent_part_id': 2761, 'part_id': 1172, 'quantity': 1}, {'id': 4, 'parent_part_id': 2484, 'part_id': 2761, 'quantity': 4}, {'id': 5, 'parent_part_id': 2484, 'part_id': 3779, 'quantity': 3}, {'id': 6, 'parent_part_id': 2484, 'part_id': 1815, 'quantity': 1}, {'id': 7, 'parent_part_id': 3850, 'part_id': 1298, 'quantity': 2}, {'id': 8, 'parent_part_id': 2342, 'part_id': 2514, 'quantity': 5}, {'id': 9, 'parent_part_id': 679, 'part_id': 4865, 'quantity': 5}, {'id': 10, 'parent_part_id': 679, 'part_id': 2360, 'quantity': 1}, {'id': 11, 'parent_part_id': 2232, 'part_id': 2484, 'quantity': 1}, {'id': 12, 'parent_part_id': 4865, 'part_id': 3997, 'quantity': 1}, {'id': 13, 'parent_part_id': 4865, 'part_id': 3850, 'quantity': 5}, {'id': 14, 'parent_part_id': 939, 'part_id': 1826, 'quantity': 3}, {'id': 15, 'parent_part_id': 939, 'part_id': 807, 'quantity': 3}, {'id': 16, 'parent_part_id': 4895, 'part_id': 1051, 'quantity': 2}, {'id': 17, 'parent_part_id': 4895, 'part_id': 679, 'quantity': 2}, {'id': 18, 'parent_part_id': 2095, 'part_id': 3217, 'quantity': 1}, {'id': 19, 'parent_part_id': 3217, 'part_id': 3045, 'quantity': 3}, {'id': 20, 'parent_part_id': 807, 'part_id': 2771, 'quantity': 1}, {'id': 21, 'parent_part_id': 4998, 'part_id': 939, 'quantity': 3}, {'id': 22, 'parent_part_id': 2480, 'part_id': 2342, 'quantity': 3}, {'id': 23, 'parent_part_id': 2480, 'part_id': 2232, 'quantity': 4}, {'id': 24, 'parent_part_id': 1172, 'part_id': 3972, 'quantity': 2}, {'id': 25, 'parent_part_id': 1815, 'part_id': 1141, 'quantity': 2}, {'id': 26, 'parent_part_id': 1815, 'part_id': 4243, 'quantity': 2}, {'id': 27, 'parent_part_id': 1051, 'part_id': 1015, 'quantity': 5}, {'id': 28, 'parent_part_id': 3045, 'part_id': 4998, 'quantity': 5}, {'id': 29, 'parent_part_id': 2360, 'part_id': 2480, 'quantity': 3}]
    expected_quantity_value = {2399: 1, 2484: 12, 4895: 1, 3217: 4, 1172: 4, 1815: 4, 2360: 2, 679: 2, 1051: 2, 2342: 3, 939: 180, 807: 45, 2480: 6, 3045: 12, 2761: 4, 2232: 24, 2095: 4, 3850: 25, 4865: 5, 4998: 60, 1298: 50, 2514: 15, 2771: 45, 3972: 8, 4243: 8, 1015: 10}
    actual_quantity_dictionary = qr_assesment.create_parts_dictionary_with_quantity(mocked_data)
    assert expected_quantity_value == actual_quantity_dictionary

def test_write_and_save_to_excel():
    """Test to check if file is getting created with the name specified
    Passes if the file exists with the same file name
    """
    quantity_value = {2399: 1, 2484: 12, 4895: 1, 3217: 4, 1172: 4, 1815: 4, 2360: 2, 679: 2, 1051: 2, 2342: 3, 939: 180, 807: 45, 2480: 6, 3045: 12, 2761: 4, 2232: 24, 2095: 4, 3850: 25, 4865: 5, 4998: 60, 1298: 50, 2514: 15, 2771: 45, 3972: 8, 4243: 8, 1015: 10}
    file_name = "Test_File.xlsx"
    qr_assesment.write_and_save_to_excel(quantity_value,file_name)
    assert os.path.isfile('Test_file.xlsx')