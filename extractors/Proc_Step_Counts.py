'''
This module returns the frequency of differnt types of proc used in 
a sas program
'''

import re
from collections import Counter
from pprint import pprint

def extract(code):
    regx= re.compile(r'\s*proc\s+(\w+)', re.IGNORECASE)
    matches= regx.finditer(code)
    proc_names= [m.group(1).capitalize() for m in matches]
    total_proc_step= len(proc_names)
    proc_type_counts= Counter(proc_names)
    return [{
        'name':'total_proc_step',
        'desc':'Total number of Proc steps',
        'value': total_proc_step},
        {
        'name': 'proc_step_type_count',
        'desc': 'Count of differnt type of Proc Steps',
        'value': proc_type_counts
        }]

#--------------------------------Testing----------------------------
if __name__ == '__main__':
    code = r'''
    proc append base= new;
    quit;    
    proc sql;
        select * from table1;
    quit;
    proc frequency;
        by namespace;
    run;
    proc append base= new;
    quit;
    '''
    pprint(extract(code))
