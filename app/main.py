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
    face_nihukura_records = nifukura.get_face_data()

    alignment_data_man = nifukura.alignment("man", face_nihukura_records)
    alignment_data_woman = nifukura.alignment("woman", face_nihukura_records)
    tweet.tweet_from_msg("男性の顔の大きさ最新情報↓" + alignment_data_man)
    tweet.tweet_from_msg("女性の顔の大きさ最新情報↓" + alignment_data_woman)
    return "complete"


if __name__ == '__main__':
    tweets_face_app()