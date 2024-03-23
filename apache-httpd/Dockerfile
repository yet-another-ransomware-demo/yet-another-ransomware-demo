FROM u1ih/ubuntu-novnc:latest
USER root

# install depencies for building apache httpd
RUN apt update -y
RUN apt install sudo -y
RUN apt install libapr1-dev libaprutil1-dev -y
RUN apt install gcc libc6 -y
RUN apt install libpcre3-dev libpcre3 -y
RUN apt install zlib1g-dev -y
RUN apt install make -y

# download and install binary for apache httpd
# https://archive.apache.org/dist/httpd/
RUN cd /opt && wget https://archive.apache.org/dist/httpd/httpd-2.4.49.tar.gz && tar -xvf httpd-2.4.49.tar.gz
RUN mkdir -p /home/apache/server
RUN cd /opt/httpd-2.4.49 && ./configure --prefix=/home/apache/server && make && make install 

# copy vulnerable conf setup
# https://blog.qualys.com/vulnerabilities-threat-research/2021/10/27/apache-http-server-path-traversal-remote-code-execution-cve-2021-41773-cve-2021-42013
COPY ./conf/httpd.conf /home/apache/server/conf/httpd.conf

# setup autocutsel for clipboard support
COPY ./vnc/xstartup /home/apache/.vnc/xstartup

# setup novnc clipboard tools
RUN apt install xdotool xclip autocutsel -y

# create apache user and home dir and set password to apache
RUN useradd -ms /bin/bash apache
WORKDIR /home/apache
RUN chown apache:apache /.novnc
RUN chown -R apache:apache /home/apache
RUN echo "apache:apache" | chpasswd
RUN echo "apache ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers

# switch to apache user before starting apache server
USER apache
CMD /home/apache/server/bin/apachectl start && /start.sh
