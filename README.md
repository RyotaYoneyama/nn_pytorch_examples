# nn_pytorch_examples
The examples of neural networks with Pytorch.
## Docker
### Build
~~~
docker build -f docker/Dockerfile -t nvcr.io/nvidia/pytorch:22.04-py3-nn-example docker
~~~
### Run
~~~
docker run -it --privileged --net host --ipc host --gpus all --name torch_container \
        -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY \
        -p 8888:8888 \
        -v $PWD/:/home/ubuntu/nn_pytorch_examples \
        -e LOCAL_UID=`id -u $USER` -e LOCAL_GID=`id -g $USER` \
        nvcr.io/nvidia/pytorch:22.04-py3-nn-example bash
~~~

OR
~~~
cd docker/
docker compose up -d
~~~

After running the docker container, you can access to the container via vscode with the extension of *remote-ssh*.