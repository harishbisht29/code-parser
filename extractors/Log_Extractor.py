'''
This module returns the frequency of differnt types of proc used in 
a sas program
'''

import re
from collections import Counter
from pprint import pprint

def extract(code):
    regx= re.compile("proc\s+printto", re.IGNORECASE)
    flag= 'True' if len(re.findall(regx, code)) > 0 else 'False'
    return [{
        'name':'log_exists',
        'desc':'Log Exists?',
        'value': flag}
        ]

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
    proc printto base= new;
    quit;
    '''
    pprint(extract(code))
