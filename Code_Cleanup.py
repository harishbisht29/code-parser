'''
'''
import re
from collections import Counter

def get_clean_code(code):
    #regx to capture multi-line and single line comments
    regx= re.compile(r'(\/\*.*?\*\/)|(\#.*?\n)', re.IGNORECASE | re.DOTALL)
    comments= [c.group(0) for c in regx.finditer(code)]
    comment_stripped= re.sub(regx, "", code)
    clean_code= re.sub(re.compile("\s+"), " ", comment_stripped)
    clean_code= re.sub(re.compile(";"), ";\n", clean_code)
    print(clean_code)
    
    meta= [{
        'name':'sas_comment_count',
        'desc':'Total number of comments',
        'value':len(comments)
    },{
        'name':'sas_statment_count',
        'desc':'Total number of SAS statements',
        'value':len(clean_code.split('\n'))
    }]

    return (clean_code, meta)

#--------------------------------Testing----------------------------
if __name__ == '__main__':
    code = r'''
#This is a single line comment
#again same single line comment
%Global Flag;
/*
Sample Libname Statement
*/
Libname        test 'This is a test data';

Libname TDCDW teradata username="" password="";
/*
Sample Include Statement


*/
%Include "/user/bin/sas/sample_program.sas";
Filename input_file "/some/text/usr/bin/names.txt";
proc printo
 file="/usr/bin/name.log";
run;
/*Sample Data Step*/
Data _Null_;
    Value= "name";
Run;

Filename output_file "/some/text/usr/bin/names.csv";

/*Sample Proc Step
*/
Proc Sql;
    Create table test 
    as select * from test1 a inner join test2 b on a.name=b.name 
    left outer join test3 c on c.name=a.name 
    order by name;
Run;
Proc Sql;
    Create table test 
    as select * from test1 a inner join test2 b on a.name=b.name 
    left outer join test3 c on c.name=a.name 
    order by name;
Run;
%Macro Sum(a,b);
    %let b= &a+&b.;
%Mend;


/*------------------Input Format Test Cases----------
----*/
Proc import data="/usr/bin/local/text.csv" out=name.file;
quit;
Proc import data="/usr/bin/local/text.csv" out=name.file;
quit;
Proc import data="/usr/bin/local/text.xlsx" out=name.file;
quit;
Data None;
    Set lib1.dataset;
Run;

proc SQl;
    create tabale temp as
    select * from name.testdataset;
Run;


filename mydata "/usr/bin/local/scores.txt";
data test;
   infile mydata;
   input name $ score;
run;


/*------------------Output Format Test Cases--------------*/
Proc Export data="/user/bin/data.csv";
quit;

filename outchron '/user/bin/sas/name.txt';
Data test;
    file outchron;
    put name=;
Run;

proc sql;
    create 
    table libref.datatable1 as
    select * from datatable1;
quit;

ods tagsets.excelxp file="spacing.xls" style=statistical
      options( skip_space='3,2,0,0,1' sheet_interval='none'
               suppress_bylines='no');

  proc sort data=sashelp.class out=class;
     by age;
  run;

  proc print data=class;
     by age;
  run;

  ods tagsets.excelxp close;

proc 
printto;
quit;
'''
    get_clean_code(code)
