import re
from types import resolve_bases
from extractors import Data_Step_Counts
from extractors import Proc_Step_Counts
from Code_Cleanup import get_clean_code
from pprint import pprint
import extractors

key_points_1= ['total_libname_count', 'total_join_count', 'log_exists', 'total_data_step','sas_comment_count', 
'sas_statment_count', 'include_stmt_count']

charts= {'proc_step_type_count':{'type':'bar', 'props':{'axis':'h'}},
'data_step_type_count':{'type':'pie', 'props':{}},
'join_type_count':{'type':'doughnut', 'props':{}}
}

def analyze_sas_program(loc):
    analysis= []
    with open(loc, "r") as f:
        code= f.read()
    clean_code, points= get_clean_code(code)
    analysis= analysis + points
    for e in extractors.extractors:
        a= e.extract(clean_code)
        analysis= analysis + a
    
    response= {}
    response['key_points_1']= []
    for a in analysis:
        if a['name'] in key_points_1:
            # print(a)
            response['key_points_1'].append(a)

    response['charts']= []
    for a in analysis:
        if a['name'] in charts.keys():
            # print(a)
            response['charts'].append(
                {
                    'id': a['name'],
                    'type':charts[a['name']]['type'],
                    'label': list(a['value'].keys()),
                    'values': list(a['value'].values()),
                    'desc':a['desc'],
                    'props': charts[a['name']]['props']
                }
            )
    return response

if __name__ == '__main__':
    path= r'C:\Codes\Source_Code_Analyzer\SAS_Programs\SAS_Program1.sas'
    response= analyze_sas_program(path)
    pprint(response)