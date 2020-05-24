# --------------
# Importing header files
import numpy as np
import warnings
import statistics

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]


#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record),axis=0)

age=census[:,0]
print("age:", age)

max_age=age.max()
print("max_age",max_age)

min_age=age.min()
print("min_age",min_age)

age_mean=age.mean()
print("Mean of age:  %.2f " %age_mean)

age_std=age.std()
print("Standerd age:  %.2f " %age_std)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


len_0=len(race_0)

len_1=len(race_1)

len_2=len(race_2)

len_3=len(race_3)

len_4=len(race_4)



if (len_0 < len_1 and len_0<len_2 and  len_0<len_3 and  len_0<len_4):
    minority_race=0
    print("minority_race: ",minority_race)
elif(len_1 < len_0 and len_1 <len_2 and len_1 <len_3 and len_1 <len_4):
    minority_race=1
    print("minority_race: ",minority_race)
elif(len_2 < len_0 and len_2 <len_1 and len_2 <len_3 and len_2 <len_4):
    minority_race=2
    print("minority_race: ",minority_race)
elif(len_3 < len_0 and len_3 <len_1 and len_3 <len_2 and len_3 <len_4):
    minority_race=3
    print("minority_race: ",minority_race)
else:
    minority_race=4
    print("minority_race: ",minority_race)


senior_citizens = list(filter(lambda x: x > 60, age)) 



senior_citizens_len=len(senior_citizens)
print("Count of  senior_citizens: ",senior_citizens_len)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=statistics.mean(high[:,7])
print("%.2f" %avg_pay_high)

avg_pay_low=statistics.mean(low[:,7])
print("%.2f" %avg_pay_low)

if(avg_pay_high > avg_pay_low):
    print("True")
else:
    print("False")
#Code starts here



