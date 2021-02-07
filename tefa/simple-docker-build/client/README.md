# Simple Client

## To run a simple client container

### Build Image
```
docker build -t simple-client . 
```
### Run container
```
docker run --network="host" simple-client
```