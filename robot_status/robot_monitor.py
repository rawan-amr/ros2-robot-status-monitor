import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class RobotMonitor(Node):
     def __init__(self):
          
          super().__init__("robot_monitor")

          self.battery_subscription = self.create_subscription(
               Int64,
               "battery_status",
               self.battery_callback,
               10
          )

          self.temperature_subscription = self.create_subscription(
               Int64,
               "temperature_status",
               self.temperature_callback,
               10
          )
    
     def battery_callback(self, msg):
         self.get_logger().info(
              f"Battery: {msg.data}%"
              )

         battery_level = msg.data

         if battery_level <= 20:
              self.get_logger().warning(
                   "Warning: Low Battery!"
              )


     def temperature_callback(self, msg):
          self.get_logger().info(
               f"Temperature: {msg.data}C"
               )

          temperature_value = msg.data

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
