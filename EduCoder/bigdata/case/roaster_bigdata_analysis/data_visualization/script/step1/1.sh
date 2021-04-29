#/bin/bash
source /etc/profile >/dev/null 2>&1
tomcat=$(netstat -nlp | grep :8080 | awk '{print $7}' | awk -F"/" '{ print $1 }')
if [ -z "${tomcat}" ]; then
   echo 1 > test.log
else
   kill -9 $tomcat
fi
cd /data/workspace/myshixun/step1
echo "{\"step\":\"开始编译程序\"}"
mysql -uroot -p123123 -h127.0.0.1 < /data/workspace/myshixun/secret/step1/1.sql
nohup python3 roaster/manage.py >/root/flask.log 2>&1 &
sleep 2


flask=$(netstat -nlp | grep :8080 | awk '{print $7}' | awk -F"/" '{ print $1 }')
if [ -z "${flask}" ]; then
	echo "Flask启动失败，错误日志如下："
	cat /root/flask.log
else
	echo "Flask 启动成功"
	echo "{\"step\":\"模拟HTTP请求访问页面localhost:8080/time_count_top10\"}"
	python3 /data/workspace/myshixun/secret/step1/1.py > /root/tupian.txt 2>&1 
	if [ $? -ne 0 ]; then
		cat /root/tupian.txt
		cat /root/flask.log
	else
		python3 /data/workspace/myshixun/secret/step1/2.py
	fi

fi