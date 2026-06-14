import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class TemperatureMonitor(Node):
     def __init__(self):
          
          super().__init__("temperature_monitor")

          self.subscription = self.create_subscription(
               Int64,
               "temperature_status",
               self.temperature_callback,
               10
          )
    
     def temperature_callback(self, msg):
         
         self.get_logger().info(
              f'Received temperature: {msg.data}C'
              )

         temperature_value = msg.data

         if temperature_value >= 35:
              self.get_logger().warning(
                   "Warning: High Temperature!"
              )
         
         
def main(args=None):
     
     rclpy.init(args=args)

     node = TemperatureMonitor()

     rclpy.spin(node)

     node.destroy_node()
     rclpy.shutdown()

if __name__ == '__main__':
     main()
