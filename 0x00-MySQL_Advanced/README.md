# MySQL Advanced

This project contains SQL scripts that perform various tasks on a MySQL 5.7 database running on Ubuntu 18.04 LTS. Each task is described in the SQL scripts with comments explaining what the script does.

## Tasks

1. **Task 8: Optimize Simple Search**
   - Created an index on the first letter of the `name` column to optimize search queries.

2. **Task 9: Optimize Search and Score**
   - Created a compound index on the first letter of the `name` and `score` columns.

3. **Task 10: Safe Divide**
   - Created a function `SafeDiv` that divides two numbers and returns 0 if the second number is 0.

4. **Task 11: No Table for a Meeting**
   - Created a view `need_meeting` to list students with scores below 80 and either no recent meeting or no meeting at all.
