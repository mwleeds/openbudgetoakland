"""
This script reads UA financial data downloaded from open.ua.edu in their CSV
format and writes it to a file in the format expected by HighCharts
"""

import csv

def main():
    with open('ua_expenses_fy16_highcharts.csv', 'w', newline='') as out_file:
        date_sums = {}
        writer = csv.writer(out_file)
        writer.writerow(['Date','Amount'])
        for csv_file in ['ua_finances_2015.csv', 'ua_finances_2016.csv']:
            with open(csv_file) as in_file:
                reader = csv.DictReader(in_file)
                for row in reader:
                    if row['Fiscal Year'] == '2016':
                        if row['Date'] not in date_sums:
                            date_sums[row['Date']] = float(row['Check Amount'])
                        else:
                            date_sums[row['Date']] += float(row['Check Amount'])
        for date in date_sums:
            amount = str(date_sums[date])
            writer.writerow([date.split(' ')[0], amount])

if __name__=='__main__':
    main()
