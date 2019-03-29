#!/home/topiary/nasa/bin python3.5

import rospy
from std_msgs.msg import String 

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "Received message : %s" , data.data)

def listener():

	rospy.init_node('nodename_2', anonymous=True)

	rospy.Subscriber('testchannel', String, callback)

	rospy.spin()

if __name__ == '__main__':

	listener()