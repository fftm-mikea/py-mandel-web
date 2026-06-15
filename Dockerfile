FROM python

WORKDIR /usr/src

COPY ./mandel.py .

RUN echo '<style> body {font-family: "Courier New", Courier, monospace; } </style>' > index.html

RUN python mandel.py >> index.html

CMD ["python", "-m", "http.server"]
