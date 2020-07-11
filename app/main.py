from flask import Flask, render_template
import app.nifukura as nifukura
import app.tweet as tweet

app = Flask(__name__)


class FaceRecord:
    def __init__(self, Age, Sex, Face_s, idx):
        self.Age = Age
        self.Sex = Sex
        self.Face_s = Face_s
        self.idx = idx


@app.route('/tweet')
def tweets_face_app():
    face_all_data = []
    n_open_tweets = 0
    face_nihukura_records = nifukura.get_face_data()

    alignment_data_man = nifukura.alignment("man", face_nihukura_records)
    alignment_data_woman = nifukura.alignment("woman", face_nihukura_records)
    tweet.tweet_from_msg("男性の顔の大きさ情報↓" + alignment_data_man)
    tweet.tweet_from_msg("女性の顔の大きさ情報↓" + alignment_data_woman)
    # if sex=="man":
    #     tweet.tweet_from_msg("男性の顔の大きさ情報↓" + alignment_data)
    # elif sex=="woman":
    #     tweet.tweet_from_msg("女性の顔の大きさ情報↓" + alignment_data)


    # print(face_nihukura_records)
    # for idx, face_nihukura_record in enumerate(face_nihukura_records):
    #     face_record = FaceRecord(Age=face_nihukura_record["Age"],Sex=face_nihukura_record["Sex"],Face_s=face_nihukura_record["Face_s"], idx=idx)
    #     face_all_data.append(face_record)
    #     break
    # print(face_all_data[0])
    return "complete"
    # return render_template('base.html', tweets=tweets, n_open_tweets=n_open_tweets)


# main関数
if __name__ == '__main__':
    tweets_face_app()