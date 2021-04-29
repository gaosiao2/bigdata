package roaster.mapreduce;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class RoasterJob {
    public static void main(String[] args) throws Exception {
        Configuration conf=new Configuration();
        Job job = Job.getInstance(conf);
        job.setJarByClass(RoasterJob.class);
        job.setMapperClass(RoasterMap.class);
        job.setReducerClass(RoasterReduce.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);

        Path path=new Path("C:\\Users\\gaosiao\\Desktop\\other\\a\\result");
        FileSystem fileSystem = path.getFileSystem(conf);
        if (fileSystem.exists(path)){
            fileSystem.delete(path,true);
        }

        FileInputFormat.addInputPath(job, new Path("C:\\Users\\gaosiao\\Desktop\\other\\a\\data_X.csv"));
        FileOutputFormat.setOutputPath(job,path);

        boolean b = job.waitForCompletion(true);
        if (b){
            System.out.println("111111111111");
        }else {
            System.out.println("2222222222222");
        }

    }
}
