package roaster.mapreduce;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class RoasterMap extends Mapper<LongWritable, Text,Text,Text> {
    /********** Begin **********/
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        


    }
    /********** End **********/
}
