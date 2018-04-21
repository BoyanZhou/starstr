#!/usr/bin/python
# -*- coding: utf-8 -*-


def read_line_in_str(line, number_of_loci):
    """
    read str data in each line and check the format and data type (float);
    return information and STR-data separately.
    """

    col = line.strip().split("\t")

    # check the column number
    if len(col) != (number_of_loci + 6):
        print("\tTermination！Can not read the file because it has wrong column number at some line.")
        return

    # check if the str is numeric
    info_part = col[:6]
    str_part = []

    for i in col[6:]:
        try:
            str_part.append(float(i))

        except ValueError:
            print("\tTermination！There is a non-numeric value in the STR data.")
            return

    return info_part, str_part
