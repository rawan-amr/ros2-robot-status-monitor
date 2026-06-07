import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class StatusPublisher(Node):

    def __init__(self):
        super().__init__("status_publisher")

        self.publisher_ = self.create_publisher(
            String,
            "robot_status",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )
    
    def publish_status(self):
        msg = String()
        msg.data = "Robot Status: Active"

        self.publisher_.publish(msg)

        self.get_logger().info(msg.data)

def main(args=None):

    rclpy.init(args=args)
    
    node = StatusPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()