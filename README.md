# Woolamaloo University

The famous Woolamaloo University is coming to town.
Their tradition will help improve the opportunities and cultural exchange in our region.
To accomplish this they need help with a synchronization system.
The data of all the employees are managed by one system.
All their web applications uses an authentication system that is based on the department and/or position to give or take permissions.

# The task

Your mission if you dare accept it, is to read the data exported from the employees system, compare against the data exported from the web auth system and generate a simple report.

# Employees system data specification

The employees system holds information of all employees including personal data, positions, department, payment, and more.
For this job only some information are useful, so the IT team provided a convenient simplified file.
The employees data file follows this standard:

```
id,name,admission_date,demission_date,department,position
```

Important, demission_date only have a value if the employee is not working on the University of Woolamaloo anymore.

Sample data:

```
id,name,admission_date,demission_date,department,position
1234,Aldo Zanchertine,13/11/1991,,Philosophy,Professor
4321,Rufus Parket,11/05/1996,14/01/2019,Transportation,Driver
```

# Web auth data specification

# Report specification

The report that could help University IT team is a synchronization system or even just a script that keep all information up to date in every system.
But, for now, it would be useful to have a report that shows what changed. Which employee was relocated to another department? Someone have a new position? There is any new employee? Someone is not working in the University anymore?

So, your task here is to compare both data and generate a report that must include:

  - All department relocations.
  - All positions chages.
  - All new employees.
  - All missing employees.

The suggested format follows, but you are free to choose the best format you think would be good.

```
Woolamaloo Synchronization Report
---------------------------------

ID   Name                Status
---- ------------------- ------------------------------------------------------------
1234 Aldo Zanchertine    Changed department, was Philosophy, now it is Mathematics.
4321 Rufus Parket        Worked with the Woolamaloo from 11/05/1996 until 14/01/2019.
```

# Requirements and instructions

  - Fork this project.
  - We would like you to use the Python programming language, by doing so you may get some extra points. But you can choose any language you want.
  - We need instructions on how to use the system or script, so document it.
  - Send your repository link to x@y.com
