# LeetCode SQL 50 — SQL → pandas → PySpark Muscle Memory

A five-day interview-prep drill built around the LeetCode Top SQL 50 study plan.

For every problem:

1. Read the requirement and inspect the mock data.
2. Type and run the complete SQL solution.
3. Type and run the pandas solution.
4. Type and run the PySpark DataFrame API solution.
5. Compare the Pattern Mapping.
6. Scroll to Muscle-Memory Round and rebuild all three without copying.

**First-pass rule:** no time limit. Repetition comes before speed.

## Why the order is shuffled

Notebook filenames preserve the official SQL 50 sequence (`01`–`50`), but the training order is shuffled so every day progresses from Easy toward Medium/Hard. This prevents advanced problems from piling up only at the end.

Difficulty distribution: **32 Easy / 17 Medium / 1 Hard**.

## Five-Day Checklist

### Day 1 — Foundation → Medium

- [ ] **SQL50 #01 · LC 1757 · Easy** — [Recyclable and Low Fat Products](1_Select/01_1757_Recyclable_and_Low_Fat_Products.ipynb)
- [ ] **SQL50 #02 · LC 584 · Easy** — [Find Customer Referee](1_Select/02_584_Find_Customer_Referee.ipynb)
- [ ] **SQL50 #05 · LC 1683 · Easy** — [Invalid Tweets](1_Select/05_1683_Invalid_Tweets.ipynb)
- [ ] **SQL50 #06 · LC 1378 · Easy** — [Replace Employee ID With The Unique Identifier](2_basic_joins/06_1378_Replace_Employee_ID_With_The_Unique_Identifier.ipynb)
- [ ] **SQL50 #15 · LC 620 · Easy** — [Not Boring Movies](3_basic_aggregate_functions/15_620_Not_Boring_Movies.ipynb)
- [ ] **SQL50 #17 · LC 1075 · Easy** — [Project Employees I](3_basic_aggregate_functions/17_1075_Project_Employees_I.ipynb)
- [ ] **SQL50 #27 · LC 1729 · Easy** — [Find Followers Count](4_sorting_and_grouping/27_1729_Find_Followers_Count.ipynb)
- [ ] **SQL50 #13 · LC 570 · Medium** — [Managers with at Least 5 Direct Reports](2_basic_joins/13_570_Managers_with_at_Least_5_Direct_Reports.ipynb)
- [ ] **SQL50 #20 · LC 1193 · Medium** — [Monthly Transactions I](3_basic_aggregate_functions/20_1193_Monthly_Transactions_I.ipynb)
- [ ] **SQL50 #47 · LC 176 · Medium** — [Second Highest Salary](7_advanced_string_functions_regex_clause/47_176_Second_Highest_Salary.ipynb)

### Day 2 — JOIN / GROUP BY / Conditional Logic

- [ ] **SQL50 #03 · LC 595 · Easy** — [Big Countries](1_Select/03_595_Big_Countries.ipynb)
- [ ] **SQL50 #04 · LC 1148 · Easy** — [Article Views I](1_Select/04_1148_Article_Views_I.ipynb)
- [ ] **SQL50 #07 · LC 1068 · Easy** — [Product Sales Analysis I](2_basic_joins/07_1068_Product_Sales_Analysis_I.ipynb)
- [ ] **SQL50 #11 · LC 577 · Easy** — [Employee Bonus](2_basic_joins/11_577_Employee_Bonus.ipynb)
- [ ] **SQL50 #23 · LC 2356 · Easy** — [Number of Unique Subjects Taught by Each Teacher](4_sorting_and_grouping/23_2356_Number_of_Unique_Subjects_Taught_by_Each_Teacher.ipynb)
- [ ] **SQL50 #32 · LC 610 · Easy** — [Triangle Judgement](5_advanced_select_and_joins/32_610_Triangle_Judgement.ipynb)
- [ ] **SQL50 #44 · LC 1667 · Easy** — [Fix Names in a Table](7_advanced_string_functions_regex_clause/44_1667_Fix_Names_in_a_Table.ipynb)
- [ ] **SQL50 #14 · LC 1934 · Medium** — [Confirmation Rate](2_basic_joins/14_1934_Confirmation_Rate.ipynb)
- [ ] **SQL50 #25 · LC 1070 · Medium** — [Product Sales Analysis III](4_sorting_and_grouping/25_1070_Product_Sales_Analysis_III.ipynb)
- [ ] **SQL50 #38 · LC 626 · Medium** — [Exchange Seats](6_subqueries/38_626_Exchange_Seats.ipynb)

### Day 3 — Relationship / Latest Record / Category Logic

- [ ] **SQL50 #08 · LC 1581 · Easy** — [Customer Who Visited but Did Not Make Any Transactions](2_basic_joins/08_1581_Customer_Who_Visited_but_Did_Not_Make_Any_Transactions.ipynb)
- [ ] **SQL50 #09 · LC 197 · Easy** — [Rising Temperature](2_basic_joins/09_197_Rising_Temperature.ipynb)
- [ ] **SQL50 #18 · LC 1633 · Easy** — [Percentage of Users Attended a Contest](3_basic_aggregate_functions/18_1633_Percentage_of_Users_Attended_a_Contest.ipynb)
- [ ] **SQL50 #26 · LC 596 · Easy** — [Classes More Than 5 Students](4_sorting_and_grouping/26_596_Classes_More_Than_5_Students.ipynb)
- [ ] **SQL50 #31 · LC 1789 · Easy** — [Primary Department for Each Employee](5_advanced_select_and_joins/31_1789_Primary_Department_for_Each_Employee.ipynb)
- [ ] **SQL50 #45 · LC 1527 · Easy** — [Patients With a Condition](7_advanced_string_functions_regex_clause/45_1527_Patients_With_a_Condition.ipynb)
- [ ] **SQL50 #21 · LC 1174 · Medium** — [Immediate Food Delivery II](3_basic_aggregate_functions/21_1174_Immediate_Food_Delivery_II.ipynb)
- [ ] **SQL50 #36 · LC 1907 · Medium** — [Count Salary Categories](5_advanced_select_and_joins/36_1907_Count_Salary_Categories.ipynb)
- [ ] **SQL50 #41 · LC 602 · Medium** — [Friend Requests II: Who Has the Most Friends](6_subqueries/41_602_Friend_Requests_II_Who_Has_the_Most_Friends.ipynb)
- [ ] **SQL50 #34 · LC 1164 · Medium** — [Product Price at a Given Date](5_advanced_select_and_joins/34_1164_Product_Price_at_a_Given_Date.ipynb)

### Day 4 — Aggregation / Window / Set Logic

- [ ] **SQL50 #10 · LC 1661 · Easy** — [Average Time of Process per Machine](2_basic_joins/10_1661_Average_Time_of_Process_per_Machine.ipynb)
- [ ] **SQL50 #12 · LC 1280 · Easy** — [Students and Examinations](2_basic_joins/12_1280_Students_and_Examinations.ipynb)
- [ ] **SQL50 #19 · LC 1211 · Easy** — [Queries Quality and Percentage](3_basic_aggregate_functions/19_1211_Queries_Quality_and_Percentage.ipynb)
- [ ] **SQL50 #28 · LC 619 · Easy** — [Biggest Single Number](4_sorting_and_grouping/28_619_Biggest_Single_Number.ipynb)
- [ ] **SQL50 #37 · LC 1978 · Easy** — [Employees Whose Manager Left the Company](6_subqueries/37_1978_Employees_Whose_Manager_Left_the_Company.ipynb)
- [ ] **SQL50 #48 · LC 1484 · Easy** — [Group Sold Products By The Date](7_advanced_string_functions_regex_clause/48_1484_Group_Sold_Products_By_The_Date.ipynb)
- [ ] **SQL50 #22 · LC 550 · Medium** — [Game Play Analysis IV](3_basic_aggregate_functions/22_550_Game_Play_Analysis_IV.ipynb)
- [ ] **SQL50 #29 · LC 1045 · Medium** — [Customers Who Bought All Products](4_sorting_and_grouping/29_1045_Customers_Who_Bought_All_Products.ipynb)
- [ ] **SQL50 #33 · LC 180 · Medium** — [Consecutive Numbers](5_advanced_select_and_joins/33_180_Consecutive_Numbers.ipynb)
- [ ] **SQL50 #42 · LC 585 · Medium** — [Investments in 2016](6_subqueries/42_585_Investments_in_2016.ipynb)

### Day 5 — Advanced Interview Day

- [ ] **SQL50 #16 · LC 1251 · Easy** — [Average Selling Price](3_basic_aggregate_functions/16_1251_Average_Selling_Price.ipynb)
- [ ] **SQL50 #24 · LC 1141 · Easy** — [User Activity for the Past 30 Days I](4_sorting_and_grouping/24_1141_User_Activity_for_the_Past_30_Days_I.ipynb)
- [ ] **SQL50 #30 · LC 1731 · Easy** — [The Number of Employees Which Report to Each Employee](5_advanced_select_and_joins/30_1731_The_Number_of_Employees_Which_Report_to_Each_Employee.ipynb)
- [ ] **SQL50 #46 · LC 196 · Easy** — [Delete Duplicate Emails](7_advanced_string_functions_regex_clause/46_196_Delete_Duplicate_Emails.ipynb)
- [ ] **SQL50 #49 · LC 1327 · Easy** — [List the Products Ordered in a Period](7_advanced_string_functions_regex_clause/49_1327_List_the_Products_Ordered_in_a_Period.ipynb)
- [ ] **SQL50 #50 · LC 1517 · Easy** — [Find Users With Valid E-Mails](7_advanced_string_functions_regex_clause/50_1517_Find_Users_With_Valid_E_Mails.ipynb)
- [ ] **SQL50 #35 · LC 1204 · Medium** — [Last Person to Fit in the Bus](5_advanced_select_and_joins/35_1204_Last_Person_to_Fit_in_the_Bus.ipynb)
- [ ] **SQL50 #39 · LC 1341 · Medium** — [Movie Rating](6_subqueries/39_1341_Movie_Rating.ipynb)
- [ ] **SQL50 #40 · LC 1321 · Medium** — [Restaurant Growth](6_subqueries/40_1321_Restaurant_Growth.ipynb)
- [ ] **SQL50 #43 · LC 185 · Hard** — [Department Top Three Salaries](6_subqueries/43_185_Department_Top_Three_Salaries.ipynb)

## Notebook Contract

Every notebook is self-contained and contains:

- `0. Problem`
- `1. Setup`
- `2. SQL Solution`
- `3. pandas Solution`
- `4. PySpark Solution`
- `5. Pattern Mapping`
- `6. Muscle-Memory Round`

The pandas setup appears before PySpark imports so pandas practice can run directly in Colab even before PySpark is installed.

## Runtime

### Databricks

Primary runtime. Spark and Spark SQL are already available.

### Google Colab

pandas runs directly. Install PySpark once before using the Spark sections:

```python
!pip -q install pyspark
```

## Validation

The repository includes `tools/validate_notebooks.py` and tests that enforce:

- exactly 50 training notebooks;
- canonical notebook sequence `01` through `50` exactly once;
- all required notebook sections;
- valid notebook JSON;
- no solution-like code inside Muscle-Memory cells.

> Spark code is designed for Databricks / PySpark-enabled Colab. The repository's build-time checks validate notebook structure and Python syntax; Spark runtime behavior should also be exercised in the target Spark environment.
