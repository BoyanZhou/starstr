#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

seed = "123456"
origin_haplotype = "15,13,20,25,10,12,13,16,11,12,19,17,18,23,12"
rate_pergeneration = "0.00224,0.00293,0.00412,0.00211,0.00245,0.000519,0.00105,0.00122," \
                     "0.000375,0.00545,0.00152,0.00429,0.00636,0.00433,0.00303"


def remove_temporary_files(model, number):
    os.remove("model_%s.simu%s.nwk" % (model, str(number)))
    os.remove("model_%s.simu%s_ms" % (model, str(number)))
    os.remove("model_%s.simu%s_str" % (model, str(number)))
    os.remove("model_%s.simu%s_str.pure_data.txt" % (model, str(number)))
    os.remove("simu%s_clustering_distance.txt" % str(number))
    threshold_list = [q/1000.0 for q in range(1, 21)]
    for m in threshold_list:
        os.remove("simu%s_clustering_%s_evaluate.txt" % (str(number), str(float(m))))

# model_a


def simu_a(i):
    # simulation by ms
    ms_command = "ms 30000 1 -T -t 360 -G 179.18 -eG 0.01 0.0 -eN 0.0167 0.4167 -seeds %s %s %s > model_a.simu%s_ms" % \
                 (str(i), str(i), str(i), str(i))
    os.system(ms_command)

    # get nwk_tree
    get_nwk = "cat model_a.simu%s_ms | sed -n '5p' > model_a.simu%s.nwk" % (str(i), str(i))
    os.system(get_nwk)

    # convert ms_data to the input of STAR_str
    convert_command = "python convert_ms_to_str.py model_a.simu%s_ms model_a.simu%s_str %s %s %s" % \
                      (str(i), str(i), origin_haplotype, rate_pergeneration, seed)
    os.system(convert_command)

    # clustering by STAR_STR
    star_str_command = "python STAR_STR.py -i model_a.simu%s_str -o simu%s_clustering -t 15 -r %s -s 300" % \
                       (str(i), str(i), rate_pergeneration)
    os.system(star_str_command)

    # divide according to nwk_tree (golden standard)
    threshold_list = [j/1000.0 for j in range(1, 21)]
    name = "model_a.simu%s.nwk" % str(i)
    for j in threshold_list:
        divide_nwk_tree = "python divide_nwk_tree.py %s %s %s" % (str(j), "30000", name)
        os.system(divide_nwk_tree)

    # evaluate clustering result
    clustering_evaluation = "python clustering_evaluation.py %s %s %s" % (str(i), "1", "21")
    os.system(clustering_evaluation)

    # result summary
    result_summary = "python result_summary.py %s %s" % (str(i), "model_a.simu.final_result.txt")
    os.system(result_summary)

    # delete temporary files
    remove_temporary_files("a", i)

for f in range(1, 51):
    simu_a(f)

# model_b


def simu_b(i):
    # simulation by ms
    ms_command = "ms 30000 1 -T -t 360 -seeds %s %s %s > model_b.simu%s_ms" % \
                 (str(i), str(i), str(i), str(i))
    os.system(ms_command)

    # get nwk_tree
    get_nwk = "cat model_b.simu%s_ms | sed -n '5p' > model_b.simu%s.nwk" % (str(i), str(i))
    os.system(get_nwk)

    # convert ms_data to the input of STAR_str
    convert_command = "python convert_ms_to_str.py model_b.simu%s_ms model_b.simu%s_str %s %s %s" % \
                      (str(i), str(i), origin_haplotype, rate_pergeneration, seed)
    os.system(convert_command)

    # clustering by STAR_STR
    star_str_command = "python STAR_STR.py -i model_b.simu%s_str -o simu%s_clustering -t 15 -r %s -s 300" % \
                       (str(i), str(i), rate_pergeneration)
    os.system(star_str_command)

    # divide according to nwk_tree (golden standard)
    threshold_list = [j/1000.0 for j in range(1, 21)]
    name = "model_b.simu%s.nwk" % str(i)
    for j in threshold_list:
        divide_nwk_tree = "python divide_nwk_tree.py %s %s %s" % (str(j), "30000", name)
        os.system(divide_nwk_tree)

    # evaluate clustering result
    clustering_evaluation = "python clustering_evaluation.py %s %s %s" % (str(i), "1", "21")
    os.system(clustering_evaluation)

    # result summary
    result_summary = "python result_summary.py %s %s" % (str(i), "model_b.simu.final_result.txt")
    os.system(result_summary)

    # delete temporary files
    remove_temporary_files("b", i)

for f in range(1, 51):
    simu_b(f)

# model_c


def simu_c(i):
    # simulation by ms
    ms_command = "ms 30000 1 -T -t 360 -G 52.53 -eG 0.0167 0.0 -seeds %s %s %s > model_c.simu%s_ms" % \
                 (str(i), str(i), str(i), str(i))
    os.system(ms_command)

    # get nwk_tree
    get_nwk = "cat model_c.simu%s_ms | sed -n '5p' > model_c.simu%s.nwk" % (str(i), str(i))
    os.system(get_nwk)

    # convert ms_data to the input of STAR_str
    convert_command = "python convert_ms_to_str.py model_c.simu%s_ms model_c.simu%s_str %s %s %s" % \
                      (str(i), str(i), origin_haplotype, rate_pergeneration, seed)
    os.system(convert_command)

    # clustering by STAR_STR
    star_str_command = "python STAR_STR.py -i model_c.simu%s_str -o simu%s_clustering -t 15 -r %s -s 300" % \
                       (str(i), str(i), rate_pergeneration)
    os.system(star_str_command)

    # divide according to nwk_tree (golden standard)
    threshold_list = [j/1000.0 for j in range(1, 21)]
    name = "model_c.simu%s.nwk" % str(i)
    for j in threshold_list:
        divide_nwk_tree = "python divide_nwk_tree.py %s %s %s" % (str(j), "30000", name)
        os.system(divide_nwk_tree)

    # evaluate clustering result
    clustering_evaluation = "python clustering_evaluation.py %s %s %s" % (str(i), "1", "21")
    os.system(clustering_evaluation)

    # result summary
    result_summary = "python result_summary.py %s %s" % (str(i), "model_c.simu.final_result.txt")
    os.system(result_summary)

    # delete temporary files
    remove_temporary_files("c", i)

for f in range(1, 51):
    simu_c(f)


origin_haplotype2 = "15,13,20,25,10,12,13,12"
rate_pergeneration2 = "0.00224,0.00293,0.00412,0.00211,0.00245,0.000519,0.00105,0.00545"


def simu_a_8sites(i):
    # simulation by ms
    ms_command = "ms 30000 1 -T -t 192 -G 179.18 -eG 0.01 0.0 -eN 0.0167 0.4167 -seeds %s %s %s > model_a.simu%s_ms" % \
                 (str(i), str(i), str(i), str(i))
    os.system(ms_command)

    # get nwk_tree
    get_nwk = "cat model_a.simu%s_ms | sed -n '5p' > model_a.simu%s.nwk" % (str(i), str(i))
    os.system(get_nwk)

    # convert ms_data to the input of STAR_str
    convert_command = "python convert_ms_to_str.py model_a.simu%s_ms model_a.simu%s_str %s %s %s" % \
                      (str(i), str(i), origin_haplotype2, rate_pergeneration2, seed)
    os.system(convert_command)

    # clustering by STAR_STR
    star_str_command = "python STAR_STR.py -i model_a.simu%s_str -o simu%s_clustering -t 15 -r %s -s 300" % \
                       (str(i), str(i), rate_pergeneration2)
    os.system(star_str_command)

    # divide according to nwk_tree (golden standard)
    threshold_list = [j/1000.0 for j in range(1, 21)]
    name = "model_a.simu%s.nwk" % str(i)
    for j in threshold_list:
        divide_nwk_tree = "python divide_nwk_tree.py %s %s %s" % (str(j), "30000", name)
        os.system(divide_nwk_tree)

    # evaluate clustering result
    clustering_evaluation = "python clustering_evaluation.py %s %s %s" % (str(i), "1", "21")
    os.system(clustering_evaluation)

    # result summary
    result_summary = "python result_summary.py %s %s" % (str(i), "model_a_8sites.simu.final_result.txt")
    os.system(result_summary)

    # delete temporary files
    remove_temporary_files("a", i)

for f in range(1, 51):
    simu_a_8sites(f)
