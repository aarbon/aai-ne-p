import os
import sys
import random

fl = sys.stdin
sepr = '#'
fl_con = fl.readlines()

num_code_lines = 0
comment_lines = [];

for index,row in enumerate(fl_con):
    if sepr in row:
        comment_lines.append([row.find(sepr), index])
    else:
        if len(row.strip())>0:
            num_code_lines+=1;

num_comment_lines = len(comment_lines);
num_comment_lines_to_remove = max(0, num_comment_lines-(2*num_code_lines))
kill_me = random.sample(comment_lines,num_comment_lines_to_remove);

for column_index ,row_index in kill_me:
    fl_con[row_index] = row[row_index][column_index:] 
    fl_con[row_index] += "\n"
    

for row in fl_con:
    sys.stdout.write(row)

sys.stderr.write("%d code lines\n"%num_code_lines)
sys.stderr.write("%d comment lines \n"%num_comment_lines)
sys.stderr.write("%d lines removed\n"%len(kill_me))

