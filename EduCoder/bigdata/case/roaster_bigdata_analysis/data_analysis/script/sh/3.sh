if hadoop fs -test -e /hive-2.3.2/warehouse/mydb.db/roaster_data
then
    echo 'roaster_data 表创建成功'
else 
    echo 'roaster_data 表未创建' 
fi

if hadoop fs -test -e /hive-2.3.2/warehouse/mydb.db/avg_roaster
then 
	 echo 'avg_roaster 表创建成功'
    
    echo "{\"step\":\"正在查询表 avg_roaster 数据，请稍后\"}"
    /hive-2.3.2/bin/hive -S -e 'select * from mydb.avg_roaster' 2>&1 | grep -v SLF4J >result.txt
    if cat result.txt | grep "2018	340.47	174.71	7.49" > /dev/null
    then
        echo '查询部分数据为：'
   		head -3 result.txt
    else 
        echo "查询失败，请检查Hive SQL是否正确，以下是查询出来的结果"
        cat result.txt
    fi
else 
    echo 'avg_roaster 表创建失败' 
fi