
import requests
html_text = requests.get('https://glints.com/id/opportunities/jobs/explore?keyword=engineer&country=ID&locationName=Indonesia').text

from bs4 import BeautifulSoup
soup1 = BeautifulSoup(html_text,'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
rows = soup2.find_all('div',class_ ='JobCardsc__JobcardContainer-sc-1f9hdu8-0 RBKNv CompactOpportunityCardsc__CompactJobCardWrapper-sc-1xtox99-0 hFaCrl compact_job_card')

records = []
for row in rows :
    company_loc   = row.find('div',class_='CompactOpportunityCardsc__OpportunityInfo-sc-1xtox99-13 hiAtMr').span.text.strip()
    job_title     = row.find('h3',class_ ='CompactOpportunityCardsc__JobTitle-sc-1xtox99-7 kJpKeD').text.strip()
    company_name  = row.find('a',class_ = 'CompactOpportunityCardsc__CompanyLink-sc-1xtox99-8 bFxfxR').text.strip()
    url           = "glints.com"+ row.find('a',class_ = 'CompactOpportunityCardsc__CardAnchorWrapper-sc-1xtox99-19 kfpfJK job-search-results_job-card_link')['href']
    records.append((job_title,company_name,company_loc,url))

import pandas as pd
df = pd.DataFrame(records,columns=['Job', 'Company','Location','Url'])
df.to_csv(r'Glints Data Jobs in Indonesia.csv',index=False ,encoding='UTF8')

