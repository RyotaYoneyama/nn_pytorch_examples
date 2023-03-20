# nn_pytorch_examples
The examples of neural networks with Pytorch.
## Docker
### Build
~~~
docker build -f docker/Dockerfile docker
~~~
### Run
~~~
docker run -it --privileged --net host --ipc host --gpus all\
        -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY \
        -p 8888:8888 \
        -v $PWD/:/workspace \
        nvcr.io/nvidia/pytorch:22.04-py3 bash
~~~

After running the docker container, you can access to the container via vscode with the extension of *remote-ssh*.