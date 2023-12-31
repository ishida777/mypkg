import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self,node):
        rclpy.init()
        self.node = Node("talker")
        self.pub = node.node_publisher(Int16, "countup", 10)
        self.n = 0
        node.node.create_timer(0.5, self.cb)

    def cb (self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

if __name__ =='__main__':
    talker = Talker()
    rclpy.spin(talker.node)
    talker.node.destroy_node()
    rclpy.shutdown()
