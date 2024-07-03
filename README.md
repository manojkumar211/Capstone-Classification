# About Dataset:

```
- Dataset is related to Diabetes disease which is nothing but suger level issue. The dataset is belongs to medical domain.
- Dataset has 768 - rows and 9 - columns.
- In this dataset, we do not have any duplicates records.
- In this dataset, we do not have any Null values.
- The cloumn names are
['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

```
```
- In this dataset, we are having 2 - Countinuous variables, 1 - Discrete categorical variables and 6 - Discrete count variables. Those are.

- Continuouse variables are: ['BMI','DiabetesPedigreeFunction']

- Discrete categorical variables are: ['Outcome']

- Discrete count variabkes are: ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','Age']

```
## Some terminolagy for the Arrhythmia.
```
- Pregnancies: How many times the person has had a pregnancies. In this dataset, might we have male and female.

- Glucose: Glucose is the main type of sugar in the blood and is the major source of energy for the body's cells.
A fasting blood sugar level less than 100 mg/dL (5.6 mmol/L) is normal. A fasting blood sugar level from 100 to 125 mg/dL (5.6 to 6.9 mmol/L) is considered prediabetes. If it's 126 mg/dL (7 mmol/L) or higher on two separate tests, you have diabetes. 

- BloodPressure: Blood pressure is the pressure of circulating blood against the walls of blood vessels.
A healthy systolic blood pressure is less than 120 mm Hg. A healthy diastolic pressure is less than 80 mm Hg. Your blood pressure is high when you have consistent systolic readings of 130 mm Hg or higher, or diastolic readings of 80 mm Hg or higher.

- SkinThickness: The dermis is a tough but elastic support structure that houses nerves, blood vessels, lymphatics, and cutaneous appendages (pilosebaceous units, eccrine and apocrine sweat glands).
It is thicker (averages 1 to 4 mm) than the epidermis which is about as thin as piece of paper.

- Insulin: Insulin is a hormone that lowers the level of glucose (a type of sugar) in the blood.
It's made by the beta cells of the pancreas and released into the blood when the glucose level goes up, such as after eating. Insulin helps glucose enter the body's cells, where it can be used for energy or stored for future use.

- BMI: Body Mass Index (BMI) is a person's weight in kilograms divided by the square of height in meters. 
BMI	Weight Status
Below 18.5 ----->	Underweight
18.5 – 24.9	----->  Healthy Weight
25.0 – 29.9 ----->	Overweight
30.0 and Above ----->	Obesity

- DiabetesPedigreeFunction: The 'DiabetesPedigreeFunction' is a function that scores the probability of diabetes based on family history, with a realistic range of 0.08 to 2.42. Age has a realistic range from 21 to 81. The Outcome, in the target variable, 0 represents healthy people, and 1 represents those with diabetes.

- Age: age of the person.

- Outcome: Whether the person has Diabetes or not. If person has Diabetes, indicate that as 1, if the person has no Diabetes, indicate that as 0.

```


# Columns:

## Pregnancies:
```
- In this column, we are having 17 unique values.
- In this unique values the 1 number is most repeated.
- The Pregnancies column has skewness with 0.9016, which we consider as a symmetrical distribution. not as a non symmetrical distribution.
- The Pregnancies column's variance value is 11.339 and standard deviation value is 3.367, which are very low. that mean the data points are spred very close to mean.
- The Pregnancies column has 0.22% correlation with Dependent variables (type/type_new variable)
- The Pregnancies column has Outliers.

	        Pregnancies	Outcome
Pregnancies	1.000000	0.221898
Outcome	    0.221898	1.000000

--------------------------------------------------------------

count    768.000000
mean       3.845052
std        3.369578
min        0.000000
25%        1.000000
50%        3.000000
75%        6.000000
max       17.000000
Name: Pregnancies, dtype: float64
```
## Glucose:
```
- In this column, we are having 17 unique values.
- In this unique values the 1 number is most repeated.
- The Glucose column has skewness with 0.1737, which we consider as a symmetrical distribution. not as a non symmetrical distribution.
- The Glucose column's variance value is 1022.248 and standard deviation value is 31.972, which are very low. that mean the data points are spred very close to mean.
- The Glucose column has 0.47% correlation with Dependent variables (type/type_new variable)
- The Glucose column has Outliers.

	     Glucose	Outcome
Glucose	1.000000	0.466581
Outcome	0.466581	1.000000
--------------------------------------------------------------

count    768.000000
mean     120.894531
std       31.972618
min        0.000000
25%       99.000000
50%      117.000000
75%      140.250000
max      199.000000
Name: Glucose, dtype: float64
```

## BloodPressure:
```
- BloodPressure column has descrite count values.
count    768.000000
mean      69.105469
std       19.355807
min        0.000000
25%       62.000000
50%       72.000000
75%       80.000000
max      122.000000
Name: BloodPressure, dtype: float64

- It has no Null values.
- It has skewness with -1.843. so, we need to apply feature transformation techniques to make it as a symmetrical distribution.
BloodPressure Skewness : -1.8436079833551302

- It has variance with 374.159. which is very low. nothing but data poits spredding is very near to the mean.
BloodPressure Variance : 374.1594492594401

- It has standard deviation with 19.3423. which is very low. nothing but data poits spredding is very near to the mean.
BloodPressure Standard Deviation : 19.343201628981696

- This feature is directly proportional. which means it has covariance in negative values.
	            BloodPressure	Glucose
BloodPressure	374.159449	94.307999
Glucose	        94.307999	1020.917262

- This feature has correlation with 0.15.
	            BloodPressure	Outcome
BloodPressure	1.000000	0.065068
Outcome	        0.065068	1.000000

- This feature has Outliers. so, we need to apply IQR method to replace the outliers with upper limit or lower limit values.

```

## SkinThickness:
```
- SkinThickness column has descrite count variable.
count    768.000000
mean      20.536458
std       15.952218
min        0.000000
25%        0.000000
50%       23.000000
75%       32.000000
max       99.000000
Name: SkinThickness, dtype: float64

- This column does not have any null values.
- This column has outlier.
- It has variance value with 254.141. which is very low. nothing but data poits spredding is very near to the mean.
SkinThickness Variance : 254.14189995659726
- It has standard deviation value with 15.941. which is very low. nothing but data poits spredding is very near to the mean.
SkinThickness Standard Deviation : 15.941828626496939
- This column has with skewness value with 0.1093. for this we need to apply the feature transformation technique to make the feature symmetrical distribution.

```

## Insulin:-
```
- This column has continuous values.
count    768.000000
mean      79.799479
std      115.244002
min        0.000000
25%        0.000000
50%       30.500000
75%      127.250000
max      846.000000
Name: Insulin, dtype: float64

- It has some outliers.
- It does not have any null values.
- It has variance value with 13263.886. which is very low. nothing but data poits spredding is very near to the mean.
Insulin Variance : 13263.886874728734

- It has standard deviation value with 115.168. which is very low. nothing but data poits spredding is very near to the mean.
Insulin Standard Deviation : 115.16894926467262

- This column has with skewness value with 2.272. for this we need to apply the feature transformation technique to make the feature symmetrical distribution.
Insulin Skewness : 2.0734541596544926
```

## BMI:
```
- This column has continuous values.
count    768.000000
mean      31.992578
std        7.884160
min        0.000000
25%       27.300000
50%       32.000000
75%       36.600000
max       67.100000
Name: BMI, dtype: float64

- It has some outliers.
- It does not have any null values.
- It has variance value with 62.079. which is very low. nothing but data poits spredding is very near to the mean.
BMI Variance : 62.079046478271486

- It has standard deviation value with 7.879. which is very low. nothing but data poits spredding is very near to the mean.
BMI Standard Deviation : 7.87902573154013

- This column has with skewness value with -0.428. for this we need to apply the feature transformation technique to make the feature symmetrical distribution.
BMI Skewness : -0.42898158845356543

```



# DiabetesPedigreeFunction:
```
- This column has continuous values.
count    768.000000
mean       0.471876
std        0.331329
min        0.078000
25%        0.243750
50%        0.372500
75%        0.626250
max        2.420000
Name: DiabetesPedigreeFunction, dtype: float64

- It has some outliers.
- It does not have any null values.
- It has variance value with 0.1096. which is very low. nothing but data poits spredding is very near to the mean.
DiabetesPedigreeFunction Variance : 0.10963569693840876

- It has standard deviation value with 0.331. which is very low. nothing but data poits spredding is very near to the mean.
DiabetesPedigreeFunction Standard Deviation : 0.3311128160286291

- This column has with skewness value with 1.9199. for this we need to apply the feature transformation technique to make the feature symmetrical distribution.
DiabetesPedigreeFunction Skewness : 1.919911066307204
```

## Age:-
```
- This column has continuous values.
0_pPeak description : count    175729.000000
mean         -0.174214
std           0.368802
min          -7.113196
25%          -0.176258
50%          -0.105488
75%          -0.054578
max           3.129033
Name: 0_qPeak, dtype: float64

- It has some outliers.
- It does not have any null values.
- It has variance value with 0.1360. which is very low. nothing but data poits spredding is very near to the mean.
Age Variance : 0.13601431469058167

- It has standard deviation value with 0.3688. which is very low. nothing but data poits spredding is very near to the mean.
Age Standard Deviation : 0.36880118585842653

- This column has with skewness value with -4.572. for this we need to apply the feature transformation technique to make the feature symmetrical distribution.
Age Skewness : -4.572967178212863
```
