faas build -f $nombreFuncion.yml --shrinkwrap
sudo buildctl build \
    --frontend dockerfile.v0 \
    --local context=build/$nombreFuncion/ \
    --local dockerfile=build/$nombreFuncion/ \
    --output type=image,name=docker.io/$DOCKERHUB_USERNAME/$nombreFuncion:latest,push=true
faas deploy -f $nombreFuncion.yml
