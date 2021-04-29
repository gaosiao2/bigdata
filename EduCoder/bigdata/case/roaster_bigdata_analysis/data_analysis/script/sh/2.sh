if hadoop fs -test -e /hive-2.3.2/warehouse/mydb.db/quality_data
then
    echo 'quality_data 表创建成功'
else 
    echo 'quality_data 表未创建' 
fi

if hadoop fs -test -e /hive-2.3.2/warehouse/mydb.db/day_max_quality
then 
	echo 'day_max_quality 表创建成功'
    echo "{\"step\":\"正在查询表 day_max_quality 数据，请稍后\"}"

    read date
    strsql="select dates,time_point,max_quality from mydb.day_max_quality where dates='$date';"
    echo $strsql> query.sql
    /hive-2.3.2/bin/hive -S -f query.sql 2>&1 | grep -v SLF4J >result.txt
    if cat result.txt | grep "$name" > /dev/null
    then
        echo '查询当天最高质量为：'
   		cat result.txt
    else 
        echo "查询失败，请检查Hive SQL是否正确，以下是查询出来的结果"
        cat result.txt
    fi
else 
    echo 'day_max_quality 表创建失败' 
fi