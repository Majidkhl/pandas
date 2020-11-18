import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 25)
pd.set_option('display.expand_frame_repr', False)

path = 'C:/Users/a_khl/PycharmProjects/dataFrame/venv/Data/'
employees_file = 'employees.csv'


# employee_file = pd.read_csv('./venv/Data/countries.csv')

# Creation des dataframes

employees_df = pd.read_csv(f"{path}{employees_file}", delimiter=";", parse_dates=['HIRE_DATE'], dayfirst=True)

print(employees_df.info())

# Display full_name of the employees

employees_df.insert(3, 'FULL_NAME', employees_df['FIRST_NAME'] + ' ' + employees_df['LAST_NAME'])
employees_df.drop(columns=['FIRST_NAME', 'LAST_NAME'], inplace=True)

print('\n' * 1)
print('Display employees full_name')
print(employees_df)

# Display employees who have comissions
print('\n' * 1)
print('Display employees who have comissions_pct')
print(employees_df[pd.notna(employees_df['COMMISSION_PCT'])])

# Display the salary of Jennifer Whalen
print('\n' * 1)
print('Display the salary of Jennifer Whalen')
print(employees_df[employees_df['FULL_NAME'] == 'Jennifer Whalen'][['FULL_NAME', 'SALARY']])

#---------------
# jen = employees_df[employees_df['FULL_NAME'] == 'Jennifer Whalen']
# print(jen[['FULL_NAME', 'SALARY']])
#-------------------

# Afficher le nom complet des employés qui sont dans le départment 50 et qui ont un salaire > 3000
print('\n' * 1)
print('Display the employees of department 50 and salary > 3000')
print(employees_df.query('DEPARTMENT_ID == 50').query('SALARY > 3000')[['FULL_NAME', 'DEPARTMENT_ID', 'SALARY']])

# Afficher le nom complet des employés qui sont dans le départment 50 et qui ont un salaire > 3000 en utilisnat mask
print('\n' * 1)
print('Display the employees of department 50 and salary > 3000 using a mask')
mask1 = employees_df['DEPARTMENT_ID'] == 50
mask2 = employees_df['SALARY'] > 3000
print(employees_df[mask1 & mask2][['FULL_NAME', 'DEPARTMENT_ID', 'SALARY']])

# Afficher le nom complet des managers
print('\n' * 1)
print('Display the employees and the name of their managers_id')
manager_df = employees_df[['EMPLOYEE_ID', 'FULL_NAME', 'MANAGER_ID']]
print(manager_df)

print('\n' * 1)
print('Display the employees and the name of their managers_names')
manager_name = pd.merge(manager_df, manager_df, left_on=['MANAGER_ID'], right_on=['EMPLOYEE_ID'])

print(manager_name)

print('\n' * 2)

manager_name = manager_name[manager_name.columns[[0, 1, 2, 4]]]
manager_name.columns = ['EMPLOYEE_ID', 'EMPLOYEE_FULL_NAME', 'MANAGER_ID', 'MANAGER_FULL_NAME']
print(manager_name)




