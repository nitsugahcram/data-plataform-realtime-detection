# Complete the commands.
FROM python:3.7-slim

RUN mkdir src
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt

# jupyter notebook --ip=0.0.0.0 --no-browser
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]