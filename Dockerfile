FROM python:3.10.14-slim
# use python's 3.10.14 version slim (essentials only)
WORKDIR /app
# working directory
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
build-essential \
curl \
software-properties-common \
git
# update and upgrade to latest software while building the docker file 
RUN git clone https://github.com/anapofasistoi/undecided-convertified.git . 
# clone the repo to /app
RUN pip3 install -r requirements.txt
# install dependecies for main.py
EXPOSE 80
#expose port from the container
HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health
# optional but good healthcheck to see if something is wrong with the container
ENTRYPOINT [ "streamlit", "run", "main.py", "--server.port=80", "--server.address=0.0.0.0", "--server.maxUploadSize=1024", "--client.toolbarMode='minimal'" ]
# command "streamlit run streamlit_app.py --server.port=80 --server.address=0.0.0.0 --server.maxUploadSize=1024 --client.toolbarMode='minimal'
# quic breakdown of that last command:
# this command will listen to the port 80 and accept any incoming requests from any interface of the server
# also it will give logs such as the problems that will encounter when something go bad

#usefull commands:
#   dokcer log <container_name>
    # gives the logs of the app for the time it will run

# docker start|restart|stop <container_name>
    # starts or restarts or stops the container
