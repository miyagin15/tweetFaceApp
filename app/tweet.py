import tweepy
import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CK = settings.TW_CONSUMER_KEY
CS = settings.TW_CONSUMER_SECRET
AT = settings.TW_TOKEN
AS = settings.TW_TOKEN_SECRET

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)


def tweet_from_msg(msg):
    msg = msg.replace("Face_s","").replace("count","データ数:").replace("mean","平均値:").replace("min","最小値:").replace("max","最大値:").replace(".000000","人")
    # 好きな言葉をツイート
    try:
        api.update_status(msg)
    except Exception as e:
        logger.warning(f'{e} + :twitter error')

    # api.update_with_media(filename='./test.png', status="abe")


# main関数
if __name__ == '__main__':
    tweet_from_msg("a")