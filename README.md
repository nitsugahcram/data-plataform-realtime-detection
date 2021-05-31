# data-plataform-realtime-detection

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
```