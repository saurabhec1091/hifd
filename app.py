# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:54:38 2020

@author: IHA
"""


import streamlit as st
import pandas as pd
import numpy as np
import joblib 
import streamlit.components.v1 as components
from PIL import Image
img= Image.open('logo.jpeg')  
st.beta_set_page_config(page_title='Health Insurance ',page_icon=img, layout = 'wide', initial_sidebar_state = 'auto')

image = Image.open('logo1.png')
st.image(image)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

footer_temp = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div class="row">
	        <div class="col l6 s12">
	          <h5 class="white-text">Iha Consulting Services</h5>
	          <p class="grey-text text-lighten-4">Health Insurance Fraud Detection under Pragyan.</p>
	        </div>
	      
	   <div class="col l3 s12">
	          <h5 class="white-text">Connect With Us</h5>
	          <ul>
	          <a href="https://www.linkedin.com/company/iha-consulting-services-pvt-ltd/about/" target="_blank" class="white-text">
	            <i class="fab fa-linkedin fa-4x"></i>
	          </a>
	          <a href="info@ihaconsulting.in" target="_blank" class="white-text">
	            <i class="fa fa-envelope-square fa-4x"></i>
	          </a>
	           <a href="Call Us +91-40-48538611" target="_blank" class="white-text">
	            <i class="fa fa-phone-square fa-4x"></i>
	          </a>
	          </ul>
	        </div>
	      </div>
	    </div>
	    <div class="footer-copyright">
	      <div class="container">
	      Made by <a class="white-text text-lighten-3">Abhishek Singh, Dev Gupta & Saurabh Verma</a><br/>
	      <a class="white-text text-lighten-3">Pragyan @Iha Consulting Services</a>
	      </div>
	    </div>
	  </footer>
	"""


def home():
    #Setting the title    
    st.markdown("***Health Insurances: Why?***")
    st.markdown("In a recent article of World Health Organisation they stated certain facts which must be given importance so that we can understand the need of Health Insurances. They stated that by 2025, 8% of all deaths will be in the under-5s, 3% among 5-19 year-olds, 27% among 20-64 year-olds and 63% among the over-65s and also provided the leading causes of these global deaths in 1997 are follows:")
    dic ={'Cause':['Infectious and parasitic diseases','Circulatory diseases','Cancer','Respiratory diseases(chronic obstructive pulmonary disease)','Perinatal conditions','Respiratory infections','Tuberculosis','Diarrhoea','Hiv/aids','Malaria','Coronary heart disease','Cerebrovascular disease'],'Deaths(in Millions)':[17.3,15.3,6.2,2.9,3.6,3.7,2.9,2.5,2.3,2.0,7.2,4.6]}
    df_1 = pd.DataFrame(dic)
    st.dataframe(data=df_1, width=700, height=768)
    st.markdown("Now several more disease could be added into the list and this shows that we will require a good medical service to survive. But Medical Service costs are constantly increasing and with the ever rising instances of diseases, Health insurance today is a necessity.")
    st.markdown("Health insurance provides people with a much needed financial backup at times of medical emergencies, but it is an observed fact that till date, medical care in our country still remains largely as an expensive affair. According to various reports, India still continues to have the lowest health insurance penetration in the world. However, government's focus towards health schemes, new initiatives like, Ayushman Bharat Yojana, and capital expenditure towards healthcare may ameliorate the situation")
    
    st.markdown("***Scope of the Project***")
    st.markdown("In an Outlook article it was stated as “India is a huge market for insurance but the industry is bleeding losses due to fraud. Insurance fraud leads to around Rs 40,000 crore every year and makes up for 8.5 per cent of the revenue that the industry generates” Being such a necessity, Health Insurance Firms are still facing losses due to these frauds which cause firms to increase the premiums and lower the profits for the customer which will lead to create tension in the industry.")
    st.markdown("Now let’s understand what these frauds are:")
    st.markdown("IRDAI classified insurance frauds into:")
    st.markdown("    - **a.   Policyholder Fraud and/or Claims Fraud** - Fraud against the insurer in the purchase and/or execution of an insurance product, including fraud at the time of making a claim.")
    st.markdown("    - **b. Intermediary Fraud** - Fraud perpetuated by an insurance agent/Corporate Agent/intermediary/Third Party Administrators (TPAs) against the insurer and/or policyholders.")
    st.markdown("    - **c.   Internal Fraud** – Fraud/ mis-appropriation against the insurer by its Director, Manager and/or any other officer or staff member (by whatever name called).")
    st.markdown("And there are several possible ways to detect the frauds to save the firm from losses and that would be the scope of the project to detect the Frauds in a Health Insurance Firm on these three measures and also optimise the process of Health Insurance Fraud Detection by eliminating loopholes in the process.") 
    
    st.markdown("***Objective of the Project***")

    st.markdown("Some of the most common methods implemented by insurers to tackle the menace are:")
    st.markdown("    - Investigation and cross checks of documents to detect the fraud.")
    st.markdown("    - Knowing the potential of fraud: can help minimise the loss")
    st.markdown("    - Use of data analytics to detect fraud")
    st.markdown("    - Running through special investigation of every doubtful claim")          
    st.markdown("    - Allocating private investigators")           
    st.markdown("All of the above process could be time taking and might require lots of resources and expenses but here our objective will be using Data Science and Machine Learning to detect Frauds which will apply Statistical Inferences to the Data and will lead us detect pattern for the fraud claims made and also providing an easy user interface for making it accessible to every person and it won’t require technical knowledge and with a simple form entry, our app would be able to tell that the provided case is fraud or no. Also while studying the project we will we rectifying the loopholes and diving deep as much as we can to diminish the losses and no. of fraud cases.")
def inpatient():          
# loading in the model to predict on the data 
    st.markdown('## According to claim details')
    scaling = joblib.load('scale.pkl')
    classifier = joblib.load('inpatient.pkl')
    
    feat = {'4019': 0 ,'486': 0,'496' : 0,'53081' : 0,'5849' : 0,'5990' : 0,'ChronicCond_Alzheimer' : 0,'ChronicCond_Heartfailure' : 0,
            'ChronicCond_KidneyDisease' : 0,'ChronicCond_Osteoporasis' : 0, 'ChronicCond_rheumatoidarthritis' : 0, 
            'County_160' : 0, 'Gender' : 0, 'IPAnnualDeductibleAmt' : 0, 'IPAnnualReimbursementAmt' : 0, 'InscClaimAmtReimbursed' : 0, 
            'OPAnnualDeductibleAmt' : 0, 'OPAnnualReimbursementAmt' : 0 ,'Race_1' : 0,
            'DOB_Month_5': 0, 'County_130':0,
            'State_17' : 0, 'State_28' : 0, 'State_33' : 0, 'State_36' : 0, 'State_39' : 0, 'TreatmentDuration' : 0, 'no_of_codes' : 0}
    
    
    
    X = pd.read_csv('inpatient.csv')    
    
    st.text("Answer the question below:")
    
    #ChronicCond
    ChronicCond = st.selectbox("Select Chronic Condition",('Alzheimer','Heartfailure','KidneyDisease','Osteoporasis','rheumatoidarthritis'))
    feat['ChronicCond_'+str(ChronicCond)] = 1
    
    #County    
    County_160 = st.selectbox('County', ("160","Other"))
    if County_160 != 'Other':
        feat['County_'+str(County_160)] = 1
        
    #State
    State = st.selectbox('Select State Number',('17','28','33','36','39','Other'))
    if State!='Other':
        feat['State_'+str(State)] = 1
    
    #Race    
    Race = st.selectbox('Select Race', ("1","2","3","4","5","Not Apllicable"))
    if Race == '1':
        feat['Race_1'] = 1
        
    #Gender
    Gender = st.selectbox('Gender', ("Male","Female"))
    if Gender == 'Male':
        feat['Gender'] = 1
        
    #DOB
    DOB = st.date_input('Date of Birth:')
    if DOB.month == 5:
        feat['DOB_Month_5'] = 1
       
    
        
    #treatment duration
    AdmissionDt = st.date_input('Admission Date:')
    DischargeDt = st.date_input('Discharge Date:')
    if AdmissionDt < DischargeDt:
        st.success('Start date: `%s`\n\nEnd date:`%s`' % (AdmissionDt, DischargeDt))
    else:
        st.error('Error: End date must fall after start date.')
    feat['TreatmentDuration'] = (DischargeDt - AdmissionDt).days       
       
    #IPAnnualDeductibleAmt
    feat['IPAnnualDeductibleAmt']= st.slider('IPAnnualDeductibleAmt', int(round(X.IPAnnualDeductibleAmt.min())), int(round(X.IPAnnualDeductibleAmt.max())))
    
    #IPAnnualReimbursementAmt
    feat['IPAnnualReimbursementAmt'] = st.slider('IPAnnualReimbursementAmt', int(round(X.IPAnnualReimbursementAmt.min())), int(round(X.IPAnnualReimbursementAmt.max())))
    
    #InscClaimAmtReimbursed
    feat['InscClaimAmtReimbursed'] = st.slider('InscClaimAmtReimbursed',  int(round(X.InscClaimAmtReimbursed.min())), int(round(X.InscClaimAmtReimbursed.max())))
    
    #OPAnnualDeductibleAmt
    feat['OPAnnualDeductibleAmt'] = st.slider('OPAnnualDeductibleAmt',  int(round(X.OPAnnualDeductibleAmt.min())), int(round(X.OPAnnualDeductibleAmt.max())))
    
    #OPAnnualReimbursementAmt 
    feat['OPAnnualReimbursementAmt'] = st.slider('OPAnnualReimbursementAmt',  int(round(X.OPAnnualReimbursementAmt.min())), int(round(X.OPAnnualReimbursementAmt.max())))
    
    #PHY431177
    #PHY = st.sidebar.selectbox('Was PHY431177 your attending//operating/other physician', ("Yes","No"))
    #if PHY == 'Yes':
    #    feat['PHY431177'] = 1
    
    
        
    #Procedure Codes:
    Pro = st.text_input("Enter all the procedure codes separated by '/' ")
    p = Pro.split('/')
    
    #Diagnosis Codes:
    Dia = st.text_input("Enter all the diagnosis codes separated by '/' ")
    d = Dia.split('/')
    
    #no_of_codes
    feat['no_of_codes'] = 5-len(d)
    
    #'4019'
    if '4019' in p+d:
        feat['4019'] = 1
    
    #'486'
    if '486' in p+d:
        feat['486'] = 1
    
    
    #'496'
    if '496' in p+d:
        feat['496'] = 1
    
    #'53081'
    if '53081' in p+d:
        feat['53081'] = 1
    
    #'5849'
    if '5849' in p+d:
        feat['5849'] = 1
      
    #'5990'
    if '5990' in p+d:
        feat['5990'] = 1
        
      
     
    st.markdown('***Details you entered***') 
    
    
    st.dataframe(pd.DataFrame(feat, index=[0]).T)
        
        
    ##------------------------------------------------------------------------------------------------------------------------##
    ##------------------------------------------------------------------------------------------------------------------------##
    ##------------------------------------------------------------------------------------------------------------------------##
    ##------------------------------------------------------------------------------------------------------------------------##    
    features = pd.DataFrame(feat, index=[0])
    
    Xscaled = pd.DataFrame(scaling.transform(features),columns=features.columns)
    
    if st.button('Submit'):
        result = classifier.predict(Xscaled)
        if result == 1.0:
            st.write('**This is a Fraud Claim.**')
        else :
            st.write('**This is not a Fraud Claim.**')

def provider():
    st.markdown('## According to Provider details')
    feat = {'Provider':[], 'BeneID':[], 'ClaimID':[], 'ClmDiagnosisCode_7':[], 'ClmDiagnosisCode_8':[],
            'AttendingPhysician':[],'AdmitForDays':[], 'InscClaimAmtReimbursed':[],
       'ClmAdmitDiagnosisCode':[], 'DeductibleAmtPaid':[], 'ClmDiagnosisCode_1':[], 'ClmProcedureCode_2':[],
       'ClmProcedureCode_1':[],'IPAnnualDeductibleAmt':[], 'OPAnnualDeductibleAmt':[], 'DiagnosisGroupCode':[],
       'OperatingPhysician':[],'IPAnnualReimbursementAmt':[]}
    
    #Provider:
    pro = st.text_input("Enter the provider code:")
    
    #no-of-records:
    no = st.text_input("Enter the number of records:")
    if no != '':
        no = int(no)
    else:
        no = 1
    
    
    
    for i in range(1,no+1):
        
        feat['Provider'].append(pro)   
    
        #BeneID:
        BeneID = st.text_input("Enter the Beneficeray code for claim number {}".format(i))
        feat['BeneID'].append(BeneID)
        
        #ClaimID:
        ClaimID = st.text_input("Enter the Claim code for claim number {}".format(i))
        feat['ClaimID'].append(ClaimID)
        
        #OperatingPhysician:
        OperatingPhysician = st.text_input("Enter the name of operating physician for claim number {}".format(i))
        feat['OperatingPhysician'].append(OperatingPhysician)
        
        #AttendingPhysician:
        AttendingPhysician = st.text_input("Enter the name of attending physician for claim number {}".format(i))
        feat['AttendingPhysician'].append(AttendingPhysician)
        
        #AdmitForDays
        AdmissionDt = st.date_input('Admission Date for claim number {}'.format(i))
        DischargeDt = st.date_input('Discharge Date for claim number {}'.format(i))
        if AdmissionDt <= DischargeDt:
            st.success('Start date: `%s`\n\nEnd date:`%s`' % (AdmissionDt, DischargeDt))
        else:
            st.error('Error: End date must fall after start date.')
        feat['AdmitForDays'].append((DischargeDt - AdmissionDt).days + 1)   
        
        X = pd.read_csv('provider.csv')    
    
        #InscClaimAmtReimbursed
        feat['InscClaimAmtReimbursed'].append(st.slider("InscClaimAmtReimbursed for claim number {}".format(i), int(round(X.InscClaimAmtReimbursed.min())), int(round(X.InscClaimAmtReimbursed.max()))))    
    
        #IPAnnualDeductibleAmt
        feat['DeductibleAmtPaid'].append(st.slider('DeductibleAmtPaid for claim number {}'.format(i), int(round(X.DeductibleAmtPaid.min())), int(round(X.DeductibleAmtPaid.max()))))
        
        #IPAnnualReimbursementAmt
        feat['IPAnnualDeductibleAmt'].append(st.slider('IPAnnualDeductibleAmt for claim number {}'.format(i), int(round(X.IPAnnualDeductibleAmt.min())), int(round(X.IPAnnualDeductibleAmt.max()))))
        
        #InscClaimAmtReimbursed
        feat['OPAnnualDeductibleAmt'].append(st.slider('OPAnnualDeductibleAmt for claim number {}'.format(i),  int(round(X.OPAnnualDeductibleAmt.min())), int(round(X.OPAnnualDeductibleAmt.max()))))
        
        #OPAnnualDeductibleAmt
        feat['IPAnnualReimbursementAmt'].append(st.slider('IPAnnualReimbursementAmt for claim number {}'.format(i),  int(round(X.IPAnnualReimbursementAmt.min())), int(round(X.IPAnnualReimbursementAmt.max()))))
        
        #ClmAdmitDiagnosisCode
        feat['ClmAdmitDiagnosisCode'].append(st.selectbox('Select ClmAdmitDiagnosisCode for claim number {}'.format(i), X.ClmAdmitDiagnosisCode.unique()))
        
        #DiagnosisGroupCode
        feat['DiagnosisGroupCode'].append(st.selectbox('Select DiagnosisGroupCode for claim number {}'.format(i), X.DiagnosisGroupCode.unique()))
        
        #ClmDiagnosisCode_1
        feat['ClmDiagnosisCode_1'].append(st.selectbox('Select ClmDiagnosisCode_1 for claim number {}'.format(i), X.ClmDiagnosisCode_1.unique()))
        
        #ClmDiagnosisCode_7
        feat['ClmDiagnosisCode_7'].append(st.selectbox('Select ClmDiagnosisCode_7 for claim number {}'.format(i), X.ClmDiagnosisCode_7.unique()))
        
        #ClmDiagnosisCode_8
        feat['ClmDiagnosisCode_8'].append(st.selectbox('Select ClmDiagnosisCode_8 for claim number {}'.format(i), X.ClmDiagnosisCode_8.unique()))
        
        #ClmProcedureCode_1
        feat['ClmProcedureCode_1'].append(st.selectbox('Select ClmProcedureCode_1 for claim number {}'.format(i), X.ClmProcedureCode_1.unique()))
        
        #ClmProcedureCode_2
        feat['ClmProcedureCode_2'].append(st.selectbox('Select ClmProcedureCode_2 for claim number {}'.format(i), X.ClmProcedureCode_2.unique()))
    
    if st.checkbox('Submit'):
        try:
            st.dataframe(pd.DataFrame(feat, index=[0]))
            Train_ProviderWithPatientDetailsdata = pd.DataFrame(feat, index=[0])
            
            Train_ProviderWithPatientDetailsdata["PerProviderAvg_InscClaimAmtReimbursed"]=Train_ProviderWithPatientDetailsdata.groupby('Provider')['InscClaimAmtReimbursed'].transform('mean')
            
            ## Grouping based on BeneID explains amounts involved per beneficiary.Reason to derive this feature is that one beneficiary
            ## can go to multiple providers and can be involved in fraud cases
            
            
            ##Average features grouped by OperatingPhysician
            Train_ProviderWithPatientDetailsdata["PerOperatingPhysicianAvg_IPAnnualReimbursementAmt"]=Train_ProviderWithPatientDetailsdata.groupby('OperatingPhysician')['IPAnnualReimbursementAmt'].transform('mean')
            Train_ProviderWithPatientDetailsdata["PerOperatingPhysicianAvg_InscClaimAmtReimbursed"]=Train_ProviderWithPatientDetailsdata.groupby('OperatingPhysician')['InscClaimAmtReimbursed'].transform('mean')
            Train_ProviderWithPatientDetailsdata["PerOperatingPhysicianAvg_AdmitForDays"]=Train_ProviderWithPatientDetailsdata.groupby('OperatingPhysician')['AdmitForDays'].transform('mean')
            
            ### Average features grouped by AttendingPhysician
            
            Train_ProviderWithPatientDetailsdata["PerAttendingPhysicianAvg_InscClaimAmtReimbursed"]=Train_ProviderWithPatientDetailsdata.groupby('AttendingPhysician')['InscClaimAmtReimbursed'].transform('mean')
            Train_ProviderWithPatientDetailsdata["PerAttendingPhysicianAvg_AdmitForDays"]=Train_ProviderWithPatientDetailsdata.groupby('AttendingPhysician')['AdmitForDays'].transform('mean')
            
            ###  Average features grouped by DiagnosisGroupCode
            Train_ProviderWithPatientDetailsdata["PerDiagnosisGroupCodeAvg_OPAnnualDeductibleAmt"]=Train_ProviderWithPatientDetailsdata.groupby('DiagnosisGroupCode')['OPAnnualDeductibleAmt'].transform('mean')
            
            ### Average features grouped by ClmAdmitDiagnosisCode
            
            Train_ProviderWithPatientDetailsdata["PerClmAdmitDiagnosisCodeAvg_DeductibleAmtPaid"]=Train_ProviderWithPatientDetailsdata.groupby('ClmAdmitDiagnosisCode')['DeductibleAmtPaid'].transform('mean')
            Train_ProviderWithPatientDetailsdata["PerClmAdmitDiagnosisCodeAvg_InscClaimAmtReimbursed"]=Train_ProviderWithPatientDetailsdata.groupby('ClmAdmitDiagnosisCode')['InscClaimAmtReimbursed'].transform('mean')
            ### Average features grouped by ClmProcedureCode_1
            
            Train_ProviderWithPatientDetailsdata["PerClmProcedureCode_1Avg_IPAnnualDeductibleAmt"]=Train_ProviderWithPatientDetailsdata.groupby('ClmProcedureCode_1')['IPAnnualDeductibleAmt'].transform('mean')
            
            ### Average features grouped by ClmProcedureCode_2
            
            Train_ProviderWithPatientDetailsdata["PerClmProcedureCode_2Avg_DeductibleAmtPaid"]=Train_ProviderWithPatientDetailsdata.groupby('ClmProcedureCode_2')['DeductibleAmtPaid'].transform('mean')
            Train_ProviderWithPatientDetailsdata["PerClmProcedureCode_2Avg_OPAnnualDeductibleAmt"]=Train_ProviderWithPatientDetailsdata.groupby('ClmProcedureCode_2')['OPAnnualDeductibleAmt'].transform('mean')
            
            
            ### Average features grouped by ClmDiagnosisCode_1
            
            Train_ProviderWithPatientDetailsdata["PerClmDiagnosisCode_1Avg_DeductibleAmtPaid"]=Train_ProviderWithPatientDetailsdata.groupby('ClmDiagnosisCode_1')['DeductibleAmtPaid'].transform('mean')
            
            
            
            ### Average Feature based on grouping based on combinations of different variables
            
            Train_ProviderWithPatientDetailsdata["ClmCount_Provider_BeneID"]=Train_ProviderWithPatientDetailsdata.groupby(['Provider','BeneID'])['ClaimID'].transform('count')
            Train_ProviderWithPatientDetailsdata["ClmCount_Provider_ClmDiagnosisCode_7"]=Train_ProviderWithPatientDetailsdata.groupby(['Provider','ClmDiagnosisCode_7'])['ClaimID'].transform('count')
            Train_ProviderWithPatientDetailsdata["ClmCount_Provider_ClmDiagnosisCode_8"]=Train_ProviderWithPatientDetailsdata.groupby(['Provider','ClmDiagnosisCode_8'])['ClaimID'].transform('count')
            
            ##### Lets impute numeric columns with 0
            
            cols1 = Train_ProviderWithPatientDetailsdata.select_dtypes([np.number]).columns
            
            Train_ProviderWithPatientDetailsdata[cols1] = Train_ProviderWithPatientDetailsdata[cols1].fillna(value=0)
            # Lets remove unnecessary columns ,as we grouped based on these columns and derived maximum infromation from them.
            
            remove_these_columns = [ 'BeneID', 'ClaimID', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8', 'AttendingPhysician',
                   'AdmitForDays','ClmAdmitDiagnosisCode', 'DeductibleAmtPaid', 'ClmDiagnosisCode_1', 
                   'ClmProcedureCode_2', 'ClmProcedureCode_1',
                   'IPAnnualDeductibleAmt', 'OPAnnualDeductibleAmt', 'DiagnosisGroupCode', 'OperatingPhysician',
                   'IPAnnualReimbursementAmt']
            Train_category_removed=Train_ProviderWithPatientDetailsdata.drop(axis=1,columns=remove_these_columns)
            
            ### Lets aggregate claims data to unique providers.
            
            Train_category_removed_groupedbyProv_PF=Train_category_removed.groupby(['Provider'],as_index=False).agg('sum')
            
            X = Train_category_removed_groupedbyProv_PF
                
            X.drop('Provider',axis=1,inplace=True)
            # MinMaxScaler
            
            from sklearn.preprocessing import MinMaxScaler
            scaler = joblib.load('scaler_m.pkl')
            X = pd.DataFrame(scaler.transform(X),columns=X.columns)
            
            import xgboost
            classifier = joblib.load('xgb_model.pkl')
            result =  (classifier.predict_proba(X)[:,1]>0.5).astype(bool)
            if result == 1.0:
                st.write('**This is a Fraud Provider.**')
            else :
                st.write('**This is not a Fraud Claim.**')

        except ValueError:
            st.error('Invalid Data Entry')
            
def csv():
    st.markdown('## Use CSV for detection.')
    a = st.file_uploader('Provider', type="csv")
    b = st.file_uploader('Beneficiary', type="csv")
    c = st.file_uploader('Inpatient', type="csv")           
    d = st.file_uploader('Outpatient', type="csv")  
    if st.checkbox("Submit"):          
                
        Test = pd.read_csv(a)
        
        Test_Beneficiarydata= pd.read_csv(b)
    
        Test_Inpatientdata = pd.read_csv(c)
    
        Test_Outpatientdata = pd.read_csv(d)
    
        
        
        #data cleaning
    
        Test_Beneficiarydata = Test_Beneficiarydata.replace({'ChronicCond_Alzheimer': 2, 'ChronicCond_Heartfailure': 2, 'ChronicCond_KidneyDisease': 2,
                                   'ChronicCond_Cancer': 2, 'ChronicCond_ObstrPulmonary': 2, 'ChronicCond_Depression': 2,
                                   'ChronicCond_Diabetes': 2, 'ChronicCond_IschemicHeart': 2, 'ChronicCond_Osteoporasis': 2,
                                   'ChronicCond_rheumatoidarthritis': 2, 'ChronicCond_stroke': 2 }, 0)
            
    
        ## As patient can be admitted for only for 1 day,we will add 1 to the difference of Discharge Date and Admission Date
        
        Test_Inpatientdata['AdmissionDt'] = pd.to_datetime(Test_Inpatientdata['AdmissionDt'] , format = '%Y-%m-%d')
        Test_Inpatientdata['DischargeDt'] = pd.to_datetime(Test_Inpatientdata['DischargeDt'],format = '%Y-%m-%d')
        Test_Inpatientdata['AdmitForDays'] = ((Test_Inpatientdata['DischargeDt'] - Test_Inpatientdata['AdmissionDt']).dt.days)+1
        # Lets make union of Inpatienta and outpatient data .
        # We will use all keys in outpatient data as we want to make union and dont want duplicate columns from both tables.

        
        Test_Allpatientdata=pd.merge(Test_Outpatientdata,Test_Inpatientdata,
                                      left_on=['BeneID', 'ClaimID', 'ClaimStartDt', 'ClaimEndDt', 'Provider',
               'InscClaimAmtReimbursed', 'AttendingPhysician', 'OperatingPhysician',
               'OtherPhysician', 'ClmDiagnosisCode_1', 'ClmDiagnosisCode_2',
               'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5',
               'ClmDiagnosisCode_6', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8',
               'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10', 'ClmProcedureCode_1',
               'ClmProcedureCode_2', 'ClmProcedureCode_3', 'ClmProcedureCode_4',
               'ClmProcedureCode_5', 'ClmProcedureCode_6', 'DeductibleAmtPaid',
               'ClmAdmitDiagnosisCode'],
                                      right_on=['BeneID', 'ClaimID', 'ClaimStartDt', 'ClaimEndDt', 'Provider',
               'InscClaimAmtReimbursed', 'AttendingPhysician', 'OperatingPhysician',
               'OtherPhysician', 'ClmDiagnosisCode_1', 'ClmDiagnosisCode_2',
               'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5',
               'ClmDiagnosisCode_6', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8',
               'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10', 'ClmProcedureCode_1',
               'ClmProcedureCode_2', 'ClmProcedureCode_3', 'ClmProcedureCode_4',
               'ClmProcedureCode_5', 'ClmProcedureCode_6', 'DeductibleAmtPaid',
               'ClmAdmitDiagnosisCode']
                                      ,how='outer')
        
        Test_AllPatientDetailsdata=pd.merge(Test_Allpatientdata,Test_Beneficiarydata,left_on='BeneID',right_on='BeneID',how='inner')
        
        
        Test_ProviderWithPatientDetailsdata=pd.merge(Test,Test_AllPatientDetailsdata,on='Provider')
        
        col = ['Provider', 'BeneID', 'ClaimID', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8', 'AttendingPhysician',
               'AdmitForDays', 'InscClaimAmtReimbursed',
               'ClmAdmitDiagnosisCode', 'DeductibleAmtPaid', 'ClmDiagnosisCode_1', 'ClmProcedureCode_2', 'ClmProcedureCode_1',
               'IPAnnualDeductibleAmt', 'OPAnnualDeductibleAmt', 'DiagnosisGroupCode', 'OperatingPhysician',
               'IPAnnualReimbursementAmt']
        Test_ProviderWithPatientDetailsdata = Test_ProviderWithPatientDetailsdata.loc[:,col]
        
        #PerClmAdmitDiagnosisCodeAvg_IPAnnualDeductibleAmt remove 
        
        Test_ProviderWithPatientDetailsdata["PerProviderAvg_InscClaimAmtReimbursed"]=Test_ProviderWithPatientDetailsdata.groupby('Provider')['InscClaimAmtReimbursed'].transform('mean')
        
        
        ##Average features grouped by OperatingPhysician
        Test_ProviderWithPatientDetailsdata["PerOperatingPhysicianAvg_IPAnnualReimbursementAmt"]=Test_ProviderWithPatientDetailsdata.groupby('OperatingPhysician')['IPAnnualReimbursementAmt'].transform('mean')
        Test_ProviderWithPatientDetailsdata["PerOperatingPhysicianAvg_InscClaimAmtReimbursed"]=Test_ProviderWithPatientDetailsdata.groupby('OperatingPhysician')['InscClaimAmtReimbursed'].transform('mean')
        Test_ProviderWithPatientDetailsdata["PerOperatingPhysicianAvg_AdmitForDays"]=Test_ProviderWithPatientDetailsdata.groupby('OperatingPhysician')['AdmitForDays'].transform('mean')
        
        ### Average features grouped by AttendingPhysician
        
        Test_ProviderWithPatientDetailsdata["PerAttendingPhysicianAvg_InscClaimAmtReimbursed"]=Test_ProviderWithPatientDetailsdata.groupby('AttendingPhysician')['InscClaimAmtReimbursed'].transform('mean')
        Test_ProviderWithPatientDetailsdata["PerAttendingPhysicianAvg_AdmitForDays"]=Test_ProviderWithPatientDetailsdata.groupby('AttendingPhysician')['AdmitForDays'].transform('mean')
        
        ###  Average features grouped by DiagnosisGroupCode
        Test_ProviderWithPatientDetailsdata["PerDiagnosisGroupCodeAvg_OPAnnualDeductibleAmt"]=Test_ProviderWithPatientDetailsdata.groupby('DiagnosisGroupCode')['OPAnnualDeductibleAmt'].transform('mean')
        
        ### Average features grouped by ClmAdmitDiagnosisCode
        
        Test_ProviderWithPatientDetailsdata["PerClmAdmitDiagnosisCodeAvg_DeductibleAmtPaid"]=Test_ProviderWithPatientDetailsdata.groupby('ClmAdmitDiagnosisCode')['DeductibleAmtPaid'].transform('mean')
        Test_ProviderWithPatientDetailsdata["PerClmAdmitDiagnosisCodeAvg_InscClaimAmtReimbursed"]=Test_ProviderWithPatientDetailsdata.groupby('ClmAdmitDiagnosisCode')['InscClaimAmtReimbursed'].transform('mean')
        ### Average features grouped by ClmProcedureCode_1
        
        Test_ProviderWithPatientDetailsdata["PerClmProcedureCode_1Avg_IPAnnualDeductibleAmt"]=Test_ProviderWithPatientDetailsdata.groupby('ClmProcedureCode_1')['IPAnnualDeductibleAmt'].transform('mean')
        
        ### Average features grouped by ClmProcedureCode_2
        
        Test_ProviderWithPatientDetailsdata["PerClmProcedureCode_2Avg_DeductibleAmtPaid"]=Test_ProviderWithPatientDetailsdata.groupby('ClmProcedureCode_2')['DeductibleAmtPaid'].transform('mean')
        Test_ProviderWithPatientDetailsdata["PerClmProcedureCode_2Avg_OPAnnualDeductibleAmt"]=Test_ProviderWithPatientDetailsdata.groupby('ClmProcedureCode_2')['OPAnnualDeductibleAmt'].transform('mean')
        
        
        ### Average features grouped by ClmDiagnosisCode_1
        
        Test_ProviderWithPatientDetailsdata["PerClmDiagnosisCode_1Avg_DeductibleAmtPaid"]=Test_ProviderWithPatientDetailsdata.groupby('ClmDiagnosisCode_1')['DeductibleAmtPaid'].transform('mean')
        
        
        
        ### Average Feature based on grouping based on combinations of different variables
        
        Test_ProviderWithPatientDetailsdata["ClmCount_Provider_BeneID"]=Test_ProviderWithPatientDetailsdata.groupby(['Provider','BeneID'])['ClaimID'].transform('count')
        Test_ProviderWithPatientDetailsdata["ClmCount_Provider_ClmDiagnosisCode_7"]=Test_ProviderWithPatientDetailsdata.groupby(['Provider','ClmDiagnosisCode_7'])['ClaimID'].transform('count')
        Test_ProviderWithPatientDetailsdata["ClmCount_Provider_ClmDiagnosisCode_8"]=Test_ProviderWithPatientDetailsdata.groupby(['Provider','ClmDiagnosisCode_8'])['ClaimID'].transform('count')
        
        ##### Lets impute numeric columns with 0
        
        cols1 = Test_ProviderWithPatientDetailsdata.select_dtypes([np.number]).columns
        
        Test_ProviderWithPatientDetailsdata[cols1] = Test_ProviderWithPatientDetailsdata[cols1].fillna(value=0)
        # Lets remove unnecessary columns ,as we grouped based on these columns and derived maximum infromation from them.
        
        remove_these_columns = [ 'BeneID', 'ClaimID', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8', 'AttendingPhysician',
               'AdmitForDays',
               'ClmAdmitDiagnosisCode', 'DeductibleAmtPaid', 'ClmDiagnosisCode_1', 'ClmProcedureCode_2', 'ClmProcedureCode_1',
               'IPAnnualDeductibleAmt', 'OPAnnualDeductibleAmt', 'DiagnosisGroupCode', 'OperatingPhysician',
               'IPAnnualReimbursementAmt']
        Test_category_removed=Test_ProviderWithPatientDetailsdata.drop(axis=1,columns=remove_these_columns)
        
        ### Lets aggregate claims data to unique providers.
        
        Test_category_removed_groupedbyProv_PF=Test_category_removed.groupby(['Provider'],as_index=False).agg('sum')
        Test_category_removed_groupedbyProv_PF= Test_category_removed_groupedbyProv_PF.drop(axis=1,columns='Provider')
        
        # MinMaxScaler
        
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler().fit(Test_category_removed_groupedbyProv_PF)
        X = pd.DataFrame(scaler.transform(Test_category_removed_groupedbyProv_PF),columns=Test_category_removed_groupedbyProv_PF.columns)
        
        # load the model from disk
        
        loaded_model = joblib.load('xgb_model.pkl')
        result = (loaded_model.predict_proba(X)[:,1]>0.5).astype(bool)
        Test['Fraud'] = result
        st.dataframe(Test.replace({'Fraud': {0: 'No', 1: 'Yes'}}))
            
    
# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()



def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


def main():
    st.title("Health Insurance Fraud Detection") 
    menu = ["Home","Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

      
    if choice == "Home":
        home()
    
    elif choice == "Login":
        st.sidebar.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            #if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                st.sidebar.success("Logged In as {}".format(username))
                task = st.sidebar.radio("Task",["Analysis", "Claim Fraud Detection","Provider Fraud Detection"])
                if task == 'Analysis':
                    analysis()
                if task == 'Claim Fraud Detection':
                    inpatient()
                if task == "Provider Fraud Detection":
                    pro = st.sidebar.radio('Detection using',('live form filling','CSV file upload'))
                    if pro == 'live form filling':
                        provider()
                    if pro == 'CSV file upload':
                        csv()
            else:
                st.warning("Incorrect Username/Password")


    elif choice == "SignUp":
        home()
        st.sidebar.subheader("Create New Account")
        new_user = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password",type='password')

        if st.sidebar.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.sidebar.success("You have successfully created a valid Account")
            st.sidebar.info("Go to Login Menu to login")

    components.html(footer_temp,height=500)




from pandas_profiling import ProfileReport 
from streamlit_pandas_profiling import st_profile_report


def analysis():
    Train = pd.read_csv('train_data.csv')
    Train_Beneficiarydata = pd.read_csv('Train_Beneficiarydata.csv')
    Train_Inpatientdata= pd.read_csv('Train_Inpatientdata.csv')
    Train_Outpatientdata = pd.read_csv('Train_Outpatientdata.csv')
    Train_ProviderWithPatientDetailsdata= pd.read_csv('Train_ProviderWithPatientDetailsdata.csv')

    
    st.markdown('## Some Facts and analysis')
                
    st.markdown('**First of all we were provided with four data files so lets explore!!**')
                
    
    df = st.selectbox('Get the Univariate Analysis Report of :',['Train','Beneficiary Data','Inpatient Data','Outpatient Data'])
    if st.checkbox('Display'):
        if df == 'Train':
            profile = ProfileReport(Train)
            st_profile_report(profile)
        if df == 'Beneficiary Data':
            profile = ProfileReport(Train_Beneficiarydata)
            st_profile_report(profile)
        if df == 'Inpatient Data':
            profile = ProfileReport(Train_Inpatientdata)
            st_profile_report(profile)
        if df == 'Outpatient Data':
            profile = ProfileReport(Train_Outpatientdata)
            st_profile_report(profile)
            
    
    st.markdown('### Major Data Cleaning steps are')
    
    st.markdown("    - Create a new variable 'WhetherDead' with flag 1 means Dead and 0 means not Dead")
    st.markdown("    - As patient can be admitted for only for 1 day,we will add 1 to the difference of Discharge Date and Admission Date")
    
    
    st.markdown("### Merging Dataframes")
    st.markdown("Made union of Inpatienta and outpatient data . We will use all keys in outpatient data as we want to make union and dont want duplicate columns from both tables. The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes will be ignored. Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on. Then merge All patient data with beneficiary details data based on 'BeneID' as joining key for inner join.")
    
    
    st.markdown('### While exploring these useful insights were observed')
                
                
    st.markdown('#### Claim per Beneficiary')
    
    import seaborn as sns
    import matplotlib.pyplot as plt
    st.set_option('deprecation.showPyplotGlobalUse', False)
                
    sns.countplot(Train_ProviderWithPatientDetailsdata.BeneID.value_counts())
    plt.rcParams['figure.figsize'] = (15,9)
    plt.xticks(rotation = 90,fontsize=12)
    plt.title("Claim count vs no of Beneficiary")
    plt.xlabel(" No of claim")
    plt.ylabel("Count of Beneficiary ")
    st.markdown('##### Beneficiary  claim 29 times which were highest claim but few beneficiary. Most of beneficiary had done one time claim which maybe safe claim.')
    st.pyplot()
    
    st.markdown('#### PLotting the frequencies of Statewise beneficiaries')
    count_States = pd.value_counts(Train_Beneficiarydata['State'], sort = True)
    plt.figure(figsize=(20, 22))
    #Drawing a barplot
    (count_States*100/len(Train_Beneficiarydata)).plot(kind = 'bar', rot=0,figsize=(16,8),fontsize=12,legend=True)
    #Giving titles and labels to the plot
    
    plt.yticks(np.arange(0,10,2))
    plt.title("Per State Beneficiary Distribution",fontsize=18)
    plt.xlabel("State Number",fontsize=15)
    plt.ylabel("Percentage of Beneficiaries "'%',fontsize=15)
    st.markdown('##### 80 percentage of beneficiary were present in state 5 . Few beneficary were present in state 0 and 2 so we can increased selling insurance in these state . ')
    st.pyplot()
    
    st.markdown('#### PLotting the frequencies of Per Race beneficiaries')
    count_Race = pd.value_counts(Train_Beneficiarydata['Race'], sort = True)
    
    #Drawing a barplot
    (count_Race*100/len(Train_Beneficiarydata)).plot(kind = 'bar', rot=0,figsize=(10,6),fontsize=12)

    plt.yticks(np.arange(0,100,20))
    plt.title("Race - wise Beneficiary Distribution",fontsize=18)
    plt.xlabel("Race Code",fontsize=15)
    plt.ylabel("Percentage of Beneficiaries "'%',fontsize=15)
    st.markdown('##### Race 1 category have 80 percentage of beneficiary and race 4 were few beneficiary. We can concentrate on race 1 category claims . ')
    st.pyplot()
    
    st.markdown('#### Plot countplot for each fraud and non fraud categories Top-10 Procedures involved in Healthcare Fraud')    
    
    sns.set(rc={'figure.figsize': (12, 8)}, style='white')
    
    ax = sns.countplot(x='ClmProcedureCode_1', hue='PotentialFraud', data=Train_ProviderWithPatientDetailsdata
                       , order=Train_ProviderWithPatientDetailsdata.ClmProcedureCode_1.value_counts().iloc[:10].index)
    
    plt.title('Top-10 Procedures invloved in Healthcare Fraud')
    st.markdown('##### In this graph we found 10 procedure which had significant fraud and procedure 9904 code have most fraud case.')
    st.pyplot()
    

    st.markdown('#### Plot Top-10 Claim Diagnosis  invloved in Healthcare Fraud')
    sns.set(rc={'figure.figsize':(12,8)},style='white')
    
    sns.countplot(x='ClmDiagnosisCode_1',hue='PotentialFraud',data=Train_ProviderWithPatientDetailsdata
                  ,order=Train_ProviderWithPatientDetailsdata.ClmDiagnosisCode_1.value_counts().iloc[:10].index)
    
    plt.title('Top-10 Diagnosis invloved in Healthcare Fraud')
    st.markdown('##### In this graph we found two significant diagnosis code involved in fraud. These diagnosis code have high non fraud case also.   ')
    st.pyplot()
    
    
    st.markdown('#### Plot Top-20 Attending Physicians involved in Healthcare Fraud')
    sns.set(rc={'figure.figsize': (12, 8)}, style='white')
    
    ax = sns.countplot(x='AttendingPhysician', hue='PotentialFraud', data=Train_ProviderWithPatientDetailsdata
                       , order=Train_ProviderWithPatientDetailsdata.AttendingPhysician.value_counts().iloc[:20].index)
    
    plt.title('Top-20 Attending physicians invloved in Healthcare Fraud')
    plt.xticks(rotation=90)
    st.markdown('#####  In this graph we were interpret that attending physician contributes in fraud. Physician PHY330576 had done huge amonut of fraud. 10 attending physician were involved in fraud only.')
    st.pyplot()
    
    st.markdown('#### Plot IPAnnualDeductibleAmt and IPAnnualReimbursementAmt in both fraud and non Fraud Categoories')
    sns.set(rc={'figure.figsize':(12,8)},style='white')
    
    sns.lmplot(x='IPAnnualDeductibleAmt',y='IPAnnualReimbursementAmt',hue='PotentialFraud',
               col='PotentialFraud',fit_reg=False,data=Train_ProviderWithPatientDetailsdata)
    st.markdown('##### In-patient annual deductible amount and in-patient annual reimbursement amount were followed same pattern and range between 0 to 10000 had most fraud claim found.')
    st.pyplot()
    plt.show()   
   
    st.markdown('#### Plot DeductibleAmtPaid and InsClaimAmtReimbursed in both fraud and non Fraud Categoories')
    sns.set(rc={'figure.figsize':(12,8)},style='white')
    
    sns.lmplot(x='DeductibleAmtPaid',y='InscClaimAmtReimbursed',hue='PotentialFraud',
               col='PotentialFraud',fit_reg=False,data=Train_ProviderWithPatientDetailsdata)
    st.markdown('##### In this graph we were interpret that deductible amount and reimbursed amount were not follow the unique pattern. There were not any effect of high and low Deductible amount and reimbursed amount.')
    st.pyplot()
    
    
    st.markdown('#### Age factor in Insurance Claim Amount Reimbursed')
    sns.set(rc={'figure.figsize':(16,10)},style='white')
    
    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    f.suptitle(' Age VS Insurance Claim Amount Reimbursed')
    ax1.scatter(Train_ProviderWithPatientDetailsdata[Train_ProviderWithPatientDetailsdata.PotentialFraud=='Yes'].Age,
                Train_ProviderWithPatientDetailsdata[Train_ProviderWithPatientDetailsdata.PotentialFraud=='Yes'].InscClaimAmtReimbursed)
    ax1.set_title('Fraud')
    ax1.axhline(y=60000,c='g')
    ax1.set_ylabel('Insurance Claim Amout Reimbursed')
    
    ax2.scatter(Train_ProviderWithPatientDetailsdata[Train_ProviderWithPatientDetailsdata.PotentialFraud=='No'].Age,
                Train_ProviderWithPatientDetailsdata[Train_ProviderWithPatientDetailsdata.PotentialFraud=='No'].InscClaimAmtReimbursed)
    ax2.set_title('Normal')
    ax2.axhline(y=60000,c='g')
    ax2.set_xlabel('Age (in Years)')
    ax2.set_ylabel('Insurance Claim Amout Reimbursed')
    
    st.markdown('##### In this graph we were interpret that most of claim which reimbursed amount were more than 60000 and age between 65 to 90 were fraud claim.   ')
    st.pyplot()
    
    #feature engineering
    st.markdown('### Feature Engineering')
    st.markdown('#### creating new feature were follow these following steps. ')
    st.markdown("    - Major feature were created continious variable tranformed by mean.")
    st.markdown("    - Grouping based on BeneID explains amounts involved per beneficiary.Reason to derive this feature is that one beneficiary can go to multiple providers and can be involved in fraud cases.")
    st.markdown("    - Continious features grouped by OtherPhysician,OperatingPhysician,AttendingPhysician,DiagnosisGroupCode,ClmAdmitDiagnosisCode,ClmProcedureCode and ClmDiagnosisCode.")
    st.markdown("    - Continious feature based on grouping based on combinations of different variables.")

    #feature selection
    st.markdown('### Feature Selection')
    st.markdown("#### Using different type of method ,We will also discover important feature helpful in detecting the behavior of potentially fraud.")
    st.markdown("    - Random Forest feature selection")
    st.markdown("    - WOE and IV transformation.")
    st.markdown("    - Recursive Feature Elimination")
    st.markdown("    - Extratrees Classifier")     
    st.markdown("    - Chi Square")
    st.markdown("    - L1 feature selection method")
    st.markdown("####  Using above method we selected 17 feature in which 16 feture were new developed features.")
    st.markdown("### Important Features which accountable  for potential fraud  provider:- ")
    st.markdown("    - InscClaimAmtReimbursed :- The insurer reimburses the expenses that you have incurred based on your sum assured limit.")
    st.markdown("    - AvgInscClaimAmtReimbursed_PerProvider :- Average insurance claim reimbursed amount on per providers. ")
    st.markdown("    - AvgIPAnnualReimbursementAmt_PerOperatingPhysician :- In patient average annual reimbursement amount on per operating physician.  ")
    st.markdown("    - AvgInscClaimAmtReimbursed_PerOperatingPhysician :- Average insurance claim reimbursed amount on per operating physician. ")
    st.markdown("    - AvgAdmitForDays_PerOperatingPhysician :- Average addmission days in hospital of insured on per operating physician.")
    st.markdown("    - AvgInscClaimAmtReimbursed_PerAttendingPhysician :- Average insurance claim reimbursed amount on per attending physician.")
    st.markdown("    - AvgAdmitForDays_PerAttendingPhysician :- Average addmission days in hospital of insured on per attending physician.")        
    st.markdown("    - AvgOPAnnualDeductibleAmt_PerDiagnosisGroupCode :-  Out patient average annual deductible amount on per diagnosis group code.")
    st.markdown("    - AvgDeductibleAmtPaid_PerClmAdmitDiagnosisCode :-  Average deductible amount paid on per claim admit diagnosis code.")
    st.markdown("    - AvgInscClaimAmtReimbursed_PerClmAdmitDiagnosisCode :- Average insurance claim reimbursed amount on per claim admit diagnosis code.")
    st.markdown("    - AvgIPAnnualDeductibleAmt_ PerClmProcedureCode_1 :- In patient average annual deductible amount on per claim procedure code 1.")
    st.markdown("    - AvgDeductibleAmtPaid_PerClmProcedureCode_2 :- Average deductible amount paid on per claim procedure code 2.")
    st.markdown("    - AvgOPAnnualDeductibleAmt_PerClmProcedureCode_2 :- Out patient average annual deductible amount on per claim procedure code 2. ")            
    st.markdown("    - AvgDeductibleAmtPaid_PerClmDiagnosisCode_1 :- Average deductible amount paid on per claim dianosis code 1." )           
    st.markdown("    - ClmCount_Provider_BeneID :- Number of claims of perticular beneficiary on per provider.")
    st.markdown("    - ClmCount_Provider_ClmDiagnosisCode_7 :- Number of claims of per provider on per claims diganosis code 7. " )          
    st.markdown("    - ClmCount_Provider_ClmDiagnosisCode_8 :- Number of claims of per provider on per claims diganosis code 8."  )          
                
if __name__ == '__main__':
	main()