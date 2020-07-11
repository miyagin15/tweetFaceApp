import urllib.request, urllib.parse
import json
import os
from os.path import join, dirname
import logging
from dotenv import load_dotenv
load_dotenv(verbose=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

X_NCMB_Application_Key = environ['X-NCMB-Application-Key']
X_NCMB_Timestamp = environ['X-NCMB-Timestamp']
X_NCMB_Signature = environ['X-NCMB-Signature']

def get_face_data():
    # 色々なヘッダーをまとめて付与
    headers = {
        "X-NCMB-Application-Key" :X-NCMB-Application-Key,
        "X-NCMB-Timestamp" :X-NCMB-Timestamp,
        "X-NCMB-Signature" :X-NCMB-Signature,
        "Content-Type" :"application/json"
    }
    req = urllib.request.Request("https://mbaas.api.nifcloud.com/2013-09-01/classes/No_Login/?order=-createDate&limit=1000", headers=headers)
    with urllib.request.urlopen(req) as res:
        res = res.read().decode("utf-8")
        res = json.loads(res)
        logger.info(f'{len(res)}')
        # print(html)
        return res["results"]

# main関数
if __name__ == '__main__':
    res = get_face_data()
    #print(data)
    #print(json.dumps(datas,sort_keys=True, indent=4))
    #print(datas["results"])
    #datas
    #print(res)
    for idx, face_data in enumerate(res):
        print(idx)
        print(face_data)