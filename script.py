#first arg = chart
#second arg = number of weeks

import billboard
import csv
import datetime
import sys

# Open the file in the write mode
f = open(sys.argv[1] + "-" + sys.argv[2] + "weeks.csv", 'w')
# Create the csv writer
writer = csv.writer(f)

# Write headers
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

# Set date to todays date
date = datetime.datetime.today()

# Loop for number of weeks specified by $2
for i in range(int(sys.argv[2])):

    # Get the chart specified by $1 for the weeek of `date`
    chart = billboard.ChartData(sys.argv[1], date=date.strftime('%Y-%m-%d'))

    # Loop through the chart entries
    for chartentry in chart:
        
        # Put the attributes of the entry 
        # into the correct collumns
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
        
    # Subtract seven days from `date` for 
    # the next iteration of the loop
    date = date - datetime.timedelta(days=7)

# close the file
f.close()
