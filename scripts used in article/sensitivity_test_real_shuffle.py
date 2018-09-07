# permutation of real data to test whether the clustering result is affected by the order of haplotypes
import os
import random


for i in range(1, 11):
    origin_data = []
    with open("Y-STRs+database4_collapsed.txt", "r") as f1:
        for line in f1:
            origin_data.append(line)
    # index of each line
    shuffle_index = range(len(origin_data))
    random.shuffle(shuffle_index)

    # output shuffled files
    with open("Y-STRs+database_4_collapsed_shuffle%s.txt" % str(i), "w") as f2:
        for j in shuffle_index:
            f2.write(origin_data[j])

    # clustering
    os.system("starstr -i Y-STRs+database_4_collapsed_shuffle%s.txt -o EastAsia_clustering_step1_shuffle%s -t 10 -r "
              "0.00224,0.00293,0.00412,0.00211,0.00245,0.000519,0.00105,0.00122,0.000375,0.00545,"
              "0.00152,0.00429,0.00636,0.00433,0.00303 -s 20" % (str(i), str(i)))

