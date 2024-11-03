# start-dfs.sh
cd /home/vamshi/Music/java/hadoop-setup
cp src/main/java/com/example/App.java hadoop_IO/App.java
cd hadoop_IO
rm ./output/*
hadoop fs -rm -r /output
hadoop fs -rm -r /input
hadoop fs -mkdir /input
hadoop fs -put input/* /input
hadoop com.sun.tools.javac.Main App.java
jar cf app.jar App*.class
hadoop jar app.jar App /input /output
hadoop fs -copyToLocal /output/* output
rm *
code output/*
# stop-dfs.sh
# clear