FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn pandas scikit-learn requests numpy matplotlib
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
