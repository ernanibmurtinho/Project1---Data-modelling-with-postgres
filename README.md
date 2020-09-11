The purpose of this project is to load song datasets and model a fact and dimensional tables, to gain insigths about the data.

**The script create_tables, is responsible to execute the instructions inside the sql_queries, that contains:
1)
Drop tables
2)
Create Tables
3)
Insert tables
4)
Select Instruction, to populate the fact table

***The script etl.py is responsible to load the dimensional and fact tables.

****The script etl notebook, have the draft of the first load of the dimensional and fact tables load.

*****The folder data, contains all of the datasets.

## Instructions to run the project:

**To run the project, follow the steps below:

open the script Exec_scripts_model.ipynb

1) exec:
%run create_tables.py

2) exec:
%run etl.py