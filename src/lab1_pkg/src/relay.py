#!/usr/bin/env python3

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def drive_callback(msg):
    # Extract speed and steering angle
    speed = msg.drive.speed
    steering_angle = msg.drive.steering_angle

    # Multiply both by 3
    speed *= 3
    steering_angle *= 3

    # Publish modified values
    modified_msg = AckermannDriveStamped()
    modified_msg.header.stamp = rospy.Time.now()
    modified_msg.drive.speed = speed
    modified_msg.drive.steering_angle = steering_angle

    relay_pub.publish(modified_msg)

if __name__ == "__main__":
	try:
	    rospy.init_node("relay")
	    rospy.Subscriber("drive", AckermannDriveStamped, drive_callback)
	    relay_pub = rospy.Publisher("drive_relay", AckermannDriveStamped, queue_size=1000)
	    rospy.spin()
	except rospy.ROSInterruptException:
        	pass

