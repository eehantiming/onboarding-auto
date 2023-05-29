xhost +local:docker && \
  docker run -it --rm \
  --privileged \
  --platform=amd64 \
  --net=host \
  --ipc host \
  --env="DISPLAY=$DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  -v $PWD/py_nodes:/root/ros2ws/src/myturtle/myturtle/py_nodes \
  --name onboarding \
  dhdevspace/onboarding:1.0