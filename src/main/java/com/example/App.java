package com.example;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class App {
    public class Rectangle implements Writable{
        public int l,b,t,r;
        public char type;
        public Rectangle(int l,int b,int r, int t,char type){
            this.l=l;
            this.b=b;
            this.r=r;
            this.t=t;
            this.type=type;
        }
        @Override
        public void write(DataOutput out) throws IOException {
            out.writeInt(l);
            out.writeInt(b);
            out.writeInt(t);
            out.writeInt(r);
            out.writeChar(type);
        }
        @Override
        public void readFields(DataInput in) throws IOException {
            l = in.readInt();
            b = in.readInt();
            t = in.readInt();
            r = in.readInt();
            type = in.readChar();
        }
        public boolean overlap(Rectangle rectangle){
                return !(this.l>=rectangle.r || this.r<=rectangle.l || this.t<=rectangle.b || this.b>=rectangle.t);
        }
    }
    public class Cell implements Writable{
        public int row,column,scale,l,b,t,r;
        public Cell(int row,int column,int scale){
            this.row=row;
            this.column=column;
            this.scale=scale;
            this.r=column*scale;
            this.t=row*scale;
            this.b=(row-1)*scale;
            this.l=(column-1)*scale;
        }
        @Override
        public void write(DataOutput out) throws IOException {
            out.writeInt(l);
            out.writeInt(b);
            out.writeInt(t);
            out.writeInt(r);
        }

        @Override
        public void readFields(DataInput in) throws IOException {
            row = in.readInt();
            column = in.readInt();
            scale = in.readInt();
            l = in.readInt();
            b = in.readInt();
            t = in.readInt();
            r = in.readInt();
        }
        public boolean overlap(Rectangle rectangle){
            return !(this.l>=rectangle.r || this.r<=rectangle.l || this.t<=rectangle.b || this.b>=rectangle.t);
        }
        public boolean cross_boundary(Rectangle rectangle){
            return (this.l<rectangle.l || this.r<rectangle.r || this.t<rectangle.t || this.b<rectangle.b);
        }
    }
    public static class MyMapper extends Mapper<Text, Text, Text, IntWritable> {
    //     public void map(Text key, Text value, Context context) throws IOException, InterruptedException{
    //         context.write(key, new IntWritable(1));
    //     }
    }
    public static class MyMapper2 extends Mapper<Text, Text, Text, IntWritable> {
        
    }
    public static class MyReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        
    }
    public static class MyReducer2 extends Reducer<Text, IntWritable, Text, IntWritable> {
        
    }
    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
        if (args.length != 3) {
        System.err.println("Usage: App <input path> <output path>");
        System.exit(-1);
        }
        Configuration  conf = new Configuration();
        Job job = Job.getInstance(conf, "App");
        job.setJarByClass(App.class);
        job.setMapperClass(MyMapper.class);
        // job.setCombinerClass(MyReducer.class);
        job.setReducerClass(MyReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        if(!job.waitForCompletion(true)){
            System.exit(1);
        }
        Job job2=Job.getInstance(conf, "App2");
        job2.setJarByClass(App.class);
        job2.setMapperClass(MyMapper2.class);    
        job2.setReducerClass(MyReducer2.class);
        job2.setOutputKeyClass(Text.class);
        job2.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job2, new Path(args[1]));
        FileOutputFormat.setOutputPath(job2, new Path(args[2]));
        System.exit(job2.waitForCompletion(true) ? 0 : 1);
    }
}