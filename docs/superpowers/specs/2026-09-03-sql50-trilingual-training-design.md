# SQL 50 Trilingual Training — Design

Date: 2026-09-03  
Repository: `dui-w-moonrin/sql50-pandas-pyspark-muscle-memory`

## Goal

Turn the LeetCode SQL 50 study plan into a 5-day muscle-memory training system where every problem is solved in the same conceptual order:

1. SQL
2. pandas
3. PySpark

The first training pass is solution-first rather than quiz-first. Every notebook includes runnable mock data and complete solutions from the beginning so the learner can repeatedly type, run, compare, and rebuild the same data operation across all three technologies.

## Training Schedule

The official SQL 50 numbering and notebook filenames are preserved, but the **training order is shuffled** so that each day starts easier and gradually becomes harder.

### Day 1 — Foundation → Medium

1. 1757 Recyclable and Low Fat Products — Easy
2. 584 Find Customer Referee — Easy
3. 1683 Invalid Tweets — Easy
4. 1378 Replace Employee ID With The Unique Identifier — Easy
5. 620 Not Boring Movies — Easy
6. 1075 Project Employees I — Easy
7. 1729 Find Followers Count — Easy
8. 570 Managers with at Least 5 Direct Reports — Medium
9. 1193 Monthly Transactions I — Medium
10. 176 Second Highest Salary — Medium

### Day 2 — JOIN / GROUP BY / Conditional Logic

1. 595 Big Countries — Easy
2. 1148 Article Views I — Easy
3. 1068 Product Sales Analysis I — Easy
4. 577 Employee Bonus — Easy
5. 2356 Number of Unique Subjects Taught by Each Teacher — Easy
6. 610 Triangle Judgement — Easy
7. 1667 Fix Names in a Table — Easy
8. 1934 Confirmation Rate — Medium
9. 1070 Product Sales Analysis III — Medium
10. 626 Exchange Seats — Medium

### Day 3 — Relationship / Latest Record / Category Logic

1. 1581 Customer Who Visited but Did Not Make Any Transactions — Easy
2. 197 Rising Temperature — Easy
3. 1633 Percentage of Users Attended a Contest — Easy
4. 596 Classes More Than 5 Students — Easy
5. 1789 Primary Department for Each Employee — Easy
6. 1527 Patients With a Condition — Easy
7. 1174 Immediate Food Delivery II — Medium
8. 1907 Count Salary Categories — Medium
9. 602 Friend Requests II: Who Has the Most Friends — Medium
10. 1164 Product Price at a Given Date — Medium

### Day 4 — Aggregation / Window / Set Logic

1. 1661 Average Time of Process per Machine — Easy
2. 1280 Students and Examinations — Easy
3. 1211 Queries Quality and Percentage — Easy
4. 619 Biggest Single Number — Easy
5. 1978 Employees Whose Manager Left the Company — Easy
6. 1484 Group Sold Products By The Date — Easy
7. 550 Game Play Analysis IV — Medium
8. 1045 Customers Who Bought All Products — Medium
9. 180 Consecutive Numbers — Medium
10. 585 Investments in 2016 — Medium

### Day 5 — Advanced Interview Day

1. 1251 Average Selling Price — Easy
2. 1141 User Activity for the Past 30 Days I — Easy
3. 1731 The Number of Employees Which Report to Each Employee — Easy
4. 196 Delete Duplicate Emails — Easy
5. 1327 List the Products Ordered in a Period — Easy
6. 1517 Find Users With Valid E-Mails — Easy
7. 1204 Last Person to Fit in the Bus — Medium
8. 1341 Movie Rating — Medium
9. 1321 Restaurant Growth — Medium
10. 185 Department Top Three Salaries — Hard

| Day | Easy | Medium | Hard |
|---|---:|---:|---:|
| Day 1 | 7 | 3 | 0 |
| Day 2 | 7 | 3 | 0 |
| Day 3 | 6 | 4 | 0 |
| Day 4 | 6 | 4 | 0 |
| Day 5 | 6 | 3 | 1 |
| **Total** | **32** | **17** | **1** |

No initial time limit is imposed. The first pass prioritizes repetition and pattern recognition over speed. Notebook filenames keep the official SQL 50 sequence number even though training order is shuffled.

## Repository Strategy

Keep official SQL 50 sequence numbers and one notebook per problem. The README controls the shuffled five-day training order; notebook filenames are not renumbered to match training-day position.

## Notebook Standard

Every notebook follows the same structure:

### 0. Problem
- LeetCode number/title/link
- concise requirement
- expected output for the mock data

### 1. Setup
Create deterministic mock data. pandas setup is runnable without PySpark. A separate Spark setup cell creates PySpark DataFrame(s) and Spark SQL temporary view(s).

### 2. SQL Solution
Complete runnable SQL executed through Spark SQL temp views.

### 3. pandas Solution
Idiomatic pandas implementation of the same requirement.

### 4. PySpark Solution
PySpark DataFrame API solution using `pyspark.sql.functions as F`.

### 5. Pattern Mapping
Map the data concept across SQL, pandas, and PySpark.

### 6. Muscle-Memory Round
Provide three blank practice cells: SQL, pandas, and PySpark. Do not repeat solution code there.

## Naming Convention

```text
01_1757_Recyclable_and_Low_Fat_Products.ipynb
02_584_Find_Customer_Referee.ipynb
...
50_<leetcode-id>_<title>.ipynb
```

## Compatibility

### Databricks
Primary target. Spark and Spark SQL are available.

### Google Colab
pandas setup and pandas solutions run directly. PySpark sections can use `!pip -q install pyspark` when needed.

### SQL
Canonical executable SQL uses Spark SQL temp views; SQL statements remain interview-readable and standard wherever practical.

## Correctness Rules

1. SQL, pandas, and PySpark produce equivalent logical results.
2. Null semantics match the original problem intent.
3. Sorting is applied only when required or useful for deterministic demonstration.
4. Output column names match expected output.
5. Joins preserve intended cardinality.
6. Aggregation rounding/casting follows the problem.
7. Each notebook runs independently.

## Verification

Before a notebook is complete:
- `.ipynb` parses as valid JSON
- required sections exist
- pandas setup/solution is executable independently of PySpark
- no unresolved placeholders exist
- Muscle-Memory cells contain no hidden solution
- relevant null/join/duplicate/tie/date edge cases are represented

## Success Criteria

All 50 problems contain Setup + SQL + pandas + PySpark + Pattern Mapping + Muscle-Memory Round, and the learner can open any notebook in Colab or Databricks and immediately begin repetition practice.