This is a program that through Python can interpret files in CSV, using SQLite commands in the terminal you can also manipulate

## Prerequisites
- Python 3 installed
- SQLite3 database installed
- CSV file "Salary_dataset.csv" in the same directory as the script

## Instructions
1. Clone or download this repository
2. Make sure you have SQLite3 installed on your machine (run `sqlite3` in terminal to check)
3. Open the terminal and navigate to the directory where the script is located
4. Create the database with the `sqlite3 salary.db` command
5. Run the script with the command `python index.py`


## to rotate

To run the program in Python and see the entire database, just run it in the terminal

```bash
    python3 salary.py
```

To execute in SQLite and be able to handle it and have more visualization options, execute it in the terminal

```bash
    sqlite3 salary.db
```
```sql
    sqlite> .import filename.csv tablename
```

In our case we will put

```sql
sqlite> .import social.csv social
```
To see the contents of the table, run

```sql
sqlite> .shema
```

Repeat this process for each of the three CSV files. You will then be able to view the created tables with the following command:

```sql
sqlite> SELECT * FROM salary;
```

## Library used
- CSV: to read data from CSV file
- SQLite3: to store and manipulate the data

## Thanks
Thanks for using this script! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.



<br>

<div>
        
    <a href="https://www.instagram.com/devbrunoo/" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for -the-badge&logo=instagram&logoColor=white" target="_blank"></a>
     <a href="https://medium.com/@devbrunoo" target="_blank"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo =medium&logoColor=white" target="_blank"></a>
     <a href="https://www.quora.com/profile/DevBrunoo" target="_blank"><img src="https://img.shields.io/badge/Quora-%23B92B27.svg?&style =for-the-badge&logo=Quora&logoColor=white" target="_blank"></a>
    <a href="https://codepen.io/brunobyhow15" target="_blank"><img src="https://img.shields.io/badge/Codepen-000000?style=for-the-badge&logo= codepen&logoColor=white" target="_blank"></a>
     <a href="mailto:contactbruno5@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target ="_blank"></a>
     <a href="https://www.linkedin.com/in/devbruono/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style =for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  
   
   </div>

<div>
<br>
<hr>
   <br>
</div>