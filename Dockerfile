FROM python
WORKDIR /site
RUN python -m venv ./venv/
RUN /site/venv/bin/python -m pip install flask
RUN /site/venv/bin/python -m pip install pillow

COPY Components ./Components
COPY Tools ./Tools
COPY templates ./templates
COPY main.py .
COPY static/img ./static/img

EXPOSE 5000

CMD './main.py'