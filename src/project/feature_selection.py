import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import plot_tree
from data_wrangling import df, X, y,X_scale


# Embedded method for feature selection:

# Decision Tree Model:



class DecisionTree_bestparam:

    try:

        for r in range(0,100):

            X_train_dt,X_test_dt,y_train_dt,y_test_dt=train_test_split(X_scale,y,test_size=0.20,random_state=r)
            dec_modl=DecisionTreeClassifier()
            dec_modl.fit(X_train_dt,y_train_dt)
            param={'criterion':['gini','entropy', 'log_loss'], 'max_depth':[1,2,3,4,5]}
            d_gcv=GridSearchCV(dec_modl,param_grid=param,cv=5,verbose=5)
            d_gcv.fit(X_train_dt,y_train_dt)
            best_param=d_gcv.best_params_

    except Exception as e:
        raise Exception(f'Error in DecisionTree_Classification init level :\n'+str(e))
    
    def __init__(self,dec_modl,d_gcv,best_param):

        self.dec_modl=dec_modl
        self.d_gcv=d_gcv
        self.best_param=best_param

    def dec_modl_defin(self):
        return self.dec_modl
    
    def d_gcv_defin(self):
        return self.d_gcv
    
    def best_param_defin(self):
        return self.best_param
    
 



print("Best Parameters for Decision Tree :",DecisionTree_bestparam.best_param)
print("Importance feature for model :",DecisionTree_bestparam.d_gcv.best_estimator_.feature_importances_)

fig,ax=plt.subplots(figsize=(10,5),dpi=300)
plot_tree(DecisionTree_bestparam.dec_modl,filled=True,feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                                                                               'BMI', 'DiabetesPedigreeFunction', 'Age'],class_names=['Yes','No'])
plt.title('Decision Tree classification freature Importence')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/src/project/feature_selection.png')


feat_imp=pd.DataFrame(data=DecisionTree_bestparam.d_gcv.best_estimator_.feature_importances_,index=X.columns,columns=['Feature_Importance'])
feature_imp=feat_imp[feat_imp['Feature_Importance']>0]
feature_selection=feature_imp.index.to_list()

X_new=X[feature_selection]
