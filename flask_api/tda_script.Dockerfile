FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install requests pytz pandas
CMD python option_scripts/get_options_from_tda.py