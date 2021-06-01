import datetime
from typing import List, Optional

from fastapi import FastAPI
from joblib import load
from prometheus_client import (Counter, Histogram, make_asgi_app)
from pydantic import BaseModel

predictions_counter = Counter('predictions', 'Number of predictions')
model_info_counter = Counter('model_info',
                             'Number of executions of model information')
predictions_output_hist = Histogram('predictions_output', 'Predictions output')
predictions_scores_hist = Histogram('predictions_scores', 'Predictions scores')
predictions_latency_hist = Histogram('predictions_latency',
                                     'Latency of predictions')

app = FastAPI()
clf = load("model.joblib")
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


class PredictionRequest(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = False


class PredictionResponse(BaseModel):
    score: float


@app.post("/prediction")
def predict(req: PredictionRequest):
    t1 = datetime.datetime.now()
    predictions_counter.inc()

    prediction = clf.predict([req.feature_vector])
    response = {"is_inlier": int(prediction[0])}
    predictions_output_hist.observe(int(prediction[0]))

    if req.score is True:
        score = clf.score_samples([req.feature_vector])
        response["anomaly_score"] = score[0]
        predictions_scores_hist.observe(score[0])

    d = datetime.datetime.now() - t1
    predictions_latency_hist.observe(d.total_seconds())
    return response


@app.get("/model_information")
def model_information():
    model_info_counter.inc()
    return clf.get_params()


if __name__ == "__main__":
    print("running...")
