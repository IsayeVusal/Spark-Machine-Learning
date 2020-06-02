# Spark-Machine-Learning

The Apache Spark machine learning library (MLlib) allows data scientists to focus on their data problems and models instead of solving the complexities surrounding distributed data (such as infrastructure, configurations, and so on). Apache Spark is known as a fast, easy-to-use and general engine for big data processing that has built-in modules for streaming, SQL, Machine Learning (ML) and graph processing. This technology is an in-demand skill for data engineers, but also data scientists can benefit from learning Spark when doing Exploratory Data Analysis (EDA), feature extraction and, of course, ML.

Spark functionality: it represents the connection to a Spark cluster and you can use it to create RDDs and to broadcast variables on that cluster. When you’re working with Spark, everything starts and ends with this SparkSession. 

# Creating RDDs

An RDD simply represents data but it’s not one object, a collection of records, a result set or a data set. That is because it’s intended for data that resides on multiple computers: a single RDD could be spread over thousands of Java Virtual Machines (JVMs), because Spark automatically partitions the data under the hood to get this parallelism. Of course, you can adjust the parallelism to get more partitions. That’s why an RDD is actually a collection of partitions.

You can easily create a simple RDD by using the parallelize() function and by simply passing some data (an iterable, like a list, or a collection) to it.

# RDD Operations

Some of the most common transformations are map(), filter(), flatMap(), sample(), randomSplit(), coalesce() and repartition() and some of the most common actions are reduce(), collect(), first(), take(), count(), saveAsHadoopFile(). The perform rightOuterJoin and fullOuterJoin operations between RDDs After sorting them using map and reduce functions to count how many times the characters appear in each RDDs.
