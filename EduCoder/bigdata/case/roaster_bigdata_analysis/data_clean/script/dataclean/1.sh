#判断Hadoop 是否启动
cd dataclean
echo "{\"step\":\"删除输出文件\"}"
#删除输出文件
rm -rf /root/files >/dev/null 2>&1

rm -rf target >/dev/null 2>&1
rm -f log.txt  >/dev/null 2>&1
echo "{\"step\":\"编译文件\"}"
#编译
mkdir target  
javac -encoding UTF-8 -Djava.ext.dirs=/app/hbase-2.1.1/lib/:./lib -sourcepath com/ -d target/  roaster/mapreduce/*.java > logs.txt 2>&1 
if [ $? -ne 0 ]; then
    cat log.txt
fi
echo "{\"step\":\"执行编译的代码\"}"
# 执行编译的代码
cd target
java -Dfile.encoding=utf-8  -Djava.ext.dirs=/app/hbase-2.1.1/lib/client-facing-thirdparty/:/app/hbase-2.1.1/lib/:../lib:$JAVA_HOME/jre/lib/ext roaster.mapreduce.RoasterJob > $evaTmpLog
if [ $? -ne 0 ]; then
    cat $evaTmpLog
else    
	echo "{\"step\":\"检测数据清洗功能是否成功实现\"}"
	head -n 20 /root/files/part-r-00000 > a.txt 2>&1 
    if [ $? -ne 0 ]; then
        echo "请将您的结果保存到指定目录下"
    	cat a.txt
        cat $evaTmpLog
        break
    else
   		python3 /data/workspace/myshixun/dataclean/roaster.py
   	fi
fi


