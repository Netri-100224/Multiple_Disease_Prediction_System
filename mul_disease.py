# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 10:37:27 2023

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model=pickle.load(open('E:\Multiple_disease\Multiple_disease_models\diabetes_model.sav', 'rb'))
breast_model=pickle.load(open(r'E:\\Multiple_disease\Multiple_disease_models\breast_cancer_model.sav','rb'))
heart_model=pickle.load(open('E:\Multiple_disease\Multiple_disease_models\heart_disease_model.sav','rb'))
parkinson_model=pickle.load(open('E:\Multiple_disease\Multiple_disease_models\parkinson_model.sav','rb'))
#2023-07-28 22:01:39.393 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`
#2023-07-28 22:01:39.402 
 # Warning: to view this Streamlit app on a browser, run it with the following
  #command:

   # streamlit run d:/.vscode/Multiple disease prediction/Mul_streamlit.py [ARGUMENTS]


with st.sidebar:

    selec = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Breast Cancer Prediction','Heart Disease Prediction','Parkinson Prediction'],icons=['capsule-pill','gender-female','activity','person-fill'],default_index=0)



if(selec=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    
    
    with col1:
    	Pregnancies=st.text_input('No of Pregnancies')
        
    with col2:
    	Glucose=st.text_input('Glucose Level')
       
    with col3:
    	BloodPressure=st.text_input('BloodPressure Level')
        
    with col1:
    	SkinThickness=st.text_input('SkinThickness Value')    
    
    with col2:
    	Insulin=st.text_input('Insulin Level')    
        
    with col3:
    	BMI=st.text_input('BMI Value') 
        
    with col1:
    	DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction Value') 
   
    with col2:
    	Age=st.text_input('Age')
        
    dia_diagnose=''
    
    if st.button('Diabetes prediction Result'):
        dia_pred=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(dia_pred[0]==1):
            dia_diagnose='You are Diabetic'
            
        else:
            dia_diagnose='You are not Diabetic'
            
    
    st.success(dia_diagnose)
            

if(selec=='Breast Cancer Prediction'):
    st.title('Breast Cancer Prediction using ML')
    col1,col2,col3=st.columns(3)
    
    
    with col1:
        mean_radius=st.text_input('mean radius')
    	    
    with col2:
    	mean_texture=st.text_input('mean texture')
       
    with col3:
    	mean_perimeter=st.text_input('mean perimeter')
        
    with col1:
    	mean_area=st.text_input('mean area')    
    
    with col2:
    	mean_smoothness=st.text_input('mean smoothness')    
        
    with col3:
   	    mean_compactness=st.text_input('BMI Value') 
        
    with col1:
   	    mean_concavity=st.text_input('mean concavity')
        
    with col2:
    	mean_concave_points=st.text_input('Nmean concave points')
        
    with col3:
    	mean_symmetry=st.text_input('mean symmetry')
       
    with col1:
    	mean_fractal_dimension=st.text_input('mean fractal dimension')
        
    with col2:
   	    radius_error=st.text_input('radius errore')    
    
    with col3:
    	texture_error=st.text_input('texture error')    
        
    with col1:
   	    perimeter_error=st.text_input('perimeter error') 
        
    with col2:
   	    area_error=st.text_input('area error') 
                                   
    with col3:
        smoothness_error=st.text_input('smoothness error')    
        
    with col1:
        compactness_error=st.text_input('compactness error') 
        
    with col2:
   	    concavity_error=st.text_input('concavity error')
        
    with col3:
    	concave_points_error=st.text_input('concave points error ')
        
    with col1:
    	symmetry_error=st.text_input('symmetry error')
       
    with col2:
    	fractal_dimension_error=st.text_input('fractal dimension error')
        
    with col3:
   	     worst_radius=st.text_input('worst radius') 
        
    with col1:
        worst_texture=st.text_input('worst texture')
        
    with col2:
   	    worst_perimeter=st.text_input('worst perimeter')
        
    with col3:
    	worst_area=st.text_input('worst area')
       
    with col1:
    	worst_smoothness=st.text_input('worst smoothness')
    
    with col2:
   	    worst_compactness=st.text_input('compactness') 
        
    with col3:
        worst_concavity=st.text_input('concavity ')
        
    with col1:
   	    worst_concave_points=st.text_input('concave points')
        
    with col2:
    	worst_symmetry=st.text_input('worst symmetry')
       
    with col3:
    	worst_fractal_dimension=st.text_input('worst fractal dimension ')                           
                                
                                
    diadiagnose=''
   
    if st.button('Breast Cancer Prediction Result'):
       diapred=breast_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error, worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
       
       if(diapred[0]==1):
           diadiagnose='Breast Cancer Predicted'
           
       else:
           diadiagnose='Breast Cancer Not Predicted'
           
    st.success(diadiagnose)


if(selec=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    
    
    with col1:
    	age=st.text_input('age')
        
    with col2:
    	sex=st.text_input('sex')
       
    with col3:
    	chest_pain_type=st.text_input('chest_pain_type')
        
    with col1:
    	resting_blood_pressure=st.text_input('resting_blood_pressure Value')    
    
    with col2:
    	cholestoral=st.text_input('cholestoral Level')    
        
    with col3:
    	fasting_blood_sugar=st.text_input('fasting_blood_sugar= Value') 
        
    with col1:
    	rest_ecg=st.text_input('rest_ecg Value')
    
    
    with col1:
    	Max_heart_rate=st.text_input('Max_heart_rate')
        
    with col2:
    	exercise_induced_angina =st.text_input('exercise_induced_angina')
       
    with col3:
    	oldpeak=st.text_input('oldpeak Level')
        
    with col1:
    	slope=st.text_input('slope Value')    
    
    with col2:
    	vessels_colored_by_flourosopy =st.text_input('vessels_colored_by_flourosopy')    
        
    with col3:
        thlassemia =st.text_input('mean thalassemia') 
        
       
       
    di_diagnose=''
   
    if st.button('Heart Disease Prediction Result'):
       di_pred=heart_model.predict([[age,sex,chest_pain_type,resting_blood_pressure,cholestoral,fasting_blood_sugar,rest_ecg,Max_heart_rate,exercise_induced_angina,oldpeak,slope,vessels_colored_by_flourosopy,thalassemia]])
       
       if(di_pred[0]==1):
           di_diagnose='Heart Disease diagnosed'
           
       else:
           di_diagnose='No Heart Disease diagnosed'
           
           
    st.success(di_diagnose)

if(selec=='Parkinson Prediction'):
   st.title('Parkinson Prediction using ML')
   col1,col2,col3=st.columns(3)
   
   
   with col1:
   	name=st.text_input('name')
       
   with col2:
   	MDVP_Fo=st.text_input('MDVP:Fo(Hz)')
      
   with col3:
  	 MDVP_Fhi=st.text_input('MDVP:Fhi(Hz)')
       
   with col1:
   	MDVP_Flo =st.text_input('MDVP:Flo(Hz)')    
   
   with col2:
    MDVP_Jitter=st.text_input('MDVP:Jitter(%)')
   	      
       
   with col3:
   	MDVP_Jitters=st.text_input('MDVP:Jitter(Abs)') 
       
   with col1:
   	MDVP_RAP=st.text_input('MDVP:RAP Value')
   with col1:
   	MDVP_PPQ=st.text_input('MDVP:PPQ')
       
   with col2:
   	Jitter_DDP=st.text_input('Jitter:DDP')
      
   with col3:
   	MDVP_Shimmer=st.text_input('MDVP:Shimmer')
       
   with col1:
   	MDVP_Shimmers=st.text_input('MDVP:Shimmer(dB)')    
   
   with col2:
   	Shimmer_APQ3=st.text_input('Shimmer:APQ3')    
       
   with col3:
   	Shimmer_APQ5 =st.text_input('Shimmer:APQ5') 
       
   with col1:
   	MDVP_APQ=st.text_input('MDVP:APQ')    

   with col2:
   	Shimmer_DDA=st.text_input('Shimmer:DDA')
       
   with col3:
   	NHR=st.text_input('NHR')
      
   with col1:
   	 HNR=st.text_input('HNR')  

   with col3:
   	RPDE =st.text_input('RPDE  Level')    
       
   with col1:
   	DFA=st.text_input('DFA Value') 
       
   with col2:
   	 spread=st.text_input('spread1 Value')
        
   with col3:
   	 spreads=st.text_input('spread2 Value')
       
   with col1:
   	D2=st.text_input('D2 Level')    
       
   with col2:
   	PPE=st.text_input('PPE Value')
   d_diagnose=''
  
   if st.button('Parkinson prediction Result'):
      d_pred=parkinson_model.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Jitters,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmers,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,status,RPDE,DFA,spread,spreads,D2,PPE]])
      
      if(d_pred[0]==1):
          d_diagnose='Parkinson Disease present'
          
      else:
          d_diagnose='Parkinson Disease not present'
          
          
          
   st.success(d_diagnose)
    
    
    
    
