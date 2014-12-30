FROM python:2-onbuild

RUN pip2.7 install -r requirements.txt

CMD [ "python2.7", "main.py" ]

