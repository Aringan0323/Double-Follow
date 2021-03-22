#!/usr/bin/env python
import rospy
import sys
import math
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import Twist

def correct_vel_linear(diff, max_vel):
        
        return -((max_vel)/(1+2**(-10*diff + 15))) + max_vel



if __name__=='__main__':
    rospy.init_node('avoid')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    avoider1 = 'seeker1'
    avoider2 = 'seeker2'
    avoider3 = 'seeker3'
    avoided = 'hider'


    # follower = rospy.get_param('~follower')
    # followed = rospy.get_param('~followed')

    moves = [
            rospy.Publisher("/{}/cmd_vel".format(avoider1), Twist, queue_size = 10),
            rospy.Publisher("/{}/cmd_vel".format(avoider2), Twist, queue_size = 10),
            rospy.Publisher("/{}/cmd_vel".format(avoider3), Twist, queue_size = 10)
        ]

    rate = rospy.Rate(10.0)

    twist = Twist()

    while not rospy.is_shutdown():
        try:
            translations = [
                            tfBuffer.lookup_transform(avoider1, avoided, rospy.Time()),
                            tfBuffer.lookup_transform(avoider2, avoided, rospy.Time()),
                            tfBuffer.lookup_transform(avoider3, avoided, rospy.Time()),
                            ]
        except(tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        for i, trans in enumerate(translations):
            twist.angular.z = 4*math.atan2(trans.transform.translation.y, trans.transform.translation.x)
            twist.linear.x = -correct_vel_linear(math.sqrt(trans.transform.translation.x**2 + trans.transform.translation.y**2), 0.3)
            moves[i].publish(twist)
        rate.sleep()