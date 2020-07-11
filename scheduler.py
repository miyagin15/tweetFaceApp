import app.nifukura as nifukura
import app.tweet as tweet

def tweets_face_app():
    face_nihukura_records = nifukura.get_face_data()

    alignment_data_man = nifukura.alignment("man", face_nihukura_records)
    alignment_data_woman = nifukura.alignment("woman", face_nihukura_records)
    alignment_data_today = nifukura.alignment_today(face_nihukura_records)
    tweet.tweet_from_msg("男性の顔の大きさ最新情報↓" + alignment_data_man)
    tweet.tweet_from_msg("女性の顔の大きさ最新情報↓" + alignment_data_woman)
    tweet.tweet_from_msg("今日、顔の大きさを測った人↓" + alignment_data_today)
    return "complete"


if __name__ == '__main__':
    tweets_face_app()