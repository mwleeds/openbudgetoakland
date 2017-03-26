"""
This script reads UA financial data downloaded from open.ua.edu in their CSV
format and writes it to a file in the format expected by the OpenBudgetOakland app.
The input CSVs should contain calendar year data; the output CSVs will be by
fiscal year (which ends Sept. 30th)
"""

import csv

def main():
    deps = []
    categories = []
    with open('FY15-16__UA.csv', 'w', newline='') as out_file:
        expense_sums = {}
        writer = csv.writer(out_file)
        writer.writerow(['account_category','account_type','amount','budget_year','department','fund_code'])
        for csv_file in ['ua_finances_2015.csv', 'ua_finances_2016.csv']:
            with open(csv_file) as in_file:
                reader = csv.DictReader(in_file)
                for row in reader:
                    if row['Fiscal Year'] == '2016':
                        if row['Agency'] not in expense_sums:
                            expense_sums[row['Agency']] = {}
                        category = row['Category'].title()
                        if category not in expense_sums[row['Agency']]:
                            expense_sums[row['Agency']][category] = float(row['Check Amount'])
                        else:
                            expense_sums[row['Agency']][category] += float(row['Check Amount'])
        for agency in expense_sums:
            for department in expense_sums[agency]:
                account_category = ''
                account_type = 'Expense'
                amount = str(expense_sums[agency][department])
                budget_year = 'FY15-16'
                deps.append(department)
                #TODO check for agencies other than UA and UA System Office
                fund_code = '1010'# if agency == 'THE UNIVERSITY OF ALABAMA' else 1011
                writer.writerow([account_category, account_type, amount, budget_year, department, fund_code])
        with open('ua_revenue_fy15-16.csv') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                account_category = row['Category']
                categories.append(account_category)
                account_type = 'Revenue'
                amount = row['Amount']
                budget_year = 'FY15-16'
                department = ''
                fund_code = '1010'
                writer.writerow([account_category, account_type, amount, budget_year, department, fund_code])
    deps = list(set(deps))
    categories = list(set(categories))
    print(deps)
    print('\n\n\n')
    print(categories)

if __name__=='__main__':
    main()
