FROM python:3.7.0-alpine
LABEL maintainer "Eric Gu <eric.changning.gu@gmail.com>"
ENV INSTALL_PATH /web
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY requirements.txt .
RUN pip install --upgrade pip -r requirements.txt
COPY . .

ENTRYPOINT [ "python" ]
CMD [ "manage.py" ]

#docker build . -t web
#docker run -t -i -p 8000:8000 web