import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class RobotMonitor(Node):
     def __init__(self):
          
          super().__init__("robot_monitor")

          self.battery_subscription = self.create_subscription(
               String,
               "battery_status",
               self.battery_callback,
               10
          )

          self.temperature_subscription = self.create_subscription(
               String,
               "temperature_status",
               self.temperature_callback,
               10
          )
    
     def battery_callback(self, msg):
         self.get_logger().info(msg.data)
         
         battery_text = msg.data
         battery_text = battery_text.replace("Battery: ", "")
         battery_text = battery_text.replace("%", "")

         battery_level = int(battery_text)

         if battery_level <= 20:
              self.get_logger().warning(
                   "Warning: Low Battery!"
              )


     def temperature_callback(self, msg):
          self.get_logger().info(msg.data)

          temperature_text = msg.data
          temperature_text = temperature_text.replace("Temperature: ", "")
          temperature_text = temperature_text.replace("C", "")

          temperature_value = int(temperature_text)

          if temperature_value >= 35:
               self.get_logger().warning(
                    "Warning: High Temperature"
               )
         
         
def main(args=None):
     
     rclpy.init(args=args)

     node = RobotMonitor()

     rclpy.spin(node)

     node.destroy_node()
     rclpy.shutdown()

if __name__ == '__main__':
     main()
