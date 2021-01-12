FROM python:3.8
WORKDIR /app
COPY ./requirements.txt /app
COPY ./option_scripts/  /app
RUN pip install -r requirements.txt
CMD python get_earnings_date_from_yahoo.py