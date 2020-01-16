FROM python:3.7-slim

# RUN apt update

WORKDIR /usr/src/app

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT 5000

EXPOSE 5000

# CMD [ "python", "dw_incognito_service/app.py" ]
# CMD ["gunicorn", "app:app", "--config=config.py"]
# RUN pip install --no-cache-dir waitress
# CMD ["waitress-serve", "flaskr:create_app", "--call"]
CMD ["python","dw_incognito_service/app.py"]
