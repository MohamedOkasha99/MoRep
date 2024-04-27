FROM python:3

WORKDIR /app
COPY . /app

RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt

CMD ["python", "text_analysis.py"]
