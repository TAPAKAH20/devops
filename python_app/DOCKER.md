# Docker

Image based on `python:3.9-alpine` for decreased volume.

## Best Practices for writing Dockerfile

1. Avoid unnecessary privileges.
    1. Avoid running containers as root.
    2. Don’t bind to a specific UID.
    3. Make executables owned by root and not writable.
2. Reduce attack surface.
    1. Leverage multistage builds.
    2. Use distroless images, or build your own from scratch.
    3. Update your images frequently.
    4. Watch out for exposed ports.
3. Prevent confidential data leaks.
    1. Never put secrets or credentials in Dockerfile instructions.
    2. Prefer COPY over ADD.
    3. Be aware of the Docker context, and use .dockerignore.
4. Others.
    1. Reduce the number of layers, and order them intelligently.
    2. Add metadata and labels.
    3. Leverage linters to automatize checks.
    4. Scan your images locally during development.
5. Beyond image building.
    1. Protect the docker socket and TCP connections.
    2. Sign your images, and verify them on runtime.
    3. Avoid tag mutability.
    4. Don’t run your environment as root.
    5. Include a health check.
    6. Restrict your application capabilities.
6. Use .dockerignore
7. Use build cache
