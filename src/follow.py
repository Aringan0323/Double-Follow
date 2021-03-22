#!/usr/bin/env python
import rospy
import sys
import math
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import Twist

'''
This is an asymptotic function which outputs a velocity that is 0 when the 
specified diff reaches 0, but increases the output velocity to max_vel when 
diff increases.
'''
def correct_vel_linear(diff, max_vel):
        
        return -((max_vel*5)/(2**(20*diff + 2.36))) + max_vel



if __name__=='__main__':
    rospy.init_node('follower')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)


    #Initializing the names of the bots
    follower1 = 'seeker1'
    follower2 = 'seeker2'
    follower3 = 'seeker3'
    followed = 'hider'

    #Initializing a list of  cmd_vel publishers for each follower bot
    moves = [
            rospy.Publisher("/{}/cmd_vel".format(follower1), Twist, queue_size = 10),
            rospy.Publisher("/{}/cmd_vel".format(follower2), Twist, queue_size = 10),
            rospy.Publisher("/{}/cmd_vel".format(follower3), Twist, queue_size = 10)
        ]

    rate = rospy.Rate(10.0)

    twist = Twist()

    while not rospy.is_shutdown():
        try:
            '''
            Initializing a list of transformations for each follower bot. 
            (Follower3 to follower2, follower2 to follower1, and follower1 to followed)
            '''
            translations = [
                            tfBuffer.lookup_transform(follower1, followed, rospy.Time()),
                            tfBuffer.lookup_transform(follower2, follower1, rospy.Time()),
                            tfBuffer.lookup_transform(follower3, follower2, rospy.Time())
                            ]
        except(tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        '''
        Updates the x velocity and angular z velocity for each follower bot so that they
        follow the robot which they have been previously specified to follow. This creates
        an effect where each follower bot follows the one in front of it, and the follower1
        follows the robot controlled by the user.
        '''
        for i, trans in enumerate(translations):
            twist.angular.z = 4*math.atan2(trans.transform.translation.y, trans.transform.translation.x)
            twist.linear.x = correct_vel_linear(math.sqrt(trans.transform.translation.x**2 + trans.transform.translation.y**2)-0.3, 0.3)
            moves[i].publish(twist)
        rate.sleep()