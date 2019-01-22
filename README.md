<h1>Steps to run querysearch.py</h1>

python querysearch.py -h
usage: querysearch.py [-h] searchtype Value

Search your keyword ex: querycheck.py andsearch general,population,Alzheimer

positional arguments:
  searchtype  Search type orsearch and andsearch only
  Value       Parameter to search

optional arguments:
  -h, --help  show this help message and exit


example :

search using  "orsearch" method

python querysearch.py orsearch Care,Quality,Commission
<br>
0 1 2 3 4 5 6

search using andsearch

python querysearch.py andsearch Care,Quality,Commission,admission
<br>
1


<h1>Part2</h1>
<h2>Raik = not available</h2>


<h2>Cache create for result 1</h2>
curl -s -X PUT -H "Content-Type: text/plain" -d "0 1 2 3 4 5 6" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“Care,Quality,Commission"

<h2>Cache create for result 2</h2>
Cache create for result 2
curl -s -X PUT -H "Content-Type: text/plain" -d “9” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“September,2004"

<h2>Cache create for result 3</h2>
Cache create for result 3
curl -s -X PUT -H "Content-Type: text/plain" -d “6 8” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“general,population,generally"

<h2>Cache create for result 4</h2>
Cache create for result 4
curl -s -X PUT -H "Content-Type: text/plain" -d “1” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“Care,Quality,Commission,admission"

<h2>Cache create for result 5</h2>
Cache create for result 5
curl -s -X PUT -H "Content-Type: text/plain" -d “6” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“general,population,Alzheimer"


$KEY = “Care,Quality,Commission”

<h2>Retrive data from cache </h2>
Retrive data from cache 
CACHE_VALUE=$(redis-cli -h "$CACHE_PROXY_IP" -p "$CACHE_PROXY_PORT" "$RIAK_TEST_BUCKET:$KEY”)


<h2>Insert value with index </h2>
Curl -X put -H "Content-Type: text/plain" -d "April 15 , 2013 Thousands of GP practices ..."  http://localhost:8098/buckets/indexname/hscicNews/keys/RESULT:5


<h2>Display key for document June 2013</h2>

Curl -I http://localhost:8098/buckets/indexname/hscicNews//keys=true