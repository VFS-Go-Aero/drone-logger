import rclpy
from rclpy.node import Node


class DroneLogger(Node):
    def __init__(self):
        super().__init__("drone_logger")
        self.get_logger().info("drone_logger node initialized")


def main(args=None):
    rclpy.init(args=args)
    node = DroneLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
