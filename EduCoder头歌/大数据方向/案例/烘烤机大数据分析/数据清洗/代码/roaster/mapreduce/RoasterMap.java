package roaster.mapreduce;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class RoasterMap extends Mapper<LongWritable, Text,Text,Text> {
    private int num=0;
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String[] values = value.toString().split(",");
        String date=values[0];
        //去除首列
        if ("date_time".equals(date)){
            return;
        }
        //转换日期格式
        SimpleDateFormat newdate = new SimpleDateFormat("yyyy-MM-dd HH:mm");
        try {
            Date dates = newdate.parse(date);
            date=new SimpleDateFormat("yyyy-MM-dd HH:mm").format(dates);
        } catch (ParseException e) {
            e.printStackTrace();
        }

        if (values[17].split("\\.")[1].length()!=2){
            values[17] = String.format("%.2f",Double.parseDouble(values[17]));

    }

        if (values[16].split("\\.")[1].length()!=2) {
            values[16] = String.format("%.2f",Double.parseDouble(values[16]));

        }
        String result="";
        for (int i=0;i<values.length;i++){
            if (i==values.length-1){
                result=result+values[i];
            }else if (i==0) {
                result=date+"\t";
            }else {
                result=result+values[i]+"\t";
            }
        }

        context.write(new Text(date),new Text(result));


    }
}
