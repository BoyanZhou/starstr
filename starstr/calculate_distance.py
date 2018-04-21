#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import parseoptions
import os


def compute_start_end(dataset_str, thread):
    """
    calculate start and end points for multi_threading
    """
    individuals_number = dataset_str.shape[0]
    number_each_thread = int(individuals_number/thread)
    start = [number_each_thread * i for i in range(thread)]
    end = start[1:]
    end.append(individuals_number)
    return start, end


def calculate(thread_number):
    options = parseoptions.options_parsed()
    # read the pure str data
    pure_data = np.loadtxt(options.filename + ".pure_data.txt", delimiter="\t")
    start_point, end_point = compute_start_end(pure_data, options.thread)
    a = start_point[thread_number]
    b = end_point[thread_number]
    suf = str(thread_number)
    output_temp_file = open(options.output_suffix + ".distance" + suf, "w")

    individuals_number = pure_data.shape[0]

    # calculate threshold step/year
    rate_per_generation = np.array(options.rate)
    threshold_step = options.step
    year_per_step = 1.0/rate_per_generation*25.0
    year_per_step_normalized = year_per_step/min(year_per_step)
    if options.years:
        threshold_year = np.median(year_per_step_normalized)
    else:
        threshold_year = 0

    # main loop
    for i in range(a, b):
        # for each individual i
        str_i = pure_data[i]

        for j in range(individuals_number):
            if i == j:
                continue
            str_j = pure_data[j]
            # the distance to j, measured by step/year
            distance_step_vector = abs(str_i - str_j)
            distance_step = sum(distance_step_vector)
            distance_year_normalized = sum(distance_step_vector * year_per_step_normalized)

            # if the distance less than one of thresholds, output the connection
            if distance_step <= threshold_step or distance_year_normalized <= threshold_year:
                output_line = "%s\t%s\t%s\t%s\n" % \
                              (str(i), str(j), str(distance_step), str(distance_year_normalized))
                output_temp_file.write(output_line)
    output_temp_file.close()


def combine_distance(suffix, thread):
    distance_file_combined = open(suffix + "_distance.txt", "w")
    for i in list(range(thread)):
        distance_file = open(suffix + ".distance" + str(i), "r")
        for line in distance_file:
            distance_file_combined.write(line)
        distance_file.close()
        os.remove(suffix + ".distance" + str(i))
    distance_file_combined.close()
