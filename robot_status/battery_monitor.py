import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class BatteryMonitor(Node):
     def __init__(self):
          
          super().__init__("battery_monitor")

          self.subscription = self.create_subscription(
               String,
               "battery_status",
               self.battery_callback,
               10
          )
    
     def battery_callback(self, msg):
         
         self.get_logger().info(
              f'Received: {msg.data}'
              )
         
         battery_text = msg.data
         battery_text = battery_text.replace("Battery: ", "")
         battery_text = battery_text.replace("%", "")

         battery_level = int(battery_text)

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
