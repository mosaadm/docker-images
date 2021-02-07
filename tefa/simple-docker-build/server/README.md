# Simple Sever

## To run a simple server container

### Build Image
```
docker build -t simple-server . 
```
### Run container
```
docker run -it --network="host" -p 9000:8080 simple-server
```