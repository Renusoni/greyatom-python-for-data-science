# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)
df=data

#Code starts here

# Step 1 
#Reading the file
#Creating a new variable to store the value counts

loan_status=df['Loan_Status'].value_counts()

#Plotting bar plot
loan_status.plot(kind='bar')
plt.title('Bar graph of Loan_Status')

# Step 2

property_and_loan=df.groupby(['Property_Area','Loan_Status']).size().unstack()

#Plotting an unstacked bar plot
property_and_loan.plot(kind='bar')

plt.title('property_and_loan')

#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')


#Rotating the ticks of X-axis
plt.xticks(rotation=45) 

# Step 3
#Plotting a stacked bar plot
education_and_loan=df.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar')

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=df[df['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column
graduate_not=df[df['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate.plot(kind='density',label='Graduate')

#Plotting density plot for 'Graduate'
graduate_not.plot(kind='density',label='Not Graduate')

#For automatic legend display


# Step 5
#Setting up the subplots
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1,figsize=(20,10))

#Plotting scatter plot
df.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)

#Setting the subplot axis title
plt.title('Applicant Income')

#Plotting scatter plot
df.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)

#Setting the subplot axis title
plt.title('Coapplicant Income')

#Creating a new column 'TotalIncome'
df['TotalIncome']=df['ApplicantIncome']+df['CoapplicantIncome']

#Plotting scatter plot
df.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)


#Setting the subplot axis title
plt.title('Total Income')


print(data['TotalIncome'][1])


