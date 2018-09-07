import sys
import numpy as np
A = int(sys.argv[2])    # start of the tree threshold
B = int(sys.argv[3])    # end of the tree threshold
N = int(sys.argv[1])    # repeat number now
threshold_list = [i/1000.0 for i in range(A, B)]

# compare cluster result with the nwk_tree
for i in threshold_list:
    branch_length_threshold = float(i)

    # read the file grouped by nwk
    group_divide_name = "simu_%s_grouped_by_nwk" % str(branch_length_threshold)
    group_divide = open(group_divide_name, "r")

    indi_divided = []
    line_num = 0
    indi_num = 0
    for line in group_divide:
        line_num += 1
        if (line_num % 2) == 0:
            indi_list = line.strip().split(";")
            indi_list.pop()
            indi_num += len(indi_list)
            indi_divided.append(indi_list)
    group_divide.close()

    # read the file of clustering result
    group_cluster_name = "simu%s_clustering.star_cluster_result.txt" % str(N)
    group_cluster = open(group_cluster_name, "r")   # cluster result by my method
    divide_evaluate_name = "simu%s_clustering_%s_evaluate.txt" % (str(N), str(branch_length_threshold))
    divide_evaluate = open(divide_evaluate_name, "w")

    n = 0
    for line2 in group_cluster:
        n += 1
        output = []
        col = line2.strip().split("\t")
        output.append(col[0])
        output.append(col[1])
        indi_list2 = col[2].split(";")
        if n == 1:
            output1 = "group\tindi_no\t"
            for j in range(1, (int(line_num/2))):
                output1 += str(j)
                output1 += "\t"
            output1 += str(line_num/2)
            divide_evaluate.write(output1 + "\n")

        for i in indi_divided:
            a = len(list(set(indi_list2).intersection(set(i))))
            output.append(str(a))
        divide_evaluate.write("\t".join(output) + "\n")

    group_cluster.close()
    divide_evaluate.close()


# summary results of comparison
method_evaluate_final_name = "simu%s_method_evaluate_final.txt" % str(N)
method_evaluate_final = open(method_evaluate_final_name, "w")
col_name_write = False

for i in threshold_list:
    branch_length_threshold = float(i)
    divide_evaluate_name = "simu%s_clustering_%s_evaluate.txt" % (str(N), str(branch_length_threshold))
    divide_evaluate = open(divide_evaluate_name, "r")
    group_divided_evaluation = []
    group_serial_number = []
    group_indi_number = []

    for line in divide_evaluate:
        col = line.strip().split("\t")
        group_divided_evaluation.append(col)

    group_divided_evaluation = np.array(group_divided_evaluation)   # the array of group divided
    nrow = int(group_divided_evaluation.shape[0])   # get the total number of row
    ncol = int(group_divided_evaluation.shape[1])   # get the total number of col

    # output the title line
    if not col_name_write:
        group_serial_number = group_divided_evaluation[1:, 0]
        group_serial_number_2 = []
        for q in group_serial_number:
            group_serial_number_2.append(q)
            group_serial_number_2.append(q)

        group_indi_number = group_divided_evaluation[1:, 1]
        group_indi_number_2 = []
        for q in group_indi_number:
            group_indi_number_2.append(q)
            group_indi_number_2.append(q)

        method_evaluate_final.write("\t".join(group_serial_number_2) + "\n")
        method_evaluate_final.write("\t".join(group_indi_number_2) + "\n")
        col_name_write = True

    line_rate = []
    for j in range(1, nrow):
        row_data = group_divided_evaluation[j, 2:]
        row_data = [float(k) for k in row_data]
        row_data_max = max(row_data)    # get the max value in the row (clustering result by my method)
        row_data_pos = row_data.index(row_data_max)     # get the position of max value
        row_data_rate = "%.4f" % (row_data_max/sum(row_data))      # inclusion rate in the row

        col_data = group_divided_evaluation[1:, row_data_pos + 2]
        col_data = [float(k) for k in col_data]
        col_data_max = max(col_data)    # get the max value in the col (clustering result by my method)
        col_data_pos = col_data.index(col_data_max)     # get the position of max value
        col_data_rate = "%.4f" % (col_data_max/sum(col_data))      # inclusion rate in the col

        line_rate.append(row_data_rate)
        line_rate.append(col_data_rate)

    method_evaluate_final.write("\t".join(line_rate) + "\n")
    divide_evaluate.close()
method_evaluate_final.close()
