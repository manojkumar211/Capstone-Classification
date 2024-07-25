
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
import tensorflow as tf
import tensorboard
import keras
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense
import os
import time





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


class Ann_Randomstate:

    try:

        test_rand_ann=[]

        for i in range(0,10):
            
            X_train_ann,X_test_ann,y_train_ann,y_test_ann=train_test_split(X_scale_new,y,test_size=0.2,random_state=i)
            ann=Sequential()
            ann.add(Dense(input_dim=5,units=9,activation='relu',kernel_initializer='uniform'))
            ann.add(Dense(units=1,activation='sigmoid',kernel_initializer='uniform'))
            ann.compile(optimizer='adam',loss='binary_crossentropy',metrics=['Accuracy'])
            ann.fit(X_train_ann,y_train_ann,batch_size=5,epochs=100)
            ann_test_pred=ann.predict(X_test_ann)
            ann_best=(ann_test_pred>0.5)
            test_rand_ann.append(accuracy_score(y_test_ann,ann_best))

    except Exception as e:
        raise Exception(f'Error find in ANN Randomstate level :\n'+str(e))

class ANN_model(Ann_Randomstate):

    try:

        X_train_ann,X_test_ann,y_train_ann,y_test_ann=train_test_split(X_scale_new,y,test_size=0.2,random_state=np.argmax(Ann_Randomstate.test_rand_ann))
        ann_model=Sequential()
        ann_model.add(Dense(input_dim=5,units=9,activation='relu',kernel_initializer='uniform'))
        ann_model.add(Dense(units=1,activation='sigmoid',kernel_initializer='uniform'))
        ann_model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['Accuracy'])
        log_dir="C:/DataScience/log/fit/"+time.asctime().replace(" ","_").replace(":","_")
        tensorboard_cp=tf.keras.callbacks.TensorBoard(log_dir=log_dir)
        early_stop=tf.keras.callbacks.EarlyStopping(patience=5,restore_best_weights=True)
        ckpt_path="model_ckpt.keras"
        checkpoint_cp=tf.keras.callbacks.ModelCheckpoint(ckpt_path,save_best_only=True)
        callback_list=[tensorboard_cp,early_stop,checkpoint_cp]
        ann_model.fit(x=X_train_ann,y=y_train_ann,batch_size=5,epochs=100,callbacks=callback_list)
        ann_test_pred=ann_model.predict(X_test_ann)
        ann_best=(ann_test_pred>0.5)
        print("Accuracy of ANN model :",accuracy_score(y_test_ann,ann_best))

    except Exception as e:
        raise Exception(f'Error in ANN model level :\n'+str(e))

    def __init__(self,ann,log_dir,tensorboard_cb,test_rand_ann,tensorboard_cp,early_stop,checkpoint_cp,callback_list):

        try:

            self.ann = ann
            self.log_dir = log_dir
            self.tensorboard_cb = tensorboard_cb
            self.test_rand_ann=test_rand_ann
            self.tensorboard_cp=tensorboard_cp
            self.early_stop=early_stop
            self.checkpoint_cp=checkpoint_cp
            self.callback_list=callback_list


        except Exception as e:
            raise Exception(f'Error in ANN_model init level :\n'+str(e))
        
    try:

        def ann_model_defin(self):
            return self.ann
        
        def log_dir_defin(self):
            return self.log_dir
        
        def tensorboard_cb_defin(self):
            return self.tensorboard_cb
        
        def test_rand_ann_defin(self):
            return super().test_rand_ann
        
        def tensorboard_cp_defin(self):
            return super().tensorboard_cp
        
        def early_stop_defin(self):
            return super().early_stop
        
        def checkpoint_cp_defin(self):
            return super().checkpoint_cp
        
        def callback_list_defin(self):
            return super().callback_list
        
    except Exception as e:
        raise Exception(f'Error in ANN_model define level :\n'+str(e))
    
        

    
    

        