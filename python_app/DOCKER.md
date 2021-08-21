# Docker

Image based on `python:3.8-alpine` for decreased volume.

## Best Practices for writing Dockerfile

1. Create ephemeral containers (easy to stop and restart)
2. Usage of `.dockerignore`
3. No unnecessary packages
4. Use multi-stage builds
5. Minimize the number of layers
6. Decouple applications (1 container = 1 process)
7. Sort multi-line arguments
