<h1>Raik = not available</h1>


<h1>Cache create for result 1</h1>
curl -s -X PUT -H "Content-Type: text/plain" -d "0 1 2 3 4 5 6" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“Care,Quality,Commission"

<h1>Cache create for result 2</h1>
Cache create for result 2
curl -s -X PUT -H "Content-Type: text/plain" -d “9” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“September,2004"

<h1>Cache create for result 3</h1>
Cache create for result 3
curl -s -X PUT -H "Content-Type: text/plain" -d “6 8” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“general,population,generally"

<h1>Cache create for result 4</h1>
Cache create for result 4
curl -s -X PUT -H "Content-Type: text/plain" -d “1” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“Care,Quality,Commission,admission"

<h1>Cache create for result 5</h1>
Cache create for result 5
curl -s -X PUT -H "Content-Type: text/plain" -d “6” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“general,population,Alzheimer"


$KEY = “Care,Quality,Commission”

<h1>Retrive data from cache </h1>
Retrive data from cache 
CACHE_VALUE=$(redis-cli -h "$CACHE_PROXY_IP" -p "$CACHE_PROXY_PORT" "$RIAK_TEST_BUCKET:$KEY”)


<h1>Insert value with index </h1>
Curl -X put -H "Content-Type: text/plain" -d "April 15 , 2013 Thousands of GP practices ..."  http://localhost:8098/buckets/indexname/hscicNews/keys/RESULT:5


<h1>Display key for document June 2013</h1>

Curl -I http://localhost:8098/buckets/indexname/hscicNews//keys=true
