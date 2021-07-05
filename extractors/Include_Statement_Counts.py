'''
This module returns the frequency of differnt types of proc used in 
a sas program
'''

import re
from collections import Counter
from pprint import pprint

def extract(code):
    regx= re.compile(r'\s*%include\s+', re.IGNORECASE)
    matches= regx.finditer(code)
    count= len([m for m in matches])
    return [{
        'name':'include_stmt_count',
        'desc':'Total number external sas programs used',
        'value': count}
        ]

#--------------------------------Testing----------------------------
if __name__ == '__main__':
    code = r'''
  %include '/usr/bin/harish.txt';
  %include '/usr/bin/harish.txt';

  %include '/usr/bin/harish.txt';

    '''
    pprint(extract(code))
