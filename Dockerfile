FROM python:3.12.3-bookworm

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD  ["src/main.py"]
