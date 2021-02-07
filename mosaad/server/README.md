# Simple Sever

## To run a simple server container

### Build Image
```
docker build -t mosaadm/python-server . 
```
### Run container
```
docker run -it -p 8080:8080 mosaadm/python-server
```