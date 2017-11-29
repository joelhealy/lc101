```sql
CREATE DATABASE _databasename_; 
```

```sql
DROP DATABASE _databasename_; 
```

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
); 
```

```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ....
);
```

The following constraints are commonly used in SQL:

    NOT NULL - Ensures that a column cannot have a NULL value
    UNIQUE - Ensures that all values in a column are different
    PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
    FOREIGN KEY - Uniquely identifies a row/record in another table
    CHECK - Ensures that all values in a column satisfies a specific condition
    DEFAULT - Sets a default value for a column when no value is specified
    INDEX - Used to create and retrieve data from the database very quickly


```sql
CREATE TABLE new_table_name AS
    SELECT column1, column2,...
    FROM existing_table_name
    WHERE ....; 
```

```sql
DROP TABLE table_name; 
```

```sql
TRUNCATE TABLE table_name; 
```

```sql
ALTER TABLE table_name
ADD column_name datatype; 
```

```sql
ALTER TABLE table_name
DROP COLUMN column_name; 
```

SQL Server / MS Access
```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype; 
```
My SQL
```sql
ALTER TABLE table_name
MODIFY COLUMN column_name datatype; 
```
Oracle
```sql
ALTER TABLE table_name
MODIFY column_name datatype;
```

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

```sql
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...); 
```

MS Access:
```sql
DROP INDEX index_name ON table_name;
```
SQL Server:
```sql
DROP INDEX table_name.index_name;
```
DB2/Oracle:
```sql
DROP INDEX index_name;
```
MySQL:
```sql
ALTER TABLE table_name
DROP INDEX index_name;
```

## SQL Date Data Types

MySQL comes with the following data types for storing a date or a date/time value in the database:

    DATE - format YYYY-MM-DD
    DATETIME - format: YYYY-MM-DD HH:MI:SS
    TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
    YEAR - format YYYY or YY


## SQL Views

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition; 
```

```sql
DROP VIEW view_name; 
```

