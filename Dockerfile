FROM ubuntu:latest
LABEL maintainer="Lucas Miranda <lucasmirandadourado@gmail.com>"
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-pip
RUN apt install python3-dev
RUN apt install -y python3-venv
RUN python3 -m venv venv
CMD ["source", "venv/bin/activate"]
CMD ["virtualenv" "-p" "python3" "venv"]
RUN venv/bin/pip3 install Flask
RUN venv/bin/pip3 install psycopg2-binary
RUN venv/bin/pip3 install requests
RUN venv/bin/pip3 install virtualenv
ADD . /venv
ENV flask_application=venv/run.py
ENV FLASK_APP=venv/run.py
ENV FLASK_ENV=development
RUN venv/bin/pip3 freeze
CMD [".","venv/bin/activate"]
WORKDIR /
EXPOSE 5000
CMD ["python3", "run.py"]