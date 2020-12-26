Data Streaming Nanodegree

SF Crime Statistics with Spark Streaming (Step 3)

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

We could change the following parameters:
 - inputRowsPerSecond: The rate at which data is arriving from this source.
 - processedRowsPerSecond: The rate at which data from this source is being procressed by Spark.
 
A higher number on processedRowsPerSecond will increase the number of rows per seconds, so it will increase the throughput.


2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Taking into account the parameter processedRowsPerSecond I check the following properties key/values:
- spark.default.parallelism: 3 (using a machine with 2 cores CPU) 
- spark.streaming.kafka.maxRatePerPartition: 10
