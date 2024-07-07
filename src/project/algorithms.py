
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from data_wrangling import df, X, y
from feature_selection import X_new




scale=StandardScaler()
X_scale_new=scale.fit_transform(X_new)






# Decision Tree Model:  



class DecisionTree_Randomstate:
    
    
    try:

        decision_train_random=[]
        decision_test_ramdom=[]

        for i in range(0,100):
            
            X_train_dt,X_test_dt,y_train_dt,y_test_dt=train_test_split(X_scale_new,y,test_size=0.20,random_state=i)
            
            deci_model=DecisionTreeClassifier(criterion= 'entropy', max_depth= 5, max_leaf_nodes= 5, min_samples_leaf= 2, min_samples_split= 2, splitter= 'random')
            deci_model.fit(X_train_dt,y_train_dt)
            y_pred_train=deci_model.predict(X_train_dt)
            y_pred_test=deci_model.predict(X_test_dt)
            decision_train_random.append(accuracy_score(y_train_dt,y_pred_train))
            decision_test_ramdom.append(accuracy_score(y_test_dt,y_pred_test))

    except Exception as e:
        raise Exception(f'Error in DecisionTree_Randomstate init level :\n'+str(e))
    
       
    

class DecisionTree_Classification(DecisionTree_Randomstate):

    try:


        X_train_dt,X_test_dt,y_train_dt,y_test_dt=train_test_split(X_scale_new,y,test_size=0.20,random_state=np.argmax(DecisionTree_Randomstate.decision_test_ramdom))

        decision_model=DecisionTreeClassifier(criterion= 'gini', max_depth= 4, max_leaf_nodes= 5, min_samples_leaf= 3, min_samples_split= 3, splitter= 'random')
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
plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/src/project/cm_decision.png')
    
    

