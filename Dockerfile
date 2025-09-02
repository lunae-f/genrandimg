FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir Pillow numpy
ENTRYPOINT ["python", "./create_image.py"]