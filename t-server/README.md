# Simple Sever

## To run a simple server container

### 1st. Build Image
```
docker build -t simple-server . 
```
### 2nd. Run container
```
docker run -it -p 9000:8080 -v ${PWD}/src/:/app/ simple-server
```