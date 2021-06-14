# Making Predictions

## Predict Sample
### Request prediction with anomaly score
```bash
curl -X 'POST' \
  'http://localhost:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [
    -0.15795269682074692,-0.10674898283572026
  ],
  "score": false
}'
```
### Request prediction w/o anomaly score

```bash
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
```

### Retrieve Model Info -  Metadata
```bash
curl -X 'GET' \ 'http://0.0.0.0:8000/model_information' \ -H 'accept: application/json'
```
