import pandas as pd
import streamlit as st
import numpy as np
st.title("Collections Dashboard")
uploaded_file1 = st.sidebar.file_uploader("Choose a CSV file 1", type="csv")
if uploaded_file1:
    df1 = pd.read_csv(uploaded_file1)            
uploaded_file2 = st.sidebar.file_uploader("Choose a CSV file 2", type="csv")
if uploaded_file2:
    df2 = pd.read_csv(uploaded_file2)
uploaded_file3 = st.sidebar.file_uploader("Choose a CSV file 3", type="csv")
if uploaded_file3:
    df3 = pd.read_csv(uploaded_file3)
uploaded_file4 = st.sidebar.file_uploader("Choose a CSV file 4", type="csv")
if uploaded_file4:
    df4 = pd.read_csv(uploaded_file4)
dpdlist=["Less Than -7 DPD","Pre-EMI ( -7 DPD to 0 DPD)","1 -7 DPD","8 -15 DPD","16 -23 DPD","24 -30 DPD","31 -60 DPD","61 -90 DPD","90+ DPD"]  
statelist=["Karnataka","Maharashtra","Tamil Nadu","Gujarat","Delhi","Uttar Pradesh","Rajasthan","Madhya Pradesh","West Bengal","Telangana","Rest Of India"]
Contactabilitylist=["Yes","No"]
CollumnList=list(df1.columns.values)
s=[0,0,0,0]
def checknone(s1,s2,s3,s4):
  if(s1=="None"):
    s[0]=1
  if(s2=="None"):
    s[1]=1
  if(s3=="None"):
    s[2]=1
  if(s4=="None"):
    s[3]=1
def dpd(state1,state2,state3,state4,n1,n2,n3,n4,n5): 
  due=[0,0,0,0,0,0,0,0,0]
  total_due=[0,0,0,0,0,0,0,0,0]
  y=[0,0,0,0,0,0,0,0,0]
  n=[0,0,0,0,0,0,0,0,0]
  final_df = pd.DataFrame(columns = ['DPD', 'DUE','Collections','Percentage','Contactability','Non Contactability','Contactability%'])
  checknone(state1,state2,state3,state4)
  for i in range(0,len(df1)):
    c1=df1.loc[i][n1]
    c2=df1.loc[i][n2]
    c3=df1.loc[i][n3]
    c4=df1.loc[i][n4]
    a=df1.loc[i][43]  
    b=df1.loc[i][73]
    d=df1.loc[i][71]
    e=df1.loc[i][62]
    f=df1.loc[i][63]
    if ((c1==state1 or s[0]==1 ) and (c2==state2 or s[1]==1) and (state3==c3 or s[2]==1) and (((c4.find('cl',0)>=0 and n5==1) or (c4.find('cl',0)<0 and n5==0)) or s[3]==1)):
      for j in range(0,9):
        if (a==dpdlist[j]):
          due[j]=due[j]+int(b)
          total_due[j]=total_due[j]+int(d)
          if (e=="Y" and (not(f=="-"))) :
            y[j]=y[j]+1
          elif (e=="N" and (not(f=="-"))) :
            n[j]=n[j]+1
          break      
  for i in range(0,9) :
    temp1=due[i]
    temp2=y[i]+n[i]
    if (due[i]==0) :
      temp1=int(100000000000000000) 
    if (temp2==0) :
      temp2=int(100000000000000000)   
    final_df.loc[len(final_df.index)] = [dpdlist[i], due[i],total_due[i],str(round((total_due[i]*100/temp1),2))+" % ",y[i],n[i],str(round((y[i]*100/temp2),2))+" % "]
  st.write(final_df)
  due_sum,total_due_sum=0,0
  for i in range (0,9):
    due_sum =due_sum+due[i];
    total_due_sum=total_due_sum+total_due[i]; 
  st.write("Due total",due_sum) 
  st.write("Grand total",total_due_sum)  
  st.write("Percentage",str(round((total_due_sum*100/due_sum),2) )+ " % ")
  s[1],s[2],s[3],s[0]=0,0,0,0

def state(state1,state2,state3,state4,n2,n3,n4,n5): 
  cc=[0,0,0,0,0,0,0,0,0,0,0]
  gc=[0,0,0,0,0,0,0,0,0,0,0]
  y=[0,0,0,0,0,0,0,0,0,0,0]
  n=[0,0,0,0,0,0,0,0,0,0,0]
  final_df1 = pd.DataFrame(columns = ['State', 'DUE','Collections','Percentage','Contactability','Non Contactability','Contactability%'])
  checknone(state1,state2,state3,state4)
  for i in range(0,len(df1)):
    c2=df1.loc[i][n2]
    c3=df1.loc[i][n3]
    c4=df1.loc[i][n4]
    a=df1.loc[i][72]  
    b=df1.loc[i][73]
    d=df1.loc[i][71]
    e=df1.loc[i][62]
    f=df1.loc[i][63]
    if ((c2==state2 or s[1]==1) and (state3==c3 or s[2]==1) and (((c4.find('cl',0)>=0 and n5==1) or (c4.find('cl',0)<0 and n5==0)) or s[3]==1)):
      for j in range(0,11) :
        if (a==statelist[j]):
          cc[j]=cc[j]+int(b)
          gc[j]=gc[j]+int(d)
          if (e=="Y" and (not(f=="-"))) :
            y[j]=y[j]+1
          elif (e=="N" and (not(f=="-"))) :
            n[j]=n[j]+1
          break      
  for i in range(0,11) :
    temp1=cc[i]
    temp2=y[i]+n[i]
    if (cc[i]==0) :
      temp1=int(1000000000000) 
    if (temp2==0) :
      temp2=int(100000000000000000)
    final_df1.loc[len(final_df1.index)] = [statelist[i], cc[i],gc[i],str(round((gc[i]*100/temp1),2) )+" % ",y[i],n[i],str(round((y[i]*100/temp2),2))+" % "]
  st.write(final_df1)
  ccsum,gcsum=0,0
  for i in range (0,11):
    ccsum =ccsum+cc[i];
    gcsum=gcsum+gc[i]; 
  st.write("Due total",ccsum) 
  st.write("Grand total",gcsum)  
  st.write("Percentage",str(round((gcsum*100/ccsum),2) )+ " % ")
  s[1],s[2],s[3],s[0]=0,0,0,0  

def yn(state1,state2,state3,state4,n2,n3,n4,n5): 
  y=[0,0,0,0,0,0,0,0,0,0,0]
  n=[0,0,0,0,0,0,0,0,0,0,0]
  yn_df = pd.DataFrame(columns = ['State', 'Contactable','Non-Contactable','Total','Contactable%'])
  checknone(state1,state2,state3,state4)
  for i in range(0,len(df1)):
    c2=df1.loc[i][n2]
    c3=df1.loc[i][n3]
    c4=df1.loc[i][n4]
    a=df1.loc[i][72]  
    b=df1.loc[i][62]
    d=df1.loc[i][63]
    if ((c2==state2 or s[1]==1) and (state3==c3 or s[2]==1) and (((c4.find('cl',0)>=0 and n5==1) or (c4.find('cl',0)<0 and n5==0)) or s[3]==1)):
      for j in range(0,11) :
        if (a==statelist[j]):
          if (b=="Y" and (not(d=="-"))) :
            y[j]=y[j]+1
          elif (b=="N" and (not(d=="-"))) :
            n[j]=n[j]+1
  for i in range(0,11) :
    temp=y[i]+n[i]
    if (temp==0) :
      temp=int(1000000000000) 
    yn_df.loc[len(yn_df.index)] = [statelist[i], y[i],n[i],temp,str(round((y[i]*100/temp),2) )+" % "]
  st.write(yn_df)
  ysum,nsum=0,0
  for i in range (0,11):
    ysum =ysum+y[i]
    nsum=nsum+n[i]
  st.write("Total Contactable accounts",ysum) 
  st.write("Total Non-Contactable accounts",nsum)  
  total=ysum+nsum
  st.write("Percentage",str(round((ysum*100/total),2) )+" % ")
  s[1],s[2],s[3],s[0]=0,0,0,0  
def week(state1,state2,state3,state4,n2,n3,n4,n5): 
  cc=[0,0,0,0,0,0,0,0,0,0,0]
  gc=[0,0,0,0,0,0,0,0,0,0,0]
  y=[0,0,0,0,0,0,0,0,0,0,0]
  n=[0,0,0,0,0,0,0,0,0,0,0]
  wstate=[0,0,0,0]
  w1_df = pd.DataFrame(columns =['State', 'DUE','Collections','Percentage','Contactability','Non Contactability','Contactability%'])
  w2_df = pd.DataFrame(columns =['State', 'DUE','Collections','Percentage','Contactability','Non Contactability','Contactability%'])
  w3_df = pd.DataFrame(columns =['State', 'DUE','Collections','Percentage','Contactability','Non Contactability','Contactability%'])
  w4_df = pd.DataFrame(columns =['State', 'DUE','Collections','Percentage','Contactability','Non Contactability','Contactability%'])
  checknone(state1,state2,state3,state4)
  for i in range(0,len(df1)):
    c12 ,c13 ,c14 = df1.loc[i][n2] , df1.loc[i][n3] , df1.loc[i][n4]
    a1,b1,d1,e1,f1=df1.loc[i][72] ,df1.loc[i][73] ,df1.loc[i][71] ,df1.loc[i][62] , df1.loc[i][63] 
    if ((c12==state2 or s[1]==1) and (state3==c13 or s[2]==1) and (((c14.find('cl',0)>=0 and n5==1) or (c14.find('cl',0)<0 and n5==0)) or s[3]==1)):
      for j in range(0,11) :
        if (a1==statelist[j]):
          cc[j]=cc[j]+int(b1)
          gc[j]=gc[j]+int(d1)
          if (e1=="Y" and (not(f1=="-"))) :
            y[j]=y[j]+1
          elif (e1=="N" and (not(f1=="-"))) :
            n[j]=n[j]+1
          break      
  for i in range(0,11) :
    temp1=cc[i]
    temp2=y[i]+n[i]
    if (cc[i]==0) :
      temp1=int(1000000000000) 
    w1_df.loc[len(w1_df.index)] = [statelist[i], cc[i],gc[i],str(round((gc[i]*100/temp1),2) )+" % ",y[i],n[i],str(round((y[i]*100/temp2),2))+" % "]
  st.write("First week report")
  st.write(w1_df)
  ccsum,gcsum,ysum,nsum=0,0,0,0
  for i in range (0,11):
    ccsum =ccsum+cc[i];
    gcsum=gcsum+gc[i]; 
    ysum=ysum+y[i]
    nsum=nsum+n[i]
    temp3=ysum+nsum
  st.write(" Due Percentage",str(round((gcsum*100/ccsum),2) )+ " % ")
  st.write(" Contactability Percentage",str(round((ysum*100/temp3),2) )+ " % ")
  cc[0],cc[1],cc[2],cc[3],cc[4],cc[5],cc[6],cc[7],cc[8],cc[9],cc[10],gc[0],gc[1],gc[2],gc[3],gc[4],gc[5],gc[6],gc[7],gc[8],gc[9],gc[10]=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9],y[10],n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10]=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  for i in range(0,len(df2)):
    a2,b2,d2,e2,f2=df2.loc[i][72] ,df2.loc[i][73] ,df2.loc[i][71] ,df2.loc[i][62] , df2.loc[i][63]
    c22 ,c23 ,c24 = df2.loc[i][n2] , df2.loc[i][n3] , df2.loc[i][n4]
    if ((c22==state2 or s[1]==1) and (state3==c23 or s[2]==1) and (((c24.find('cl',0)>=0 and n5==1) or (c24.find('cl',0)<0 and n5==0)) or s[3]==1)):
      for j in range(0,11) :
        if (a2==statelist[j]):
          cc[j]=cc[j]+int(b2)
          gc[j]=gc[j]+int(d2)
          if (e2=="Y" and (not(f2=="-"))) :
            y[j]=y[j]+1
          elif (e2=="N" and (not(f2=="-"))) :
            n[j]=n[j]+1
          break      
  for i in range(0,11) :
    temp1=cc[i]
    temp2=y[i]+n[i]
    if (cc[i]==0) :
      temp1=int(1000000000000) 
    w2_df.loc[len(w2_df.index)] = [statelist[i], cc[i],gc[i],str(round((gc[i]*100/temp1),2) )+" % ",y[i],n[i],str(round((y[i]*100/temp2),2))+" % "] 
  st.write("Second week report")
  st.write(w2_df)
  ccsum,gcsum,ysum,nsum=0,0,0,0
  for i in range (0,11):
    ccsum =ccsum+cc[i];
    gcsum=gcsum+gc[i]; 
    ysum=ysum+y[i]
    nsum=nsum+n[i]
    temp3=ysum+nsum
  st.write(" Due Percentage",str(round((gcsum*100/ccsum),2) )+ " % ")
  st.write(" Contactability Percentage",str(round((ysum*100/temp3),2) )+ " % ")
  cc[0],cc[1],cc[2],cc[3],cc[4],cc[5],cc[6],cc[7],cc[8],cc[9],cc[10],gc[0],gc[1],gc[2],gc[3],gc[4],gc[5],gc[6],gc[7],gc[8],gc[9],gc[10]=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9],y[10],n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10]=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  for i in range(0,len(df3)):
    a3,b3,d3,e3,f3=df3.loc[i][72] ,df3.loc[i][73] ,df3.loc[i][71] ,df3.loc[i][62] , df3.loc[i][63]
    c32 ,c33 ,c34 = df3.loc[i][n2] , df3.loc[i][n3] , df3.loc[i][n4]
    if ((c32==state2 or s[1]==1) and (state3==c33 or s[2]==1) and (((c34.find('cl',0)>=0 and n5==1) or (c34.find('cl',0)<0 and n5==0)) or s[3]==1)):
      for j in range(0,11) :
        if (a3==statelist[j]):
          cc[j]=cc[j]+int(b3)
          gc[j]=gc[j]+int(d3)
          if (e3=="Y" and (not(f3=="-"))) :
            y[j]=y[j]+1
          elif (e3=="N" and (not(f3=="-"))) :
            n[j]=n[j]+1
          break      
  for i in range(0,11) :
    temp1=cc[i]
    temp2=y[i]+n[i]
    if (cc[i]==0) :
      temp1=int(1000000000000) 
    w3_df.loc[len(w3_df.index)] = [statelist[i], cc[i],gc[i],str(round((gc[i]*100/temp1),2) )+" % ",y[i],n[i],str(round((y[i]*100/temp2),2))+" % "]
  st.write("Third week report")
  st.write(w3_df)
  ccsum,gcsum,ysum,nsum=0,0,0,0
  for i in range (0,11):
    ccsum =ccsum+cc[i];
    gcsum=gcsum+gc[i]; 
    ysum=ysum+y[i]
    nsum=nsum+n[i]
    temp3=ysum+nsum
  st.write(" Due Percentage",str(round((gcsum*100/ccsum),2) )+ " % ")
  st.write(" Contactability Percentage",str(round((ysum*100/temp3),2) )+ " % ")
  cc[0],cc[1],cc[2],cc[3],cc[4],cc[5],cc[6],cc[7],cc[8],cc[9],cc[10],gc[0],gc[1],gc[2],gc[3],gc[4],gc[5],gc[6],gc[7],gc[8],gc[9],gc[10]=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9],y[10],n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10]=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  for i in range(0,len(df4)):
    a4,b4,d4,e4,f4=df4.loc[i][72] ,df4.loc[i][73] ,df4.loc[i][71] ,df4.loc[i][62] , df4.loc[i][63]
    c42 ,c43 ,c44 = df4.loc[i][n2] , df4.loc[i][n3] , df4.loc[i][n4]
    if ((c42==state2 or s[1]==1) and (state3==c43 or s[2]==1) and (((c44.find('cl',0)>=0 and n5==1) or (c44.find('cl',0)<0 and n5==0)) or s[3]==1)):
      for j in range(0,11) :
        if (a4==statelist[j]):
          cc[j]=cc[j]+int(b4)
          gc[j]=gc[j]+int(d4)
          if (e4=="Y" and (not(f4=="-"))) :
            y[j]=y[j]+1
          elif (e4=="N" and (not(f4=="-"))) :
            n[j]=n[j]+1
          break      
  for i in range(0,11) :
    temp1=cc[i]
    temp2=y[i]+n[i]
    if (cc[i]==0) :
      temp1=int(1000000000000) 
    w4_df.loc[len(w4_df.index)] = [statelist[i], cc[i],gc[i],str(round((gc[i]*100/temp1),2) )+" % ",y[i],n[i],str(round((y[i]*100/temp2),2))+" % "]
  st.write("Fourth week report")
  st.write(w4_df)
  ccsum,gcsum,ysum,nsum=0,0,0,0
  for i in range (0,11):
    ccsum =ccsum+cc[i];
    gcsum=gcsum+gc[i]; 
    ysum=ysum+y[i]
    nsum=nsum+n[i]
    temp3=ysum+nsum
  st.write(" Due Percentage",str(round((gcsum*100/ccsum),2) )+ " % ")
  st.write(" Contactability Percentage",str(round((ysum*100/temp3),2) )+ " % ")
  s[1],s[2],s[3],s[0]=0,0,0,0  

with st.form(key='columns_in_form'):
  st.write("DPD wise collections")
  st.write(CollumnList[64] + " to " + CollumnList[70])
  cols = st.beta_columns(4)
  a=cols[0].selectbox(f'Select the state', ["None","Karnataka","Maharashtra","Tamil Nadu","Gujarat","Delhi","Uttar Pradesh","Rajasthan","Madhya Pradesh","West Bengal","Telangana","Rest Of India"], key=0)
  b=cols[1].selectbox(f'Select the period', ["None","Post-Covid","Pre-Covid"], key=1)
  c=cols[2].selectbox(f'Select the allocation', ["None","Inhouse","Agency"], key=2)
  d=cols[3].selectbox(f'Select the product',["None","IC","CL"], key=3)
  submitted1 = st.form_submit_button('Submit')
if submitted1 :
  if a=="None" and b=="None" and c=="None" and d=="None": 
    dpd(a,b,c,d,72,60,59,48,2)
  else : 
    if (d=="IC"):
      dpd(a,b,c,d,72,60,59,48,0)
    elif (d=="CL"):
       dpd(a,b,c,d,72,60,59,48,1)    
with st.form(key='columns_in_form1'):
  st.write("State wise collections")
  st.write(CollumnList[64] + " to " + CollumnList[70])
  col = st.beta_columns(4)
  a1=col[0].selectbox(f'Select the method', ["State wise"], key=0)
  b1=col[1].selectbox(f'Select the period', ["None","Post-Covid","Pre-Covid"], key=1)
  c1=col[2].selectbox(f'Select the allocation', ["None","Inhouse","Agency"], key=2)
  d1=col[3].selectbox(f'Select the product',["None","IC","CL"], key=3)
  submitted2 = st.form_submit_button('Submit')
if submitted2 :    
   if  b1=="None" and c1=="None" and d1=="None": 
       state(a1,b1,c1,d1,60,59,48,2)
   else : 
    if (d1=="IC"):
      state(a1,b1,c1,d1,60,59,48,0)
    elif (d1=="CL"):
       state(a1,b1,c1,d1,60,59,48,1)      
with st.form(key='columns_in_form2'):
  st.write("Contactability")
  st.write(CollumnList[64] + " to " + CollumnList[70])
  col1 = st.beta_columns(4)
  a2=col1[0].selectbox(f'Select the method', ["Contactibility"], key=0)
  b2=col1[1].selectbox(f'Select the period', ["None","Post-Covid","Pre-Covid"], key=1)
  c2=col1[2].selectbox(f'Select the allocation', ["None","Inhouse","Agency"], key=2)
  d2=col1[3].selectbox(f'Select the product',["None","IC","CL"], key=3)
  submitted3 = st.form_submit_button('Submit')
if submitted3 :    
   if  b2=="None" and c2=="None" and d2=="None": 
       yn(a2,b2,c2,d2,60,59,48,2)
   else : 
    if (d2=="IC"):
      yn(a2,b2,c2,d2,60,59,48,0)
    elif (d2=="CL"):
       yn(a2,b2,c2,d2,60,59,48,1)       
with st.form(key='columns_in_form3'):
  st.write("Weeky")
  col2 = st.beta_columns(4)
  a3=col2[0].selectbox(f'Select the method', ["Weekly report"], key=0)
  b3=col2[1].selectbox(f'Select the period', ["None","Post-Covid","Pre-Covid"], key=1)
  c3=col2[2].selectbox(f'Select the allocation', ["None","Inhouse","Agency"], key=2)
  d3=col2[3].selectbox(f'Select the product',["None","IC","CL"], key=3)
  submitted4 = st.form_submit_button('Submit')
if submitted4 :    
   if  b3=="None" and c3=="None" and d3=="None": 
       week(a3,b3,c3,d3,60,59,48,2)
   else : 
    if (d3=="IC"):
      week(a3,b3,c3,d3,60,59,48,0)
    elif (d3=="CL"):
       week(a3,b3,c3,d3,60,59,48,1)       

