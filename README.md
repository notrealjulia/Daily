# Build instructions

```bash
docker build -t <name>:<tag> -f ./docker/DockerFile .
docker run -p 443:443 <name>:<tag>
docker push <name>:<tag>
```