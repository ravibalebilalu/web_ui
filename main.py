import os
import calendar
import re
import shutil

#create year directory
years = [2025]
month_list = list(calendar.month_abbr[1:])
month_list = [month.lower() for month in month_list]
for year in years:
    os.makedirs(f"{year}",exist_ok=True)
    # make year and month directory
    for month in month_list:
        if month:
            os.makedirs(f"{year}/{month.lower()}", exist_ok=True)
             

list_of_content = os.listdir()  

for content in list_of_content:
    dir_month_name = re.sub("[^a-z]","" ,content)
    if dir_month_name in month_list:
        source = os.path.join(content)
        dest = os.path.join("2025/",dir_month_name)
        shutil.move(source,dest)
         
     


    
     
         




 

