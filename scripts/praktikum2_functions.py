#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)

#######################
# YOUR FUNCTIONS HERE #
#######################
def forward(duration, velocity):
    for i in range(0,duration):
        vel_msg.linear.x = velocity
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def turning(duration, angle):
    for i in range(0,duration):
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = angle
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def sideway(duration, velocity):
    for i in range(0,duration):
        vel_msg.linear.x = 0
        vel_msg.linear.y = velocity
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)


###########################
# YOUR FUNCTIONS HERE END #
###########################


def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        ########################
        # YOUR CODE HERE START #
        ########################
        forward(30, 0.4)

        turning(20, 0.5)

        sideway(40, 0.3)

        ######################
        # YOUR CODE HERE END #
        ######################


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
