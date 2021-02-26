import pyarrow.fs

hdfs = pyarrow.fs.HadoopFileSystem(host="localhost", port=50070, user="root")
hdfs.create_dir("/data/test")
hdfs.copy_file("test-file.txt", "/data/test")
print(hdfs.ls("/data/test"))
