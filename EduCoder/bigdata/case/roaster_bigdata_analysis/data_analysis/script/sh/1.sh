if hadoop fs -test -e /hive-2.3.2/warehouse/mydb.db/quality_data
then
    echo 'quality_data 表创建成功'
else 
    echo 'quality_data 表未创建' 
fi

if hadoop fs -test -e /hive-2.3.2/warehouse/mydb.db/month_avg_quality
then 
	 echo 'month_avg_quality 表创建成功'
    
    echo "{\"step\":\"正在查询表 month_avg_quality 数据，请稍后\"}"
    /hive-2.3.2/bin/hive -S -e 'select * from mydb.month_avg_quality;' 2>&1 | grep -v SLF4J >result.txt
    if cat result.txt | grep "2018	09	404.48" > /dev/null
    then
        echo '查询部分数据为：'
   		head -15 result.txt
    else 
        echo "查询失败，请检查Hive SQL是否正确，以下是查询出来的结果"
        cat result.txt
    fi
else 
    echo 'month_avg_quality 表创建失败' 
fi