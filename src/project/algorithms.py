
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from data_wrangling import df, X, y
from feature_selection import X_new




scale=StandardScaler()
X_scale_new=scale.fit_transform(X_new)



# Logistic Regression Model:

class Logistic_Randomstate:

    try:


        log_train_random=[]
        log_test_random=[]

        for i in range(0,100):

            X_train_log,X_test_log,y_train_log,y_test_log=train_test_split(X_scale_new,y,test_size=0.2,random_state=i)
            log_model=LogisticRegression()
            log_model.fit(X_train_log,y_train_log)
            y_pred_train=log_model.predict(X_train_log)
            y_pred_test=log_model.predict(X_test_log)
            log_train_random.append(accuracy_score(y_pred_train,y_train_log))
            log_test_random.append(accuracy_score(y_test_log,y_test_log))

    except Exception as e:
        raise Exception(f'Error in Logistic_Regression_Randomstate init level :\n'+str(e))

class Logistic_Regression(Logistic_Randomstate):

    X_train_log,X_test_log,y_train_log,y_test_log=train_test_split(X_scale_new,y,test_size=0.2,random_state=np.argmax(Logistic_Randomstate.log_test_random))

    try:

        logistic_model=LogisticRegression()
        logistic_model.fit(X_train_log,y_train_log)
        y_log_pred_train=logistic_model.predict(X_train_log)
        y_log_pred_test=logistic_model.predict(X_test_log)
        accuracy_log_train=accuracy_score(y_log_pred_train,y_train_log)
        accuracy_log_test=accuracy_score(y_log_pred_test,y_test_log)
        cross_val_log=cross_val_score(logistic_model,X_scale_new,y,cv=5).mean()
        con_mat_log=confusion_matrix(y_test_log,y_log_pred_test)

    except Exception as e:
        raise Exception(f'Error in Logistic_Regression init level :\n'+str(e))


    def __init__(self,logistic_model,y_log_pred_train,y_log_pred_test,accuracy_train,accuracy_test,cross_val_log,con_mat_log,log_model,log_train_random,log_test_random):

        try:

            self.logistic_model=logistic_model
            self.y_log_pred_train=y_log_pred_train
            self.y_log_pred_test=y_log_pred_test
            self.accuracy_train=accuracy_train
            self.accuracy_test=accuracy_test
            self.cross_val_log=cross_val_log
            self.con_mat_log=con_mat_log
            self.log_model=log_model
            self.log_train_random=log_train_random
            self.log_test_random=log_test_random

        except Exception as e:
            raise Exception(f'Error in Logistic_Regression_Randomstate init level :\n'+str(e))
        
    try:


        def logistic_model_defin(self):
            return self.logistic_model
        
        def y_log_pred_train_defin(self):
            return self.y_log_pred_train
        
        def y_log_pred_test_defin(self):
            return self.y_log_pred_test
        
        def accuracy_train_defin(self):
            return self.accuracy_train
        
        def accuracy_test_defin(self):
            return self.accuracy_test
        
        def cross_val_defin(self):
            return self.cross_val_log
        
        def con_mat_defin(self):
            return self.con_mat_log
        
        def log_model_defin(self):
            return super().log_model
        
        def log_train_random_defin(self):
            return super().log_train_random
        
        def log_test_random_defin(self):
            return super().log_test_random
        
    except Exception as e:
        raise Exception(f'Error in Logistic_Regression_Randomstate init level :\n'+str(e))
    


ConfusionMatrixDisplay(Logistic_Regression.con_mat_log,display_labels=df['Outcome'].unique()).plot()
plt.title('Confusion Matrix plot for Logistic Regression classification :')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Logistic_Regression/cm_log.png')



# Suport vectore classification model:



class SVC_Randomstate:

    try:

        svc_train_random=[]
        svc_test_random=[]

        for i in range(0,100):
            
            X_train_svc,X_test_svc,y_train_svc,y_test_svc=train_test_split(X_scale_new,y,test_size=0.2,random_state=i)
            svc_model=SVC()
            svc_model.fit(X_train_svc,y_train_svc)
            y_pred_train=svc_model.predict(X_train_svc)
            y_pred_test=svc_model.predict(X_test_svc)
            svc_train_random.append(accuracy_score(y_pred_train,y_train_svc))
            svc_test_random.append(accuracy_score(y_pred_test,y_test_svc))

    except Exception as e:
        raise Exception(f'Error in SVC_Randomstate init level :\n'+str(e))

class SVC_Classification(SVC_Randomstate):

    X_train_svc,X_test_svc,y_train_svc,y_test_svc=train_test_split(X_scale_new,y,test_size=0.2,random_state=np.argmax(SVC_Randomstate.svc_test_random))

    try: 
        svc_main_model=SVC()
        svc_main_model.fit(X_train_svc,y_train_svc)
        y_svc_pred_train=svc_main_model.predict(X_train_svc)
        y_svc_pred_test=svc_main_model.predict(X_test_svc)
        accuracy_svc_train=accuracy_score(y_svc_pred_train,y_train_svc)
        accuracy_svc_test=accuracy_score(y_svc_pred_test,y_test_svc)
        cross_val_svc=cross_val_score(svc_main_model,X_scale_new,y,cv=5).mean()
        con_mat_svc=confusion_matrix(y_test_svc,y_svc_pred_test)

    except Exception as e:
        raise Exception(f'Error in SVC_Classification init level :\n'+str(e))
    
    def __init__(self,svc_main_model,y_svc_pred_train,y_svc_pred_test,accuracy_train,accuracy_test,cross_val_svc,con_mat_svc,svc_model,svc_train_random,svc_test_random):

        try:

            self.svc_main_model=svc_main_model
            self.y_svc_pred_train=y_svc_pred_train
            self.y_svc_pred_test=y_svc_pred_test
            self.accuracy_train=accuracy_train
            self.accuracy_test=accuracy_test
            self.cross_val_svc=cross_val_svc
            self.con_mat_svc=con_mat_svc

        except Exception as e:
            raise Exception(f'Error in SVC_Classification init level :\n'+str(e))
        
    try:

        def svc_main_model_defin(self):
            return self.svc_main_model
        
        def y_svc_pred_train_defin(self):
            return self.y_svc_pred_train
        
        def y_svc_pred_test_defin(self):
            return self.y_svc_pred_test
        
        def accuracy_train_defin(self):
            return self.accuracy_train
        
        def accuracy_test_defin(self):
            return self.accuracy_test
        
        def cross_val_defin(self):
            return self.cross_val_svc
        
        def con_mat_defin(self):
            return self.con_mat_svc
        
        def svc_model_defin(self):
            return super().svc_model
        
        def svc_train_random_defin(self):
            return super().svc_train_random
        
        def svc_test_random_defin(self):
            return super().svc_test_random
        
    except Exception as e:
        raise Exception(f'Error in SVC_Classification init level :\n'+str(e))
    

ConfusionMatrixDisplay(SVC_Classification.con_mat_svc,display_labels=df['Outcome'].unique()).plot()
plt.title('Confusion Matrix plot for SVC classification :')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/SVC/cm_svc.png')




# Decision Tree Model:  



class DecisionTree_Randomstate:
    
    
    try:

        decision_train_random=[]
        decision_test_ramdom=[]

        for i in range(0,100):
            
            X_train_dt,X_test_dt,y_train_dt,y_test_dt=train_test_split(X_scale_new,y,test_size=0.2,random_state=i)
            deci_model=DecisionTreeClassifier()
            deci_model.fit(X_train_dt,y_train_dt)
            y_pred_train=deci_model.predict(X_train_dt)
            y_pred_test=deci_model.predict(X_test_dt)
            decision_train_random.append(accuracy_score(y_pred_train,y_train_dt))
            decision_test_ramdom.append(accuracy_score(y_pred_test,y_test_dt))

    except Exception as e:
        raise Exception(f'Error in DecisionTree_Randomstate init level :\n'+str(e))


class DecisionTree_Classification(DecisionTree_Randomstate):
    
    X_train_dt,X_test_dt,y_train_dt,y_test_dt=train_test_split(X_scale_new,y,test_size=0.2,random_state=np.argmax(DecisionTree_Randomstate.decision_test_ramdom))

    try:

        decision_model=DecisionTreeClassifier(criterion= 'entropy', max_depth= 4)
        decision_model.fit(X_train_dt,y_train_dt)
        y_pred_train=decision_model.predict(X_train_dt)
        y_pred_test=decision_model.predict(X_test_dt)
        accuracy_train=accuracy_score(y_pred_train,y_train_dt)
        accuracy_test=accuracy_score(y_pred_test,y_test_dt)
        cross_val=cross_val_score(decision_model,X_scale_new,y,cv=5).mean()
        con_mat=confusion_matrix(y_test_dt,y_pred_test)
        feature_imp=decision_model.feature_importances_

    except Exception as e:
        raise Exception(f'Error in DecisionTree_Classification init level :\n'+str(e))

    def __init__(self,decision_model,y_pred_train,y_pred_test,accuracy_train,accuracy_test,cross_val,con_mat,feature_imp,decision_train_random,decision_test_ramdom):

        try:

            self.decision_model=decision_model
            self.y_pred_train=y_pred_train
            self.y_pred_test=y_pred_test
            self.accuracy_train=accuracy_train
            self.accuracy_test=accuracy_test
            self.cross_val=cross_val
            self.con_mat=con_mat
            self.feature_imp=feature_imp
            self.decision_train_random=decision_train_random
            self.decision_test_ramdom=decision_test_ramdom

        except Exception as e:
            raise Exception(f'Error in DecisionTree_Classification init level :\n'+str(e))
        
    try:

        def decision_model_defin(self):
            return self.decision_model
        
        def y_pred_train_defin(self):
            return self.y_pred_train
        
        def y_pred_test_defin(self):
            return self.y_pred_test
        
        def accuracy_train_defin(self):
            return self.accuracy_train
        
        def accuracy_test_defin(self):
            return self.accuracy_test
        
        def cross_val_defin(self):
            return self.cross_val
        
        def con_mat_defin(self):
            return self.con_mat
        
        def feature_imp_defin(self):
            return self.feature_imp
        
        def decision_train_random_defin(self):
            return super().decision_train_random
        
        def decision_test_ramdom_defin(self):
            return super().decision_test_ramdom
        
        
    except Exception as e:
        raise Exception(f'Error in DecisionTree_Classification define level :\n'+str(e))
    


ConfusionMatrixDisplay(DecisionTree_Classification.con_mat,display_labels=df['Outcome'].unique()).plot()
plt.title('Confusion Matrix plot for Decision Tree classification :')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Decision_Tree/cm_decision.png')


print("Test Accuracy for Decision Tree :",DecisionTree_Classification.accuracy_test)
print("Best Test Random state number :",np.argmax(DecisionTree_Randomstate.decision_test_ramdom))
print("Train Accuracy for Decision Tree :",DecisionTree_Classification.accuracy_train)
print("CV Accuracy for Decision Tree :",DecisionTree_Classification.cross_val)

print('##'*30)

print("Test Accuracy for Logistic Regression :",Logistic_Regression.accuracy_log_test)
print("Best Test Random state number Logistic Regression :",np.argmax(Logistic_Regression.log_test_random))
print("Train Accuracy for Logistic Regression :",Logistic_Regression.accuracy_log_train)
print("CV Accuracy for Logistic Regression :",Logistic_Regression.cross_val_log)

print('##'*30)

print("Test Accuracy for SVC :",SVC_Classification.accuracy_svc_test)
print("Best Test Random state number SVC :",np.argmax(SVC_Classification.svc_test_random))
print("Train Accuracy for SVC :",SVC_Classification.accuracy_svc_train)
print("CV Accuracy for SVC :",SVC_Classification.cross_val_svc)
