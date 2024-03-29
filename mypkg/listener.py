# SPDX-FileCopyrightText: 2023 kotaYoshiba
# SPDX-License-Identifier: BSD-3-clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("Listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
