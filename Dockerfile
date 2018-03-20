FROM alpine:3.7
RUN apk add --no-cache python3
RUN apk add --no-cache git
RUN pip3 install requests bs4

RUN git clone https://github.com/soopanova/BisonHacksTut.git /code
