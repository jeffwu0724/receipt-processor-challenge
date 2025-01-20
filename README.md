# Receipt Processor Challenge - Jeff Wu
# Language + Env
using python 3.11 and fast api, also enable it to be dockerized

# How to run
we will need to run the below command in the root folder to create a docker image
```
docker build -t receipt-processor-challenge .
docker run -d -p 8000:8000 receipt-processor-challenge
docker ps -a
```
at this moment, we will need to record what is the docker name, and replaced ${docker_name} with the real name 
```
docker exec -it ${docker_name} pytest ReceiptProcessorTest.py
docker exec -it nostalgic_poitras  pytest ReceiptProcessorTest.py
```
This will trigger the test to see if the code is running as expected

In addition, we can also checkout `http://localhost:8000/docs` in the browser, this will allow us to test out the api endpoint as using Postman.