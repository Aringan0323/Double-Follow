# Double-Follow

## Description

* This program simulates a group of 4 robots in Gazebo where one robot is the leader, and the other robots are either the followers or the avoiders.
* When the other robots are the followers, they will follow the leader robot in a line. This is much like a line of ducks all following a mother duck.
* When the other robots are the avoiders, they will all move backwards away from the leader and try to avoid it.
* The leader robot is controlled by key presses from the user of the program.

## Usage

### Starting the simulation

* Type the following command into the terminal to have the auxillary robots follow the leader: 
  * <code>roslaunch (PACKAGE_NAME) followbots.launch reaction_to_leader:=follow</code>
* Type the following command into the terminal to have the auxillary robots avoid the leader: 
  * <code>roslaunch (PACKAGE_NAME) followbots.launch reaction_to_leader:=avoid</code>
* If the parameter <code>reaction_to_leader</code> is not specified, then the default behavior of the auxillary robots will be to follow the leader.

### Controlling the leader

* Type the following command into the terminal to launch <code>key_publisher.py</code>:
  * <code>rosrun (PACKAGE_NAME) key_publisher.py</code>
* In the terminal that <code>key_publisher.py</code> is running in, press the following keys to control the leader robot:
  * <code>"w"</code>: Moves the robot forwards with a speed of 0.3 m/s
  * <code>"s"</code>: Moves the robot backwards with a speed of 0.3 m/s
  * <code>"a"</code>: Rotates the robot left with an angular speed of pi/3 rads/s
  * <code>"d"</code>: Rotates the robot right with an angular speed of pi/3 rads/s
  * <code>"q"</code>: Tilts the robot left with an angular speed of pi/3 rads/s
  * <code>"e"</code>: Tilts the robot right with an angular speed of pi/3 rads/s
  * <code>" "</code>: Halts all motion

## Movement functions
#### <code>x</code> represents the distance between two robots in meters
#### <code>y</code> represents the linear x velocity of the robot in meters per second

### Follow

When the auxillary robots are following the leader robot, their motion is determined by the following function:
![linear_vel_equation](https://user-images.githubusercontent.com/57344340/112061632-28dc8400-8b35-11eb-86f8-ddcb97500d38.PNG)
![linear_vel_function](https://user-images.githubusercontent.com/57344340/112061642-2d08a180-8b35-11eb-8ca4-b448bcac5bb6.PNG)

### Avoid

When the auxilary robots are avoiding the leader robot, their motion is determined by the following function:
![linear_vel_equation_avoid](https://user-images.githubusercontent.com/57344340/112062341-35151100-8b36-11eb-8bf5-dd030515c66a.PNG)
![linear_vel_avoid](https://user-images.githubusercontent.com/57344340/112062349-36ded480-8b36-11eb-8cd3-87f3f0c46be5.PNG)




