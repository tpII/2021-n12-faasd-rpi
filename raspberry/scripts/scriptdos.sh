#!/bin/bash
# Deploy de funcion de prueba
cd
## Descarga de los binarios de buildkit
wget -qO- https://github.com/moby/buildkit/releases/download/v0.9.2/buildkit-v0.9.2.linux-arm-v7.tar.gz | tar -xz -C /usr/local/bin/ --strip-components=1
## Creacion de la funcion
mkdir ~/openfaas && cd ~/openfaas
faas new hello-go --lang go --prefix $DOCKERHUB_USERNAME
faas build -f hello-go.yml --shrinkwrap
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
cd ~/openfaas/
## Inicio del buildkit daemon, pusheo de la funcion a dockerhub
/usr/local/bin/buildkitd &
buildctl build \
    --frontend dockerfile.v0 \
    --local context=build/hello-go/ \
    --local dockerfile=build/hello-go/ \
    --output type=image,name=docker.io/$DOCKERHUB_USERNAME/hello-go:latest,push=true
## Deploy de la funcion
faas deploy -f hello-go.yml
