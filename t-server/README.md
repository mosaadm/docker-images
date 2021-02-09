# Simple Sever

## To run a simple server container

### 1st. Build Image
```
docker build -t t-simple-server . 
```
### 2nd. Run container
```
docker run -it -p 8080:8080 -v ${PWD}/src/:/app/ t-simple-server
```