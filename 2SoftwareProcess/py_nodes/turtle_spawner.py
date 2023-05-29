"""Script for spawning turtles. 
run with `ros2 run myturtle turtle_spawner.py`
"""
import rclpy
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner()
    rclpy.spin(node)
    rclpy.shutdown()


class TurtleSpawner(Node):
    """
    A ros node class for spawning turtles.

    ...

    Attributes
    ----------


    Methods
    -------

    """
    def __init__(self):
        super().__init__("turtle_spawner")
        self.get_logger().info("Started turtle_spawner node!")


if __name__ == "__main__":
    main()
