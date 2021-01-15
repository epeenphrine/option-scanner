FROM python:3.6
WORKDIR /app
COPY ./scrapers /app
COPY ./option_scripts /app
RUN pip install requests pytz pandas lxml 
CMD python ipo_scrape.py & python get_data_from_nasdaq.py