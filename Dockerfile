FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt
EXPOSE 8001
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]
