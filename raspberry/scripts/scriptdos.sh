#!/bin/bash
cd
## Descarga de los binarios de buildkit
wget -qO- https://github.com/moby/buildkit/releases/download/v0.9.2/buildkit-v0.9.2.linux-arm-v7.tar.gz | tar -xz -C /usr/local/bin/ --strip-components=1
## Autenticacion para pushear a un registro de docker
mkdir ~/.docker && cd ~/.docker
touch config.json
export DOCKER_AUTH=$(echo -n "$DOCKERHUB_USERNAME:$DOCKERHUB_TOKEN" | base64)
cat > ~/.docker/config.json << EOF
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "$DOCKER_AUTH"
        }
    }
}
EOF
## Inicio del buildkit daemon, pusheo de la funcion a dockerhub
/usr/local/bin/buildkitd &
