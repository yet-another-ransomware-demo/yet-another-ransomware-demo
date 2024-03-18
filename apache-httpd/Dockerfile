FROM u1ih/ubuntu-novnc:latest
USER root

# install deps for httpd
RUN apt update -y
RUN apt install libapr1-dev libaprutil1-dev -y
RUN apt install gcc libc6 -y
RUN apt install libpcre3-dev libpcre3 -y
RUN apt install zlib1g-dev -y
RUN apt install make

# download and install binary for httpd
# https://archive.apache.org/dist/httpd/
RUN cd /opt && wget https://archive.apache.org/dist/httpd/httpd-2.4.49.tar.gz && tar -xvf httpd-2.4.49.tar.gz
RUN mkdir /opt/apache2 
RUN cd /opt/httpd-2.4.49 && ./configure --prefix=/opt/apache2 && make && make install 

# copy vulnerable conf setup
# https://blog.qualys.com/vulnerabilities-threat-research/2021/10/27/apache-http-server-path-traversal-remote-code-execution-cve-2021-41773-cve-2021-42013
COPY ./conf/httpd.conf /opt/apache2/conf/httpd.conf
RUN chown -R www-data:www-data /opt/apache2
RUN usermod -aG www-data daemon

CMD su www-data -s /bin/bash -c "/opt/apache2/bin/apachectl start" && bash /start.sh
