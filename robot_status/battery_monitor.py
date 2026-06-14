import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class BatteryMonitor(Node):
     def __init__(self):
          
          super().__init__("battery_monitor")

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

         battery_level = msg.data         

         if battery_level <= 20:
              self.get_logger().warning(
                   "Warning: Low Battery!"
              )
         
def main(args=None):
     
     rclpy.init(args=args)

     node = BatteryMonitor()

     rclpy.spin(node)

     node.destroy_node()
     rclpy.shutdown()

if __name__ == '__main__':
     main()
