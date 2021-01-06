FROM python:3.6
WORKDIR /app
COPY ./scrapers /app
RUN pip install requests pytz pandas lxml 
CMD python ipo_scrape.py