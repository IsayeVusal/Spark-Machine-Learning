a =  sc.parallelize([("spark", 1), ("RDD", 2), ("python", 3),("context", 4), ("create", 5), ("class", 6)])
b =  sc.parallelize([("operation", 1), ("apache", 2), ("scala", 3),("lambda", 4), ("parallel", 5), ("partition", 6)])

sorted(b.rightOuterJoin(a).collect())
sorted(a.leftOuterJoin(b).collect())

from collections import Counter

a =  sc.parallelize([("spark", 1), ("RDD", 2), ("python", 3),("context", 4), ("create", 5), ("class", 6)])
b =  sc.parallelize([("operation", 1), ("apache", 2), ("scala", 3),("lambda", 4), ("parallel", 5), ("partition", 6)])

a = a.map(lambda x: list(x))
a.map(lambda x: x[0].count('s')).reduce(lambda x,y: x+y)

words = ['spark','RDD','python','context','create','class','operation','apache','scala','lambda','parallel','partition']
sum(map(lambda x : 1 if 's' in x else 0, words))

a =  sc.parallelize([("spark", 1), ("RDD", 2), ("python", 3),("context", 4), ("create", 5), ("class", 6)])
b =  sc.parallelize([("operation", 1), ("apache", 2), ("scala", 3),("lambda", 4), ("parallel", 5), ("partition", 6)])
all = a.union(b).map(lambda x: list(x))
all.map(lambda x: x[0].count('s')).reduce(lambda x,y: x+y)

students= sc.textFile("path.txt")

sqlContext = SQLContext(sc)

