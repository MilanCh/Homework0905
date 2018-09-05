import csv
import os


file_path=os.path.join("budget_data.csv")

with open(file_path,newline="") as data_file:
     csvreader=csv.reader(data_file,delimiter=",")
     next(csvreader)
     i=0
     month_num=0
     each_month=[]
     months=[]
     for row in csvreader:
         months.append(row[0])
         each_month.append(float(row[1]))
         month_num=month_num+1
    
     f=open('budget_result.txt','w')


     print("Financial Analysis")
     f.write("Financial Analysis\n")
     print("----------------------------")
     f.write("--------------------------\n")
     print("Total Months:{}".format(month_num))
     f.write("Total Months:{}\n".format(month_num))
     print("Total:${}".format(sum(each_month)))
     f.write("Total:${}\n".format(sum(each_month)))

     change1=each_month[:-1]
     change2=each_month[1:]
     changes=[change2[i]-change1[i] for i in range(month_num-1)]

     print("Average change:${}".format(sum(changes)/(month_num-1)))
     f.write("Average change:${}\n".format(sum(changes)/(month_num-1)))
     print("Greatest increase in Profits :{} (${})".format(months[changes.index(max(changes))+1],max(changes)))
     f.write("Greatest increase in Profits :{} (${})\n".format(months[changes.index(max(changes))+1],max(changes)))
     print("Greatest Decrease in Profits :{} (${})".format(months[changes.index(min(changes))+1],min(changes)))
     f.write("Greatest Decrease in Profits :{} (${})\n".format(months[changes.index(min(changes))+1],min(changes)))

        