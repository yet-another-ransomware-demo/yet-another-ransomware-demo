FROM u1ih/ubuntu-novnc:latest
USER root

# install deps for httpd
RUN apt update -y
RUN apt install libapr1-dev libaprutil1-dev -y
RUN apt install gcc -y
RUN apt install libpcre3-dev libpcre3 -y
RUN apt install make

# download and install binary for httpd
# https://archive.apache.org/dist/httpd/
RUN cd /opt && wget https://archive.apache.org/dist/httpd/httpd-2.4.49.tar.gz && tar -xvf httpd-2.4.49.tar.gz
RUN cd /opt/httpd-2.4.49 && ./configure && make && make install 

# copy vulnerable conf setup
# https://blog.qualys.com/vulnerabilities-threat-research/2021/10/27/apache-http-server-path-traversal-remote-code-execution-cve-2021-41773-cve-2021-42013
COPY ./apache-httpd/httpd.conf /usr/local/apache2/conf/httpd.conf

CMD /usr/local/apache2/bin/apachectl start && bash /start.sh
