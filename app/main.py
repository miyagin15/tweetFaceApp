from flask import Flask, render_template
import nifukura

app = Flask(__name__)

class FaceRecord:
    def __init___(self, Age, Sex, Face_s, idx):
        self.Age = Age
        self.Sex = Sex
        self.Face_s = Face_s
        self.idx = idx
        
@app.route('/')
def tweets_face_app():
    face_all_data = []
    n_open_tweets = 0
    face_nihukura_records = nifukura.get_face_data()
    print(face_nihukura_records)
    for idx, face_nihukura_record in enumerate(face_nihukura_records):
        print(face_nihukura_record)
        face_record = FaceRecord(**face_nihukura_record,idx=idx)
        face_all_data.append(face_record)
        break
    print(face_all_data)

    return render_template('base.html', tweets=tweets, n_open_tweets=n_open_tweets)

