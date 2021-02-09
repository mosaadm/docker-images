# docker-images

## To run m-docker-compose.yml
This command will start mserver with 4 tclients and 5 mclients
```
docker-compose -f m-docker-compose.yml up --scale tclient=4 --scale mclient=5
```
## To run t-docker-compose.yml
This command will start t-server with 10 instances of t-client and 10 instances of m-client
```
docker-compose -f t-docker-compose up
```