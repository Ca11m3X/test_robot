#!/usr/bin/env python3

import rospy
from interbotix_xs_modules.arm import InterbotixManipulatorXS

if __name__ == "__main__":
    bot = InterbotixManipulatorXS("vx300s", "arm", "gripper")
    bot.arm.go_to_home_pose()
    bot.arm.set_ee_pose_components(x=0.2, z=0.1, pitch=1.57)
    bot.arm.set_single_joint_position("waist", 1.57)
    bot.gripper.open()
    bot.arm.set_ee_cartesian_trajectory(z=-0.08)
    bot.gripper.close()
    bot.arm.set_ee_cartesian_trajectory(z=0.08)
    bot.arm.set_single_joint_position("waist", 0)
    bot.arm.set_ee_cartesian_trajectory(z=-0.08)
    bot.gripper.open()
    bot.arm.set_ee_cartesian_trajectory(z=0.08)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()
