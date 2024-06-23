FROM --platform=linux/amd64 python:3.10

RUN apt clean \
    && apt -y update

RUN apt -y install \
    python3-dev \
    build-essential

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["main.py"]