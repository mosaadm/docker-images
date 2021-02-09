# docker-images

## To run m-docker-compose.yml
This command will start mserver with 4 tclients and 5 mclients
```
docker-compose -f m-docker-compose.yml up --scale tclient=4 --scale mclient=5
```
## To run t-t-docker-compose.yml
This command will start t-server with 10 instances of t-client
```
docker-compose -f t-t-docker-compose up
```

## To run t-m-docker-compose.yml
This command will start t-server with 10 instances of m-client
```
docker-compose -f t-m-docker-compose.yml up
```