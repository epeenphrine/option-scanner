FROM python:3.6
WORKDIR /app
RUN mkdir /tmp/json
RUN mkdir /tmp/data
COPY ./option_scripts /app
RUN pip install requests pytz pandas tqdm
CMD python get_options_from_tda.py