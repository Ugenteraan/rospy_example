#!/home/topiary/nasa/bin python3.5

import rospy
from std_msgs.msg import String 


def pub():

	pub = rospy.Publisher('testchannel', String, queue_size=100)
	rospy.init_node('nodename_1', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		test_str = "Testing communcation %s" %rospy.get_time()
		rospy.logininfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()


if __name__ == '__main__':

	try:
		pub()

	except rospy.ROSInterruptException:
		pass