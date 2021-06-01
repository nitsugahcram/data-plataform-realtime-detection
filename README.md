# data-plataform-realtime-detection

An “Isolation Forest” (Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou, 2008) is an unsupervised learning algorithm for identifying anomalies—data observations that follow a different pattern than normal instances. Unlike most anomaly detection algorithms, which work by learning the normal or common patterns and classifying the rest as anomalies, an isolation forest focuses on isolating the anomalies and not the normal cases. According to the authors, the drawback of the first approach is that these methods are optimized for profiling the normal instances and not the anomalies and their constraint to perform well in only low-dimensional data. On the other hand, isolation forests focus on the property that anomalies are usually the minority class among a dataset and that their features differ from the normal ones. As a result, and quoting the paper, “anomalies are ‘few and different,’ which make them more susceptible to isolation than normal points.”


### Build a Docker Image
```sh
docker build -t nitsuga/lp-jupyter -f jupyter/Dockerfile 
# docker build -t nitsuga/lp-jupyter
```
### Run the Docker Image built

```sh
docker run -d -p 8888:8888 --mount type=bind,source="$(pwd)"/datasets,target=/src nitsuga/lp-jupyter 
docker run -d -p 8888:8888 nitsuga/lp-jupyter
```


```sh
pipenv lock -r > requirements.txt
``1