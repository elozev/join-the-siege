FROM python:3.11-slim

WORKDIR /app

ENV PYHTONUNBUFFERED=1
RUN apt-get update && \
    apt-get -y install tesseract-ocr && \
    apt-get -y install ffmpeg libsm6 libxext6 && \
    apt-get -y install poppler-utils

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "-m", "flask", "--app", "src.app", "run", "--host=0.0.0.0", "--port=8080"]