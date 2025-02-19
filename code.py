import setup.py
import rclpy
import math
from rclpy.node import Node
# from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

class MyRobot(Node):
    
    def __init__(self):
        super().__init__('subscribe_laser_node')
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
        history=rclpy.qos.HistoryPolicy.KEEP_LAST, depth=1)
        ## This QOS_POLICY needs to go before the laser subscription in your code. ##
        self.sub = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback, qos_profile=qos_policy)
            ## The QOS_POLICY needs to be added to the call back. ## 
        self.sub2 = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.my_x = 0.0
        self.my_y = 0.0
        self.my_th = 0.0
        self.my_ls = LaserScan()        
        self.my_x1 = 0.0
        self.my_y1 = 0.0
        self.stage = -1


    def scan_callback(self, msg):
        self.my_ls.ranges = msg.ranges
        print ('r = {0:5.2f}, f = {1:5.2f}, l = {2:5.2f}'.format(self.my_ls.ranges[90], self.my_ls.ranges[0], self.my_ls.ranges[270]))
		 
	
    def odom_callback(self, msg):
        
        if self.stage == -1:
            self.my_x1 = msg.pose.pose.position.x
            self.my_y1 = msg.pose.pose.position.y
            self.stage = 0

        self.my_x = msg.pose.pose.position.x-self.my_x1
        self.my_y = msg.pose.pose.position.y-self.my_y1

        # convert quaternian to Euler angles
        q0 = msg.pose.pose.orientation.w
        q1 = msg.pose.pose.orientation.x
        q2 = msg.pose.pose.orientation.y
        q3 = msg.pose.pose.orientation.z
        self.my_th = math.atan2(2 * (q0 * q3 + q1 * q2), (1 - 2 * (q2 * q2 + q3 * q3))) * 180 / math.pi
         print ('x = {0:5.2f}, y = {1:5.2f}, th = {2:5.2f}'.format(self.my_x, self.my_y, self.my_th))

    def timer_callback(self):
        move = Twist()
        # your controller code should be replace the following two lines.
        move.linear.x = 0.2
        move.angular.z = 0.0
        try: 
            if self.stage == 0:
                if  self.my_ls[0] < 0.51:
                    move.linear.x = 0.0
                    move.angular.z = 0.2
                elif self.my_ls[45]:
                        move.linear.x = 0.0
                        move.angular.z = 0.2
                elif self.my_ls[315]:
                        move.linear.x = 0.
                        move.angular.z = -0.2
                        #self.stage +=1

        except  move.linear.x = 0.0
                move.angular.z = 0.0 
                print("hold")          
        
                
  


        # if self.stage == 2: 
        #     if  self.my_th < 3 or self.my_th > -3:
        #         move.linear.x = (0-self.my_th)*0.01
        #         move.angular.z = 0.2
        #     if 89 > self.my_th > 3 or -180 < self.my_th < -3 or 180 > self.my_th > 91:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #     if 91 > self.my_th > 89: 
        #         move.linear.x = 0.2
        #         move.angular.z = 0.0
        #         self.stage +=1

        # if self.stage == 3:
        #     if -1 < self.my_y < 1:
        #         move.linear.x = 0.2
        #         move.angular.z = 0.0
        #     else:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #         self.stage +=1 

        # if self.stage == 4: 
        #     if  self.my_th < 110  :
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #     if 110 < self.my_th < 168:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #     if 168 < self.my_th < 178:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.08
        #     if 178 < self.my_th < 180 or -178 > self.my_th > -180 : 
        #         move.linear.x = 0.2
        #         move.angular.z = 0.0
        #         self.stage +=1
            
        # if self.stage == 5:
        #     if 0.1 < self.my_x < 1.5:
        #         move.linear.x = 0.2
        #         move.angular.z = 0.0
        #     else:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #         self.stage +=1 

            
        # if self.stage == 6: 
        #     if 160 < self.my_th <  180:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #     if -180 < self.my_th < -95:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #     if -95 < self.my_th < -92:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.08
        #     if -92 < self.my_th < -88  : 
        #         move.linear.x = 0.2
        #         move.angular.z = 0.0
        #         self.stage +=1

        # if self.stage == 7:
        #     if 0.1 < self.my_y < 1.5:
        #         move.linear.x = 0.2
        #         move.angular.z = 0.0
        #     else:
        #         move.linear.x = 0.0
        #         move.angular.z = 0.2
        #         self.stage +=1 

        # if counter%10 ==0:
        #     self.Moving()
            
        # move.linear.x = 0.2
        # move.angular.z = 0.0

        self.pub.publish(move)

    def Moving(self):
        # open a data file in the M-Drive, you need it to change to yours
        myfile = open("/tb3_ws/src/ce215_pkg/ce215_pkg/myodom.txt", "a")

        # your data saving code should be here
        myfile.write('ashdkshdkjad')
        # close the data file
        myfile.close
        print('path completed!')

def main(args=None):
    rclpy.init(args=args)

    myrobot_node = MyRobot()
    myrobot_node.Moving()
    rclpy.spin(myrobot_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    myrobot_node.destroy_node()
    rclpy.shutdown()

    if __name__ == '__main__':
        main()
