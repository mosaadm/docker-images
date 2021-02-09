# docker-images

## To run m-docker-compose.yml
This command will start mserver with 4 tclients and 5 mclients
```
docker-compose -f m-docker-compose.yml up --scale tclient=4 --scale mclient=5
```
