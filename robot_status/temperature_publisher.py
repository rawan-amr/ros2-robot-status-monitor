import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TemperaturePublisher(Node):

    def __init__(self):
        super().__init__("temperature_publisher")

        self.publisher_ = self.create_publisher(
            String,
            "temperature_status",
            10
        )

        self.temperature = 25
        self.temperature_increasing = True

        self.timer = self.create_timer(
            1.0,
            self.publish_temperature
        )
    
    def publish_temperature(self):
        msg = String()
        msg.data = f"Temperature: {self.temperature}C"

        self.publisher_.publish(msg)


        if self.temperature_increasing:
            self.temperature += 1
        else:
            self.temperature -= 1
        
        if self.temperature >= 40:
            self.temperature_increasing = False
        elif self.temperature <= 25:
            self.temperature_increasing = True

        self.get_logger().info(msg.data)

def main(args=None):

    rclpy.init(args=args)
    
    node = TemperaturePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()