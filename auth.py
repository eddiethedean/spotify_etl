import os
import requests
import numpy as np
import pandas as pd
import psycopg2 as ps
import datetime
import base64
import time


def authentication():
    
    ############ CLIENT ID AND CLIENT SECRET ################
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode())
    
    ############## API CALL PARAMETERS ######################
    
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_headers = {
        'Authorization': f'Basic {client_creds_b64.decode()}'
    }
    
    ############ API CALL ###################################
    
    r = requests.post(auth_url, data=auth_data, headers=auth_headers)
    request_status = r.status_code in range(200,299)
    
    ########################################################
    
    if request_status == True:
        auth_response = r.json()
        now = datetime.datetime.now()
        access_token = auth_response['access_token']
        expires_in = auth_response['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        
    return access_token, expires