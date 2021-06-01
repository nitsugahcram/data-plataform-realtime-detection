curl -X 'POST' \
  'http://localhost:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [
    0,0
  ],
  "score": false
}'

curl -X 'POST' \
  'http://localhost:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [
    1,.3
  ],
  "score": true
}'

curl --location --request GET 'localhost:8000/model_information'