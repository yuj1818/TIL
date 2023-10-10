CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('examples');

ALTER TABLE 
  examples
ADD COLUMN 
  Country VARCHAR(100) NOT NULL DEFAULT '';

ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL DEFAULT 0;

ALTER TABLE examples
ADD COLUMN Address VARCHAR(100) NOT NULL DEFAULT '';

ALTER TABLE
	examples
RENAME COLUMN
	Address TO PostCode;

CREATE TABLE backup_examples
AS SELECT * FROM examples;

CREATE TABLE new_examples
AS SELECT ExamId, LastName, FirstName, Country, Age FROM examples; 

DROP TABLE examples;

ALTER TABLE new_examples RENAME TO examples;

-- ALTER TABLE DROP COLUMN 작동하지 않기 때문에 위의 방법으로 대체
-- ALTER TABLE
-- 	examples
-- DROP COLUMN
-- 	PostCode;

ALTER TABLE
	examples
RENAME TO
	new_examples;

DROP TABLE new_examples;