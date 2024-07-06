1 - Clone Repo (and [optional] start a virtual env)

```
git clone git@github.com:gatij/py-ml-api.git
```

2 - Install dependencies

```
pip install -r requirements.txt
```

3 - Train and save model after serializing (in `.joblib` format, you can delete `model.joblib` file first to generate it again)

```
python3 trainModel/trainAndSaveModel.py
```

4 - Start a flask server:

```
python3 api/serveModel.py
```

5 - Test by hitting predict end-point (through `CURL` here, can use `POSTMAN` too):

```
$ curl -X POST -H "Content-Type: application/json" -d '{"input": [5.1, 3.5, 1.4, 0.2]}' http://localhost:5000/predict

{
  "prediction": "setosa"
}

$ curl -X POST -H "Content-Type: application/json" -d '{"input": [6.2, 3.4, 5.4, 2.3]}' http://localhost:5000/predict

{
  "prediction": "virginica"
}

$ curl -X POST -H "Content-Type: application/json" -d '{"input": [6.4, 3.2, 4.5, 1.5]}' http://localhost:5000/predict

{
  "prediction": "versicolor"
}

```

