#import itertools
#import matplotlib.pyplot
# Code 1: Read files, set variables to use (input data/transactions, frequent itemsets, candidate itemsets, support counts, rules, confidence)

# Set variables to use
input_transactions = {}
freq_itemsets = []
cand_itemsets = []
supp_counts = []
rules = []
conf = 0.0

def read_input_file(input):
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            tran_id, item_id = map(int, line.strip().split())
            if tran_id not in input_transactions:
                input_transactions[tran_id] = []
            input_transactions[tran_id].append(item_id)
    file.close()
    return input_transactions

# The five parameters
minsuppc = 0.0
minconf = 0.0
input_file = ' '
output_file_name = ' '

# Code 2: Generate F1 (frequent 1-itemsets)
def generate_f1(input_transactions, minsuppc):
    temp_counts = {}
    f1_results = {}
    for itemset in input_transactions.values():
        for specific_item in itemset:
            if specific_item in temp_counts:
                temp_counts[specific_item] += 1
            else:
                temp_counts[specific_item] = 1
    
    itemsets_set = {}
    for item, supp in temp_counts.items():
        if supp >= minsuppc:
            itemsets_set.append(item)
            f1_results[item] = supp
    
    #return f1_results
    return itemsets_set

# What makes an itemset frequent? Its support is greather than or equal to the minsup
# Generate all itemsets whose support >= minsup
# Variables to use: supp_counts, 


# Code 3: Create functions to generate the output files and create examples of all the output files
def output_items_file(output_file_name, freq_itemsets):
    output_file_name = str(output_file_name) + '_items_G9.txt'
    with open(output_file_name, 'w') as file:
        for itemsets, supp in freq_itemsets.items():
            file.write(f"{itemsets}|{supp}\n")
    file.close()
        

#def output_rules_file(output_file_name):
#    output_file_name += '_rules_G9.txt'
#    with open(output_file_name, 'w') as file:
#        file.write(f"")
#    file.close()

#def output_info_file(output_file_name):
#    output_file_name += '_info_G9.txt'
#    with open(output_file_name, 'w') as file:
#        file.write(f"")
#    file.close()




# Code 4: Candidate Generation and Pruning for Frequent Itemset Generation
def cand_generation(prev_freq, k):
    temp_itemsets = {}
    # use cand_itemsets, supp_counts
    pass


def pruning():
    # use cand_itemsets, supp_counts
    pass

# Add function to plot Phase 2

# Code 5: Support Counting and Candidate Elimination for Frequent Itemset Generation (support counting=use itertools.combinations())
def supp_counting():
    # use supp_counts
    pass


def cand_elimination():
    # use cand_itemsets
    pass

# Phase2-Plot


# Code 6: Complete confident rule generation (no pruning is required)
def conf_rule_generation():
    # use rules
    pass


# Main function
if __name__=="__main__":
    input_file = read_input_file('C:\\Users\\jeffr\\Desktop\\CodePrograms\\PythonProjects\\small.txt') # Make this simpler???
    #print(input_file.values())
    freq_itemsets = generate_f1(input_file, minsuppc)
    print(freq_itemsets)
    output_items_file('test', freq_itemsets)
    