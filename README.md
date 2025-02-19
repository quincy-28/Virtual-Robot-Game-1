# Virtual-Robot-Game-1
Virtual Robot in a world which can manouvre obstacles to win prizes

This ROS 2 Python script defines a node (subscribe_laser_node) that enables a mobile robot to navigate using LaserScan (LiDAR) and Odometry data while publishing velocity commands to /cmd_vel. It subscribes to /scan for obstacle detection and /odom for tracking position and orientation, converting quaternion data into Euler angles. A timer triggers movement updates every 0.1 seconds, implementing basic obstacle avoidance by adjusting linear and angular velocities based on sensor readings. The script also includes a method (Moving) to log data to a file, though it currently writes placeholder text. Some syntax errors and indexing mistakes exist, requiring fixes for proper functionality.
