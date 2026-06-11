import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TemperatureMonitor(Node):
     def __init__(self):
          
          super().__init__("temperature_monitor")

          self.subscription = self.create_subscription(
               String,
               "temperature_status",
               self.temperature_callback,
               10
          )
    
     def temperature_callback(self, msg):
         
         self.get_logger().info(
              f'Received: {msg.data}'
              )
         
         temperature_text = msg.data
         temperature_text = temperature_text.replace("Temperature: ", "")
         temperature_text = temperature_text.replace("C", "")

         temperature_value = int(temperature_text)

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
