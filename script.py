#first arg = chart
#second arg = number of weeks

import billboard
import csv
import datetime
import sys

# open the file in the write mode
f = open(sys.argv[1] + "-" + sys.argv[2] + "weeks.csv", 'w')

# create the csv writer
datetime.timedelta(days=10)
date = datetime.datetime.today()

writer = csv.writer(f)
writer.writerow((
    "rank", 
    "artist", 
    "title", 
    "date", 
    "lastPos", 
    "weeks", 
    "peakPos",
    "isNew"
))

for i in range(int(sys.argv[2])):
    chart = billboard.ChartData(sys.argv[1], date=date.strftime('%Y-%m-%d'))
    date = date - datetime.timedelta(days=7)
    for chartentry in chart:
        row = (
            chartentry.rank,
            chartentry.artist,
            chartentry.title,
            chart.date,
            chartentry.lastPos,
            chartentry.weeks,
            chartentry.peakPos,
            chartentry.isNew
        )

        # write a row to the csv file
        writer.writerow(row)

# close the file
f.close()
