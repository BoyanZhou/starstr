#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


def calculate_d_stat(distance_data, individual_index):
    """
    calculate D_stat for each individual
    """
    d_ij = 1.0/(distance_data[:, 3] + 1.0)
    # record D_stat for each individual
    individual_d_stat = [0.0]*len(individual_index)    # D_stat of each individual

    for i in range(len(distance_data[:, 0])):
        index_temp = distance_data[i, 0]
        pos = individual_index.index(index_temp)
        individual_d_stat[pos] += d_ij[i]
        individual_d_stat = np.array(individual_d_stat)

    return individual_d_stat


def grouping(distance_data, individual_index, individual_D_stat):
    """
    give each individual a group number according its distance to others
    """
    group = np.array([0]*len(individual_index))    # store group number of each individual
    group_number_temp = 0
    for i in range(len(group)):
        if group[i] != 0:   # the individual has been grouped
            continue
        else:
            ID_1 = individual_index[i]             # the start person
            ID_in_chain = [ID_1]
            D_stat_1 = individual_D_stat[i]     # the start D
            ID_surround = distance_data[np.where(distance_data[:, 0] == ID_1), 1][0]
            D_stat_surround = individual_D_stat[[individual_index.index(k) for k in ID_surround]]
            # get surround ID and D_stat, then find the max
            max_pos = D_stat_surround.argmax()
            ID_2 = ID_surround[max_pos]
            D_stat_2 = D_stat_surround[max_pos]
            group_number_temp2 = group[individual_index.index(ID_2)]

            # when the D of tested one is smaller than surround ones and not grouped
            while D_stat_2 > D_stat_1 and group_number_temp2 == 0:
                ID_in_chain.append(ID_2)
                ID_1 = ID_2
                D_stat_1 = D_stat_2
                ID_surround = distance_data[np.where(distance_data[:, 0] == ID_1), 1][0]
                D_stat_surround = individual_D_stat[[individual_index.index(k) for k in ID_surround]]
                max_pos = D_stat_surround.argmax()
                ID_2 = ID_surround[max_pos]                             # max_D of surround individuals
                D_stat_2 = D_stat_surround[max_pos]
                group_number_temp2 = group[individual_index.index(ID_2)]

            ID_in_chain2 = set(ID_in_chain[:])
            for j in ID_in_chain:
                surround_j = distance_data[np.where(distance_data[:, 0] == j)]
                j_same = surround_j[np.where(surround_j[:, 3] == 0)][:, 1]
                ID_in_chain2 = ID_in_chain2 | set(j_same)
            ID_in_chain2 = list(ID_in_chain2)
            if D_stat_1 >= D_stat_2:
                group_number_temp += 1      # it is a new group
                group[[individual_index.index(k) for k in ID_in_chain2]] = group_number_temp
            else:
                group[[individual_index.index(k) for k in ID_in_chain2]] = group_number_temp2
    return group
