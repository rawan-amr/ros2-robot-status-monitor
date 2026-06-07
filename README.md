# ROS2 Robot Status Monitor

## Project Overview

This project implements a simple robot monitoring system using ROS2 Jazzy and Python.

The system consists of two ROS2 nodes:

- Status Publisher Node
- Status Subscriber Node

The publisher periodically broadcasts the robot state through the `/robot_status` topic, while the subscriber listens to incoming messages and displays them in real time.

## Motivation

The goal of this project was to gain hands-on experience with:

- ROS2 package creation
- Publishers and Subscribers
- Topic-based communication
- ROS2 build workflow
- Debugging ROS2 applications
- Git and GitHub project management

## System Architecture

```text
Status Publisher ---> /robot_status ---> Status Subscriber
```

## Technologies Used

- ROS2 Jazzy
- Python
- Ubuntu 24.04
- Git
- GitHub

## How to Run

Build the package:

```bash
cd ~/ros2_portfolio_ws
colcon build
source install/setup.bash
```

Run the publisher:

```bash
ros2 run robot_status status_publisher
```

Run the subscriber:

```bash
ros2 run robot_status status_subscriber
```

## Lessons Learned

During development I encountered and resolved several issues including:

- Incorrect subscription initialization
- ROS2 package build and sourcing issues

These debugging exercises helped me better understand ROS2 package structure and node communication.