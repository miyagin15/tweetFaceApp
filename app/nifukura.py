import urllib.request, urllib.parse
import json
import logging
import settings
import numpy as np
import pandas as pd


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

X_NCMB_Application_Key = settings.X_NCMB_Application_Key
X_NCMB_Timestamp = settings.X_NCMB_Timestamp
X_NCMB_Signature = settings.X_NCMB_Signature


def get_face_data():
    # 色々なヘッダーをまとめて付与
    headers = {
        "X-NCMB-Application-Key": X_NCMB_Application_Key,
        "X-NCMB-Timestamp": X_NCMB_Timestamp,
        "X-NCMB-Signature": X_NCMB_Signature,
        "Content-Type": "application/json"
    }
    req = urllib.request.Request("https://mbaas.api.nifcloud.com/2013-09-01/classes/No_Login/?order=-createDate&limit=1000", headers=headers)
    with urllib.request.urlopen(req) as response:
        res = response.read().decode("utf-8")
        res = json.loads(res)
        logger.info(f'{len(res)}')
        # print(html)
        return res["results"]


def alignment(sex, records):
    list_df = pd.DataFrame(columns=['Age','Sex','Face_s'])
    for record in records:
        tmp_se = pd.Series([record["Age"],  record["Sex"], record["Face_s"]], index=list_df.columns)
        list_df = list_df.append(tmp_se, ignore_index=True)
    # print(list_df.query("Sex == 'woman'").describe())
    # print(list_df.query("Sex == 'man'").describe())
    # print(list_df.describe())
    query="Sex == '"+sex+"'"
    print(query)
    return list_df.query(query).describe().to_string()


# main関数
if __name__ == '__main__':
    res = get_face_data()
    alignment_data = alignment("man",res)
    print(alignment_data)
    #print(data)
    #print(json.dumps(datas,sort_keys=True, indent=4))
    #print(datas["results"])
    #datas
    #print(res)

    # for idx, face_data in enumerate(res):
    #     print(idx)
    #     print(face_data)