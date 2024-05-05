# Inverse Kinematics using the FABRIK Algorithm
The **FABRIK** (_Forward And Backward Reaching Inverse Kinematics_) algorithm is used in computer graphics and robotics to solve the inverse kinematics problem efficiently. Inverse kinematics is about figuring out the joint angles of a robotic arm or the position of a character's limbs given a desired end-effector position (like the hand of a robot or the foot of a character in animation).
## Initialization
-   Define the initial configuration of joints in the chain (e.g., segments of a robotic arm or bones of a character's limb).
-   Specify the target position for the end effector.

<sub>it should look something similar to this where there is the limb, a start position and an end effector</sub>
![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/Initialization.png?raw=true)

## Method 1: Backwards Reaching
We will start with the Backwards reaching phase:

![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/Backwards.png?raw=true)

-   Set the current end position of the limb, denoted as P<sub>3</sub>​, to the end effector position.
-   Iterate through the chain from end to start: (in this situation P<sub>3</sub> is the current point being worked on while P<sub>2</sub> is the point before it)
    1.  Compute the direction from the new P<sub>3</sub>​ to the previous joint P<sub>2</sub>​.
    2.  Move the segment (from P<sub>3</sub>​ to P<sub>2</sub>) to align with this direction.
-   This may result in P<sub>0</sub>​ (the root joint) being offset from the limb's root, we fix that in the next method

<sub>we should get something like this</sub>
![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/Backwards2.png?raw=true)

## Method 2: Forwards Reaching
-   Reset P<sub>0</sub>​ to the limb's root position.
-   Iterate through the chain from start to end:
    1.  Compute the direction from the new P<sub>0</sub>​ to the next joint.
    2.  Move the segment (from P<sub>0</sub>​ to the next joint) to align with this direction.

![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/Forwards.png?raw=true)

Repeat these two methods until the end effector reaches a specific distance from the target position, or until both P<sub>3</sub>​ and the end effector are within a tolerance level.

## Small Optimization

-   If the end effector is out of reach, the limb will fully extend naturally.
-   Check if the total length of the limb (sum of segment lengths) is less than the distance between the limb's root and the end effector. If so, the end effector is out of reach.
## Bending Towards a Point
- Initially extend the limb fully towards the desired point.
- Iterate through the FABRIK algorithm (backwards and forwards reaching phases) for at least 10 iterations. (10 as a "maximum" is not required, just recommended for most use cases)

The limb bends towards the desired point while ensuring that P<sub>3</sub>​ (the end effector) remains at the target 

<sub> this should be how the whole thing works</sub>
![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/End.png?raw=true)
