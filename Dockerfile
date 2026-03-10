FROM python:3.13 

WORKDIR /usr/local/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 8080

RUN useradd app

USER app

HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8080/ || exit 1

CMD ["uvicorn", "src.app:app","--host","0.0.0.0","--port","8080"]
