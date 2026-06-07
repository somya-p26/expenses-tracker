import pandas as pd
import numpy as ny
df=pd.read_csv("E.csv")
tab=pd.DataFrame(df,columns=["Date","Catergory","Amount"])

print("""
========================================
      EXPENSE TRACKER ANALYZER
========================================

Hello and welcome!

This Expense Tracker helps you analyze your spending habits and gain insights into your monthly expenses.

With this tool, you can:
1.Check your total expenses
2. Analyze category-wise spending
3.View monthly expense summaries
4. Identify your highest and lowest spending till now.
5.Find your highest expense for a specific month
6.print your whole expenses table.
7.Exit

Let the tracker do the analysis for you.

Let's get started!
========================================
""")

while True:

    a=int(input('enter your choose from 1 to 7:'))

    if a==1 :
        total_expenses=df["Amount"].sum()
        print("total_expenses:Rs. ",total_expenses)
        
    elif a==2:
        catergory_spending=df.groupby("Catergory")["Amount"].sum()
        print("catergory-spending: Rs.",catergory_spending)
        
    elif a==3:
        m=pd.to_datetime(df["Date"])
        monthly_spending=df.groupby(m.dt.to_period("M"))["Amount"].sum()
        print("monthly_spending: Rs.",monthly_spending)
        
    elif a==4:
        highest_spend=df["Amount"].max()
        lowest_spend=df["Amount"].min()
        print("highest_spend: Rs",highest_spend)
        print("lowest_spend: Rs",lowest_spend)
        
    elif a==5:
        month=int(input("enter the month for which you want to check the spending(1-12):"))
        year=int(input("enter the year for which you want to check the spending(20XX):"))
        m=pd.to_datetime(df["Date"])
        data=df[(m.dt.month==month)&(m.dt.year==year)]
        if len(data)>0:
            highest_row=data.loc[data["Amount"].idxmax()]
            print("highest expenses")
            print("date:",highest_row["Date"])
            print("catergory:",highest_row["Catergory"])
            print("amount:",highest_row["Amount"])
        else:
            print(' There is no expenses for this month ')

        if len(data)>0:
            lowest_row=data.loc[data["Amount"].idxmin()]
            print("lowest expenses")
            print("date:",lowest_row["Date"])
            print("catergory:",lowest_row["Catergory"])
            print("amount:",lowest_row["Amount"])
        else:
            print(' There is no expenses for this month ')
    elif a==6:
        print(df)
    elif a==7:
        print('Thank you for using expenses Tracker')
        print("GOODBYE!!")
        break
        
    else:
        print ('wrong input')
