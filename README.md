# About Dataset:

```
- Dataset is related to Arrhythmia disease which is nothing but blood circulation issue. The dataset is belongs to medical domain.
- Dataset has 175729 - rows and 34 - columns.
- In this dataset, we do not have any duplicates records.
- In this dataset, we do not have any Null values.
- The cloumn names are
['record', 'type', '0_pre-RR', '0_post-RR', '0_pPeak', '0_tPeak', '0_rPeak', '0_sPeak', '0_qPeak', '0_qrs_interval', '0_pq_interval', '0_qt_interval', '0_st_interval', '0_qrs_morph0', '0_qrs_morph1', '0_qrs_morph2', '0_qrs_morph3', '0_qrs_morph4', '1_pre-RR', '1_post-RR', '1_pPeak', '1_tPeak', '1_rPeak', '1_sPeak', '1_qPeak', '1_qrs_interval', '1_pq_interval', '1_qt_interval', '1_st_interval', '1_qrs_morph0', '1_qrs_morph1', '1_qrs_morph2', '1_qrs_morph3', '1_qrs_morph4']

```
```
- In this dataset, we are having 20 - Countinuous variables, 2 - Discrete categorical variables and 12 - Discrete count variables. Those are.

- Continuouse variables are: ['0_pPeak', '0_tPeak', '0_rPeak', '0_sPeak', '0_qPeak', '0_qrs_morph0', '0_qrs_morph1', '0_qrs_morph2', '0_qrs_morph3', '0_qrs_morph4', '1_pPeak', '1_tPeak', '1_rPeak', '1_sPeak', '1_qPeak', '1_qrs_morph0', '1_qrs_morph1', '1_qrs_morph2', '1_qrs_morph3', '1_qrs_morph4']

- Discrete categorical variables are: ['record', 'type']

- Discrete count variabkes are: ['0_pre-RR', '0_post-RR', '0_qrs_interval', '0_pq_interval', '0_qt_interval', '0_st_interval', '1_pre-RR', '1_post-RR', '1_qrs_interval', '1_pq_interval', '1_qt_interval', '1_st_interval']

```
## Some terminolagy for the Arrhythmia.
```
- P wave = Atrial depolarization. The positive wave of depolarization spreads from the SA node and is conducted throughout the cells of the atria through gap junctions in that connect these cells.
- PR segment = depolarization of the AV node. I.e. When current is passing through the AV node.  It’s a flat line because the wave is not strong enough to be recorded on the voltmeter.
- PR interval = Wave goes over the atrium and through the AV node and ends just before it activates the ventricles to depolarize.
- Q wave = Ventricular Septal Depolarization
- R wave = Resultant or major ventricular muscle depolarization. The resultant vector is directed downward and leftward.
- S Wave = Basal Ventricular depolarization, i.e. depolarization of the base of the ventricles. Note the apex of the heart is the L. pointed end. The base of the ventricles connects to the atria.
- ST segment = During the ST segment, all the ventricular myocardium is depolarized. All have positive charges. So there is nothing potential difference to be recorded by the voltmeter (ECG machine). So you have a flat line.
- T wave represents ventricular repolarization.
- QT interval = Important because it captures the beginning of ventricular depolarization through the plateau phase to the ventricular repolarization. It covers the entire ventricular activity. During this time, the action potential was generated and terminated in the ventricular tissue. The beginning of the QRS complex is the start of ventricular systole and that goes until the end of the T wave. Ventricular diastole starts when the T wave ends. 
- U wave. Sometimes the electrical activity of the ventricular papillary muscle is out of phase with the rest of the ventricles and will record as a “U” wave that shows after the T wave.

- Above parameters are based on the ECG Waves or Strokes.
```


# Columns:
```
- Before analyse the columns we apllied some data cleaning techniques like, replaced some elements name.
those are
----------------
I01-1 to I75-75
N- Normal & 0
VEB- 1
SVEB- 2
F- 3
Q- 4 with new column as type_new variable based on type variable.
```

## record:
```
- In this column, we are having 75 unique values.
- In this unique values the 36 number is most repeated.
- The record column has skewness with 0.0290, which we consider as a symmetrical distribution. not as a non symmetrical distribution.
- The record column's variance value is 464.3977 and standard deviation value is 21.5498, which are very low. that mean the data points are spred very close to mean.
- The record column has 0.036% correlation with Dependent variables (type/type_new variable)
            record  type_new
record    1.000000  0.036071
type_new  0.036071  1.000000
--------------------------------------------------------------
count    175729.000000
mean         37.219406
std          21.549952
min           1.000000
25%          19.000000
50%          37.000000
75%          56.000000
max          75.000000
```