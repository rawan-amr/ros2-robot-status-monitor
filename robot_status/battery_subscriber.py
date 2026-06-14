import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class BatterySubscriber(Node):
     def __init__(self):
          
          super().__init__("battery_subscriber")

          self.subscription = self.create_subscription(
               Int64,
               "battery_status",
               self.battery_callback,
               10
          )
    
     def battery_callback(self, msg):
         
         self.get_logger().info(
              f'Received battery level: {msg.data}%'
              )
         
         
def main(args=None):
     
     rclpy.init(args=args)

     node = BatterySubscriber()

     rclpy.spin(node)

     node.destroy_node()
     rclpy.shutdown()

if __name__ == '__main__':
     main()
