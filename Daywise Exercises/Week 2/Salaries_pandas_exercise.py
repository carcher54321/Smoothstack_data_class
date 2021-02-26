import numpy as np
import pandas as pd

data_set = pd.read_csv('Salaries.csv')


def average(it):
    avg = sum(it) / len(it)
    return round(avg, 2)


# Check and display the head of the DataFrame.
print(data_set.head())

# Use the .info() method to find out how many entries there are.
print(data_set.info())

# What is the average of first 10000 items in BasePay
print(f'Average: {average(data_set["BasePay"][0:10000])}')

# What is the highest amount of TotalPayBenefits in the dataset
print(f"Highest TotalPayBenefits: {max(data_set['TotalPayBenefits'])}")

# What is the job title of JOSEPH DRISCOLL
joseph = data_set.loc[data_set['EmployeeName'] == 'JOSEPH DRISCOLL']
print(f"Joseph Job Title: {joseph['JobTitle']}")

# How much does JOSEPH DRISCOLL make (including benefits)?
print(f"Joseph Total Pay: {joseph['TotalPayBenefits']}")

# What is the name of highest paid person (including benefits)?
max_paid = data_set.loc[data_set['TotalPayBenefits'] == data_set['TotalPayBenefits'].max()]
print(f"MaxPaidName: {max_paid['EmployeeName']}")

# What is the name of lowest paid person (including benefits)? Do you notice something
# strange about how much he or she is paid?
min_paid = data_set.loc[data_set['TotalPayBenefits'] == data_set['TotalPayBenefits'].min()]
print(f"MinPaidName: {min_paid['EmployeeName']}")
print(f"MinPaidAmt: {min_paid['TotalPayBenefits']}")
# Joe Lopez's pay is negative

# What was the average (mean) TotalPay of all employees per year? (2011-2014)
print(data_set.groupby('Year').mean())

# How many unique job titles are there?
unique_jobs = data_set['JobTitle'].value_counts()
print(f"Unique Job Titles: {len(unique_jobs)}")

# What are the top 7 most common jobs?
print(unique_jobs[0:7])

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with
# only one occurence in 2013?)
unique_jobs_2013 = data_set.loc[data_set['Year'] == 2013]['JobTitle'].value_counts()
num_jobs = unique_jobs_2013.value_counts()
print(f'Number of jobs in 2013 with one occurrence: {num_jobs[1]}')

# How many people have the word Chief in their job title?
print(f"Number of job titles which contain 'Chief': {len(data_set.loc[data_set['JobTitle'].str.contains('Chief')])}")

# Is there a correlation between length of the Job Title string and Salary?

# Because the correlation is so close to 0 (-0.036), I'd say there is not a
# statistically significant correlation
print(data_set['JobTitle'].apply(lambda x: len(x)).corr(data_set['TotalPayBenefits']))

"""
OUTPUT:
sys:1: DtypeWarning: Columns (3,4,5,6,12) have mixed types.Specify dtype option on import or set low_memory=False.
   Id       EmployeeName  ...         Agency Status
0   1     NATHANIEL FORD  ...  San Francisco    NaN
1   2       GARY JIMENEZ  ...  San Francisco    NaN
2   3     ALBERT PARDINI  ...  San Francisco    NaN
3   4  CHRISTOPHER CHONG  ...  San Francisco    NaN
4   5    PATRICK GARDNER  ...  San Francisco    NaN

[5 rows x 13 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148654 entries, 0 to 148653
Data columns (total 13 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                148654 non-null  int64  
 1   EmployeeName      148654 non-null  object 
 2   JobTitle          148654 non-null  object 
 3   BasePay           148049 non-null  object 
 4   OvertimePay       148654 non-null  object 
 5   OtherPay          148654 non-null  object 
 6   Benefits          112495 non-null  object 
 7   TotalPay          148654 non-null  float64
 8   TotalPayBenefits  148654 non-null  float64
 9   Year              148654 non-null  int64  
 10  Notes             0 non-null       float64
 11  Agency            148654 non-null  object 
 12  Status            38119 non-null   object 
dtypes: float64(3), int64(2), object(8)
memory usage: 14.7+ MB
None
Average: 112236.76
Highest TotalPayBenefits: 567595.43
Joseph Job Title: 24    CAPTAIN, FIRE SUPPRESSION
Name: JobTitle, dtype: object
Joseph Total Pay: 24    270324.91
Name: TotalPayBenefits, dtype: float64
MaxPaidName: 0    NATHANIEL FORD
Name: EmployeeName, dtype: object
MinPaidName: 148653    Joe Lopez
Name: EmployeeName, dtype: object
MinPaidAmt: 148653   -618.13
Name: TotalPayBenefits, dtype: float64
            Id      TotalPay  TotalPayBenefits  Notes
Year                                                 
2011   18080.0  71744.103871      71744.103871    NaN
2012   54542.5  74113.262265     100553.229232    NaN
2013   91728.5  77611.443142     101440.519714    NaN
2014  129593.0  75463.918140     100250.918884    NaN
Unique Job Titles: 2159
Transit Operator                7036
Special Nurse                   4389
Registered Nurse                3736
Public Svc Aide-Public Works    2518
Police Officer 3                2421
Custodian                       2418
TRANSIT OPERATOR                2388
Name: JobTitle, dtype: int64
Number of jobs in 2013 with one occurrence: 202
Number of job titles which contain 'Chief': 423
-0.03687844593260708

Process finished with exit code 0
"""
