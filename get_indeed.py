import requests 
import pandas as pd 
from requests_html import HTMLSession
import re
import json

def get_jobs(url, table_index=0, timeout=60):
    'not using this anymore - might use it later though'
    session = HTMLSession()
    indeed = session.get(url)
    indeed.html.render(timeout=timeout)
    indeed = indeed.html.html
    indeed = re.findall(r'jobmap\[[0-99]\]= .*;',indeed)
    indeed = [re.sub(r'jobmap\[[0-99]\]= ','',job).replace(';','') for job in indeed]
    indeed = [json.loads(job.replace('{','{"').replace(':','":').replace('\',','", "').replace('\'','"')) for job in indeed]
    return pd.DataFrame(indeed)

if __name__ == '__main__':
    print('Getting indeed data')
    url = "https://ca.indeed.com/jobs?q=cryptography&l=Ottawa%2C+ON"
    indeed = get_jobs(url)
    indeed.to_csv('indeed.csv', index=False)

