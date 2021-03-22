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
