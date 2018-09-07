import sys
import numpy as np

result_name = "simu%s_method_evaluate_final.txt" % sys.argv[1]

total_result_summary = open(sys.argv[2], "a")
result = open(result_name, "r")
result_array = []
for line in result:
    col = line.strip().split("\t")
    result_array.append(col)

result.close()
result_array = np.array(result_array, dtype=np.float)
nrow = int(result_array.shape[0])
ncol = int(result_array.shape[1])
list_odd = np.array(range(ncol/2))*2
list_even = list_odd + 1
data_odd = result_array[2:nrow, list_odd]
data_even = result_array[2:nrow, list_even]
dataset = data_odd + data_even
data_max = dataset[dataset.argmax(axis=0), range(dataset.shape[1])]
data_max = [str(i) for i in data_max]
group_num = result_array[1, list_odd]
group_num = [str(i) for i in group_num]

total_result_summary.write("\t".join(group_num) + "\n")
total_result_summary.write("\t".join(data_max) + "\n")
total_result_summary.close()