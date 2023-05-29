# To build: docker build -t dhdevspace/onboarding:0.1 .

FROM osrf/ros:foxy-desktop
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y vim tmux

## Set up bashrc
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
RUN echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
RUN echo "source ~/ros2ws/install/setup.bash" >> ~/.bashrc 
RUN ln -s /opt/ros/foxy/lib/libconsole_bridge.so /opt/ros/foxy/lib/libconsole_bridge.so.1.0 #required for cpp example node

## Set up ros2 workspace
RUN mkdir -p ~/ros2ws/src
WORKDIR /root/ros2ws/src
RUN source /opt/ros/foxy/setup.bash && ros2 pkg create myturtle --build-type ament_python --dependencies rclpy

## Build
RUN cd ~/ros2ws && colcon build --packages-select myturtle --symlink-install