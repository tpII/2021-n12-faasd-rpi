FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/classic-watchdog:0.2.0 as watchdog
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3-alpine

ARG TARGETPLATFORM
ARG BUILDPLATFORM

# Allows you to add additional packages via build-arg
ARG ADDITIONAL_PACKAGE

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
RUN apk --no-cache add ca-certificates ${ADDITIONAL_PACKAGE} py3-rpigpio

RUN apk add gcc musl-dev python3-dev unzip \ 
&& pip install setuptools wheel \
&& wget https://github.com/adafruit/Adafruit_Python_DHT/archive/refs/tags/1.4.1.zip \
&& unzip 1.4.1.zip \
&& cd Adafruit_Python_DHT-1.4.1/ \
&& python3 setup.py install --force-pi

# Add non root user
RUN addgroup -S app && adduser app -S -G app

WORKDIR /home/app/

COPY index.py           .
COPY requirements.txt   .

RUN chown -R app /home/app && \
  mkdir -p /home/app/python && chown -R app /home/app
USER app
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python

#RUN pip install -r requirements.txt --target=/home/app/python --force-bbb
#RUN pip3 install Adafruit_DHT

RUN mkdir -p function
RUN touch ./function/__init__.py

WORKDIR /home/app/function/
COPY function/requirements.txt	.

#RUN pip install -r requirements.txt --target=/home/app/python --force-bbb
#RUN pip3 install Adafruit_DHT

WORKDIR /home/app/

USER root

COPY function           function

# Allow any user-id for OpenShift users.
RUN chown -R app:app ./ && \
  chmod -R 777 /home/app/python

USER app

ENV fprocess="python3 index.py"
EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
