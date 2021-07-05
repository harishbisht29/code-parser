'''
This module returns the frequency of differnt types of data steps used in 
a sas program- 
_Null_ - 
Work -
External - 
'''

import re
from collections import Counter
from pprint import pprint


def extract(code):
    regx= re.compile(r'\s*data\s+(\w+)(\.\w+)?', re.IGNORECASE)
    matches= regx.finditer(code)
    dataset_type= []
    total_data_steps= 0
    for m in matches:
        type= "_Null_" if m.group(1).lower() == "_null_" else \
            "Work" if m.group(1).lower() == "work" or m.group(2) is None else \
                "External" 
        dataset_type.append(type)
        total_data_steps+= 1

    dataset_type_counts= Counter(dataset_type)
    return [{
        'name':'total_data_step',
        'desc':'Total number of Data steps',
        'value': total_data_steps},
        {
        'name': 'data_step_type_count',
        'desc': 'Count of differnt type of datasets',
        'value': dataset_type_counts
        }]

#--------------------------------Testing----------------------------
if __name__ == '__main__':
    code = r'''
Data _Null_;
    set nothing;
Run;
Data cs.Play;
    if name=="cs" then do;
    play=1;
    end;
Run;
Data _Null_;
    set nothing;
Run;
Data Work.Play;
set cs.Play;
Run;
Data cs.Hello;
    if name=="cs" then do;
    play=1;
    end;
Run;
'''
    pprint(extract(code))