FROM python:3.9-slim-buster
WORKDIR /App
COPY . /App
RUN pip install --no-cache-dir -r requiremnts.txt
EXPOSE 5000
CMD ["python","app.py"]