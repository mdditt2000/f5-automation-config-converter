FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-dev python3-pip python3-jmespath && \
    apt-get install -y openssh-client iputils-ping sshpass wget

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install ansible
RUN pip3 install deepdiff
RUN pip3 install pprintpp
RUN pip3 install beautifulsoup4

RUN ansible-galaxy install f5devcentral.atc_deploy --force
RUN ansible-galaxy collection install f5networks.f5_modules