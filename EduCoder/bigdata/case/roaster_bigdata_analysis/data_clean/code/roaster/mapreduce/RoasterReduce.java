package roaster.mapreduce;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class RoasterReduce extends Reducer<Text,Text,Text,NullWritable> {
    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        int num=0;
        for (Text val:values){
            if (num==0){
                num++;
                context.write(new Text(val), NullWritable.get());
            }

        }
    }
}
