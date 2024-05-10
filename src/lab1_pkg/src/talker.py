#!/usr/bin/env python3

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def talker():
    rospy.init_node('talker', anonymous=True)

    # Retrieve ROS parameters
    v = rospy.get_param('~v', 0.0)  # Default value is 0.0
    d = rospy.get_param('~d', 0.0)  # Default value is 0.0

    # Publisher for AckermannDriveStamped message
    drive_pub = rospy.Publisher('drive', AckermannDriveStamped, queue_size=10)

    rate = rospy.Rate(100) # Publish as fast as possible

    while not rospy.is_shutdown():
        # Create message
        drive_msg = AckermannDriveStamped()
        drive_msg.header.stamp = rospy.Time.now()
        drive_msg.drive.speed = v
        drive_msg.drive.steering_angle = d
        msg=f"{drive_msg}"
        rospy.loginfo(msg)

        # Publish message
        drive_pub.publish(drive_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

