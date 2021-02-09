# Simple Client

## To run a simple client container

### 1st. Build Image
```
docker build -t simple-client . 
```
### 2nd. Run container
```
docker run -it -v ${PWD}/src:/app/ simple-client
```