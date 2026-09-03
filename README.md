# LeetCode SQL 50 — SQL → pandas → PySpark Muscle Memory

A five-day interview-prep drill built around the LeetCode Top SQL 50 study plan.

For every problem:

1. Read the requirement.
2. Type and run the provided SQL solution.
3. Type and run the pandas solution.
4. Type and run the PySpark solution.
5. Rebuild all three in the Muscle-Memory Round.

**First-pass rule:** no time limit. Repetition comes before speed.

## Training Order

The official SQL 50 notebook numbering is preserved, but the practice order is shuffled so every day progresses from easier to harder problems.

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

## Notebook Contract

Every notebook contains:

- Problem
- Setup / mock data
- SQL Solution
- pandas Solution
- PySpark Solution
- Pattern Mapping
- Muscle-Memory Round

## Runtime

### Databricks

Primary runtime. Spark and Spark SQL are already available.

### Google Colab

pandas runs directly. Install PySpark once if needed:

```python
!pip -q install pyspark
```

## Status

Repository scaffold created. Day 1 implementation is the first delivery batch.
