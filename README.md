# Inverse Kinematics using the FABRIK Algorithm
The **FABRIK** (_Forward And Backward Reaching Inverse Kinematics_) algorithm is used in computer graphics and robotics to solve the inverse kinematics problem efficiently. Inverse kinematics is about figuring out the joint angles of a robotic arm or the position of a character's limbs given a desired end-effector position (like the hand of a robot or the foot of a character in animation).
## Initialization
You start by setting up the initial configuration of the joints in the chain (like the segments of a robotic arm or the bones of a character's limb). You also define the target position that you want the end effector to reach.

<sub>it should look something similar to this where there is the limb, a start position and an end effector</sub>
![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/Initialization.png?raw=true)

## Method 1: Backwards Reaching
We will start with the Backwards reaching phase:

![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/Backwards.png?raw=true)

Here we set the shown P3 (the current end position of the limb) and set it to the end effector
we take the direction from the new P3 to the old P2 and "Move" the whole segment (P3 to P2) to it's new location according to the new location of the shown points, we iterate that until we can't any more

<sub>we should get something like this</sub>
![](https://github.com/0Pixelated0/Inverse-Kinematics-Pygame/blob/main/Backwards2.png?raw=true)

as you see, the new P0 is not at the root of the limb, to fix this we are gonna move to the next method
