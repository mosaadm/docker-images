# Simple Client

## To run a simple client container

### 1st. Build Image
```
docker build -t t-simple-client . 
```
### 2nd. Run container
```
docker run -it --network="host" -v ${PWD}/src:/app/ t-simple-client
```