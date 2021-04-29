package roaster.mapreduce2;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import phone.mapreduce.PhonetrafficDriver;

import java.io.IOException;

public class Driver {
    public static class Map extends Mapper<LongWritable, Text,Text, NullWritable> {
        @Override
        protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String[] values=value.toString().split(",");
            int sum=0;
            int num=0;
            for(int i=1;i<=15;i++){
                sum+=Integer.parseInt(values[i]);
                num=i;
            }
            double avg=sum/num;

            String result=values[0]+","+avg+","+values[16]+","+values[17]+","+values[18];
            context.write(new Text(result),NullWritable.get());
        }
    }
    public static class Reduce extends Reducer<Text, NullWritable,Text, NullWritable> {
        @Override
        protected void reduce(Text key, Iterable<NullWritable> values, Context context) throws IOException, InterruptedException {
            context.write(key,NullWritable.get());
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf=new Configuration();
        Job job = Job.getInstance(conf);
        job.setJarByClass(Driver.class);
        job.setMapperClass(Driver.Map.class);
        job.setReducerClass(Driver.Reduce.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(NullWritable.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);

        Path output= new Path("C:\\Users\\gaosiao\\Desktop\\other\\data\\a");
        FileSystem fileSystem = output.getFileSystem(conf);
        if (fileSystem.exists(output)){
            fileSystem.delete(output,true);
        }
        FileInputFormat.addInputPath(job, new Path("C:\\Users\\gaosiao\\Desktop\\other\\a\\data.csv"));
        FileOutputFormat.setOutputPath(job,output);

        boolean b = job.waitForCompletion(true);
        if (b){
            System.out.println("恭喜，清洗成功");
        }else{
            System.out.println("不好意思，清洗失败");
        }
    }
}
