# Simple Sever

## To run a simple server container

### Build Image
```
docker build -t mosaadm/python-client .
```
### Run container
```
docker run -it -v ${PWD}:/usr/app mosaadm/python-client
```