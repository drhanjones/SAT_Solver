import random


#def read_sudoku(filepath=None):

sudoku_size = 4
filepath =None

if filepath:
    pass

else:
    print("random sudoku")

    with open("testcases/{0}x{0}.txt".format(sudoku_size)) as f:
        sudoku_list = f.readlines()

print(sudoku_list[0])

rules_path = 'rules/sudoku-rules-{0}x{0}.txt'.format(sudoku_size)
#%%
"""
with open(rules_path) as f:
    default_sudoku_rules_string = f.read()
    

cnf_config = default_sudoku_rules_string.split('\n')[0]

cnf_clauses_str = default_sudoku_rules_string.split('\n',1)[1]

cnf_clauses_list = cnf_clauses_str.replace("\n", ' ').split('0')[:-1]

cnf_clauses_list = [ x.strip().split(' ') for x in cnf_clauses_list]

"""
#%%



test_sudoku = sudoku_list[0]
sudoku_dict = {str(i):{str(j): test_sudoku[(i-1)*sudoku_size+j-1] for j in range(1,sudoku_size+1)} for i in range(1,sudoku_size+1)} 


def sudoku_dict_to_cnf(s_dict):

    p_clauses = []
    
    for i in range(1,sudoku_size+1):
        for j in range(1,sudoku_size+1):
            cell_val_t = s_dict[str(i)][str(j)] 
            if cell_val_t != '.':
                p_clauses.append([str(i)+str(j)+cell_val_t])

    return p_clauses

puzzle_clauses = sudoku_dict_to_cnf(sudoku_dict)

#%% 

from sat_funcs import *


variables_n, clause_n, rules_clauses = read_file(rules_path)

clauses = rules_clauses + puzzle_clauses

DPLL(clauses)
