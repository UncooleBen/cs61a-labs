.read sp19data.sql

-- Q2
CREATE TABLE obedience AS
  SELECT a.seven, b.animal
  FROM students AS a, students AS b
  WHERE a.time = b.time;

-- Q3
CREATE TABLE smallest_int AS
  SELECT a.time, b.smallest
  FROM students AS a, students AS b
  WHERE a.time = b.time and b.smallest > 2
  ORDER BY b.smallest ASC
  LIMIT 20;

-- Q4
CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
  FROM students AS a, students AS b
  WHERE a.pet = b.pet and
        a.song = b.song and
	a.time < b.time;
