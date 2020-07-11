# tweet my application data 
I'm using Flask, Heroku, the Twitter API for this. The app can be hosted for free.

[![Alt text](https://pbs.twimg.com/profile_images/1181376523929935874/VxsL2Ye__400x400.jpg)](https://play.google.com/store/apps/details?id=com.Miyagin.Face_shape)

I only use scheduler.py, main.py, nifukura.py, tweet.py 
first I get application data from nifukura. Then I do alignment the data.
After that I tweet it using tweepy. That is all


## Flask Quickstart:
### Create virtual env
```console
python3 -m venv venv
Activate (on Mac):
. venv/bin/activate
```

```console
pip install Flask
export FLASK_APP=app/main.py
flask run
```

## Heroku start
```console
heroku login -i
heroku create your_app_name
```

add config vars:
```console
heroku config:set CONSUMER_KEY=xxx
heroku config:set CONSUMER_SECRET=xxx
heroku config:set ACCESS_TOKEN=xxx
heroku config:set ACCESS_SECRET=xxx
heroku config:set INTERVAL=1200
heroku config:set DEBUG=0
```


Test locally:
```console
heroku local
```

Push to Heroku:
```console
git init
heroku git:remote -a your_app_name
git add .
git commit -m "initial commit"
git push heroku master
```
