import numpy as np
import random
import sys

random.seed(int(sys.argv[5]))


def mutation_direction():
    a = random.uniform(0, 1)
    if a <= 0.5:
        return 1
    else:
        return -1


# get the origin haplotype
haplotype_origin = sys.argv[3]
haplotype_origin = haplotype_origin.split(",")
haplotype_origin = [int(i) for i in haplotype_origin]
haplotype_origin = np.array(haplotype_origin)

# get the mutation rate
rate_pergeneration = sys.argv[4]
rate_pergeneration = rate_pergeneration.split(",")
rate_pergeneration = [float(j) for j in rate_pergeneration]
rate_pergeneration = np.array(rate_pergeneration)

# get the number of STR loci
number_of_loci = len(haplotype_origin)

mutation_STR = []   # mutation of STR, 1 or -1
STR_total_sites = 0
STR_assigned_num = [0] * number_of_loci  # number of mutations assigned to each STR
STR_each_start = []
STR_each_end = []

filename = sys.argv[1]
filename2 = sys.argv[2]

simu1 = open(filename, 'r')
simu_STR = open(filename2, 'w')
start = False
n = 0
# prop_STR = 360.0/5160.0
# prop_SNP = 1 - prop_STR
STR_length_chr = rate_pergeneration/sum(rate_pergeneration)
# length of each STR in 0-1 scale chr
STR_end_pos = []
for i in range(0, (number_of_loci - 1)):
    STR_end_pos.append(sum(STR_length_chr[: i + 1]))
STR_end_pos.append(1)                    # end position for each STR

for line in simu1:
    if not start:
        if line[0:3] == "seg":
            site_num = line.strip().split(" ")[1]   # get total positions number
        if line[0:3] == "pos":
            pos = line.strip().split(" ")[1:]   # mutation position
            STR_ranked = 0                         # the ranked STR
            for i in pos:
                if float(i) <= STR_end_pos[STR_ranked]:
                    STR_assigned_num[STR_ranked] += 1   # mutation sites of this STR add 1
                    mutation_STR.append(mutation_direction())   # decide the direction of STR mutation

                else:
                    STR_ranked_0 = 0
                    for j in range(len(STR_end_pos)):
                        if float(i) > STR_end_pos[j]:
                            STR_ranked_0 += 1
                        else:
                            break
                    STR_ranked = STR_ranked_0
                    STR_assigned_num[STR_ranked] += 1   # mutation sites of this STR add 1
                    mutation_STR.append(mutation_direction())   # decide the direction of STR mutation

            start = True
            mutation_STR = np.array(mutation_STR)               # direction of mutation
            STR_total_sites = sum(STR_assigned_num)

            for k in range(len(STR_assigned_num)):
                STR_each_start.append(sum(STR_assigned_num[: k]))
                STR_each_end.append(sum(STR_assigned_num[:k + 1]))

    else:
        indi1 = line.strip()
        STR_string = list(indi1[:STR_total_sites])
        STR_mutation = np.array(map(int, STR_string))
        STR_mutation_directed = STR_mutation * mutation_STR
        STR_step = []
        for i, j in zip(STR_each_start, STR_each_end):
            STR_step.append(sum(STR_mutation_directed[i: j]))

        haplotype_indi1 = np.array(STR_step) + haplotype_origin
        haplotype_output = ""
        for i in haplotype_indi1:
            haplotype_output += str(i)
            haplotype_output += "\t"
        haplotype_output = haplotype_output.rstrip("\t")
        haplotype_output = "0\t0\t0\t0\t0\t0\t" + haplotype_output  # add the first 6 columns
        simu_STR.write(haplotype_output + "\n")

simu1.close()
simu_STR.close()
