#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:09:40 2020

@author: pranavmanjunath
"""




def tt(ti,typea):
    
    lst_1_mnc=['Adobe', 'Akamai', 'Amazon', 'Ca technologies', 'GE', 'Oracle', 'MediaTek', 'SAP Labs', 'Shell', 'Sling Media', 'Societe Generale', 
               'VM ware', 'Cisco', 'Google', 'McAfee', 'Harman international', 'Samsung', 'Morgan Stanley', 'Microsoft','Target','Goldman Sachs']
    
    lst_1_pvt=['Capillary Technologies', 'Ola', 'Sprinklr', 'Atimi software', 'Infibeam', 'Accolite', 'Amadeus','Edgeverve', 
               'Microchip', 'Myntra-Designs', 'Unacademy', 'Wissen-Technologies', 'Flipkart',
               'Affirmed Networks','Air Asia','Pharmeasy','PhonePe','Paytm','ACI','Catamaran Ventures','Ccl core']
    #3 more
    
    
    lst_2_mnc=[ 'Danske IT', 'Deloitte', 'Mercedese Benz', 'Mahindra Comviva', 'PWC', 'Robert Bosch', 'Sapient', 
               'L_T Infotech', 'Sony','Cognizant', 'Ericsson', 'Dell', 'Siemens', 'Nvidia',
               'HCL Technologies Ltd', 'Wipro', 'LG software', 'IBM', 'Nokia',  'Software AG', 'Toyota-Kirloskar-Motor-Pvt-Ltd']

    
    
    lst_2_pvt=['AIG Analytics','BRIDGEi2i','Aryaka Networks', 'Betsol', 'CSG Solutions India Pvt Ltd', 
               'Inksedge','Manipal Global Education Services Private limited','Urban Ladder','Fastenal',
               'Microchip', 'Tally Solutions', 'Moon Raft', 'Musigma', 'Alstom', 'Perfios', 'Polycom',
               'Reverie Language Technologies Pvt Ltd', 
               'Capco','Vantage Agora Operations','Cloud lending Solutions','Code Nation']
    
    lst_3_mnc=['Accenture', 'Atos','Infosys','Capgemini', 'Cognizant', 'Ericsson', 'L_T Infotech', 'Volvo', 
               'WNS-Global-Services','HCL Technologies Ltd', 'Wipro', 'IBM', 'Tata Elxsi', 'Sonata Software', 
               'Century_Link', 'Infosys',  'iGate', 'Ntt data','Commscope','Grindwell_Norton','Salt Side']
    
    lst_3_pvt=['Musigma', 'OTIS Elevator company (I) Ltd', 'Quest Global', 'iCreate', 'Neev Technologies', 'Key Note (Aayuja)', 
               'Signal-Chip','Talend','Tata','TE Connectivity', 'Textron India Private Limited','Groupm',
               'Rare Mile', 'Rolon Seals', 'Indegene lifesystems Pvt. Ltd.', 'Senzopt', 'Tivo','Orient Cement','Onmobile','INS Zoom','Just Dial']

    
    if ti==1 and typea=='MNC':
        return lst_1_mnc
    
    elif ti==1 and typea=='Private':
        return lst_1_pvt
        
    elif ti==2 and typea=='MNC':
        return lst_2_mnc
        
    elif ti==2 and typea=='Private':
        return lst_2_pvt
        
    elif ti==3 and typea=='MNC':
        return lst_3_mnc
    
    else:
        return lst_3_pvt

lst=tt(3,'Private')


for i in range(len(lst)):
    lst[i]=lst[i].capitalize()
    
print(lst)
