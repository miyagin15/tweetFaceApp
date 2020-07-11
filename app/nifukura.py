import urllib.request, urllib.parse
import json
import logging
import settings
import pandas as pd
import datetime
import dateutil.parser


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
        logger.info(f'データ数:{len(res)}')
        return res["results"]


def alignment(sex, records):
    list_df = pd.DataFrame(columns=['Age','Sex','Face_s'])
    for record in records:
        tmp_se = pd.Series([record["Age"],  record["Sex"], record["Face_s"]], index=list_df.columns)
        list_df = list_df.append(tmp_se, ignore_index=True)
    query = "Sex == '"+sex+"'"
    return list_df.query(query).describe().to_string()


def alignment_today(records):
    list_df = pd.DataFrame(columns=['Age','Sex','Face_s'])
    for record in records:
        if datetime.date.today() == dateutil.parser.parse(record["createDate"]).date():
            tmp_se = pd.Series([record["Age"],  record["Sex"], record["Face_s"]], index=list_df.columns)
            list_df = list_df.append(tmp_se, ignore_index=True)
    return list_df.describe().to_string()


if __name__ == '__main__':
    res = get_face_data()
    alignment_today(res)