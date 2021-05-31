# Complete the commands.
FROM python:3.7-slim

RUN mkdir src
WORKDIR /src

RUN pip install notebook

# jupyter notebook --ip=0.0.0.0 --no-browser
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]