import sys

tree_file_name = sys.argv[3]
tree_file = open(tree_file_name, 'r')

branch_length_threshold = float(sys.argv[1])

tree_grouped_name = "simu_%s_grouped_by_nwk" % str(branch_length_threshold)
tree_grouped = open(tree_grouped_name, 'w')

individual_threshold = int(sys.argv[2])
group_no = 0
number_of_indi = 0
total_individual_number = 0
while tree_file:
    group_indi = []     # no of individual in this group/lineage
    group_no += 1       # record the number of group
    left_num = 0
    right_num = 0
    total_branch_length = 0
    while total_branch_length < branch_length_threshold:
        x = tree_file.read(1)
        # read until x is a digit
        while not x.isdigit():
            x = tree_file.read(1)

        # when x is a digit
        left_num += 1
        indi_no = x[:]
        x = tree_file.read(1)

        # get the first person id in the group/lineage
        while x.isdigit():
            indi_no += x
            x = tree_file.read(1)

        if x == ":":
            group_indi.append(indi_no)

            indi_branch = float(tree_file.read(5))
            if left_num > right_num:
                total_branch_length += indi_branch
            if total_branch_length >= branch_length_threshold:
                tree_grouped.write(str(group_no) + "\n")
                group_indi_str = ""
                for k in group_indi:
                    group_indi_str += str(k)
                    group_indi_str += ";"
                tree_grouped.write(group_indi_str + "\n")
                total_individual_number += len(group_indi)
                if total_individual_number >= individual_threshold:
                    exit()
                x = tree_file.read(1)

                if x == ",":
                    break

                while x != "(":
                    x = tree_file.read(1)
                break
        else:
            exit()

        while left_num > right_num:
            x = tree_file.read(1)
            if x == ",":
                continue
            if x == "(":
                left_num += 1
                continue
            if x == ")":
                right_num += 1
                if left_num > right_num:
                    continue
                else:
                    x = tree_file.read(1)   # this is a :
                    indi_branch = float(tree_file.read(5))
                    total_branch_length += indi_branch
                    if total_branch_length < branch_length_threshold:
                        x = tree_file.read(1)
                        if x != ")":
                            left_num += 1
                            continue
                        else:
                            pass

                    group_indi_str = ""
                    for k in group_indi:
                        group_indi_str += str(k)
                        group_indi_str += ";"
                    tree_grouped.write(str(group_no) + "\n")
                    tree_grouped.write(group_indi_str + "\n")
                    total_individual_number += len(group_indi)
                    if total_individual_number >= individual_threshold:
                        exit()
                    x = tree_file.read(1)
                    while x != "(":
                        x = tree_file.read(1)
                    total_branch_length += branch_length_threshold
                    break

            if x == ":":
                indi_branch = tree_file.read(5)
            if x.isdigit():
                indi_no = x[:]
                x = tree_file.read(1)
                while x.isdigit():
                    indi_no += x
                    x = tree_file.read(1)

                if x == ":":
                    group_indi.append(indi_no)
                    indi_branch = float(tree_file.read(5))

tree_file.close()
tree_grouped.close()


