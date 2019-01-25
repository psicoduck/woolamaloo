# Woolamaloo University

The famous Woolamaloo University is coming to town.
Their tradition will help improve the opportunities and cultural exchange in our region.
To accomplish this they need help with a synchronization system.
The data of all the employees is managed by one system.
All their web applications use an authentication system that is based on the department and/or position to give or take permissions.

## The task

Your mission, if you dare accept it, is to read the data exported from the employees system, compare against the data exported from the web auth system and generate a simple report.

## Employees system data specification

The employees system holds information of all employees including personal data, positions, department, payment, and more.
For this job only some information is useful, so the IT team provided a convenient simplified file that follows this standard:

```csv
id,name,admission_date,demission_date,department,position
```

Each line contains data for one employee and the first line is a header.  
Important: `demission_date` only has a value if the employee is not working on the University of Woolamaloo anymore.

Sample data:

```csv
id,name,admission_date,demission_date,department,position
1234,Aldo Zanchertine,13/11/1991,,Mathematics,Professor
4321,Rufus Parket,11/05/1996,14/01/2019,Transportation,Driver
```

## Web auth data specification

The web auth data you can use is a simplification from what you could would from a query to a LDAP database. Our IT team already created a script that transforms the LDAP export format to a csv format to make it easier to compare. The University will use the report you will provide to update the authentication data.

```csv
cn,employeeNumber,mail,uid,department,position
Aldo Zanchertine,1234,aldo.zanchertine@woolamaloo.mon.ty.py,aldo.zanchertine,Philosophy,Professor
Rufus Parket,4321,rufus.parket@woolamaloo.mon.ty.py,rufus.parket,Transportation,Driver
```

## Report specification

The report that could help University IT team is a synchronization system or even just a script that keep all information up to date in every system.
But, for now, it would be useful to have a report that shows what changed. Which employee was relocated to another department? Someone has a new position? Is there any new employee? Someone is not working in the University anymore?

So, your task here is to compare both datas and generate a report that must include:

  - All department relocations.
  - All positions changes.
  - All new employees.
  - All missing employees.

The suggested format follows, but you are free to choose the format you think would be best.

```
Woolamaloo Synchronization Report
---------------------------------

ID   Name                Status
---- ------------------- ------------------------------------------------------------
1234 Aldo Zanchertine    Changed department, was Philosophy, now it is Mathematics.
4321 Rufus Parket        Worked with the Woolamaloo from 11/05/1996 until 14/01/2019.
```

## Requirements and instructions

  - Fork this project.
  - We would like you to use the Python programming language, by doing so you may get some extra points. But you may choose any language you want.
  - We need instructions on how to use the system or script, so document it.
  - Send your repository link to woolamaloo@cmc.pr.gov.br

## Recommendations

  * It is not required at all, but we would like to see some tests (if you know how to do it, otherwise don't UAIste your time!);  
  Seriously, if you don't know how to test yet, you might learn here.
  * Practice the [12 Factor-App](http://12factor.net) concepts;
  * Use [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design))
  design principles;
  * Use good programming practices (for example, you could write your entire code in one line, but if you do we won't even look at it);
  * Use [git's best practices](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices),
    with clear messages (written in English);

  **Have fun!**

## Disclaimer

**ATTENTION**, this is a fictional repository we use to assess interns knowledge before hiring them.
It's name is a reference from a [Monty Python Sketch](https://en.wikipedia.org/wiki/Bruces_sketch).

## Credits

We were inspired by the Work at the [Olist repository](https://github.com/olist/work-at-olist).
