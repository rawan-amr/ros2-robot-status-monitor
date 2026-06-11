# ROS2 Robot Status Monitor

## Project Overview

This project implements a simple robot monitoring system using ROS2 Jazzy and Python.

The system simulates two robot sensors:

- Battery Sensor
- Temperature Sensor

Each sensor publishes its data on a dedicated ROS2 topic, and a corresponding subscriber receives and displays the data.

## Motivation

The goal of this project was to gain hands-on experience with:

- ROS2 package creation
- Publishers and Subscribers
- Topic-based communication
- ROS2 build workflow
- Debugging ROS2 applications
- Git and GitHub project management
- ROS2 node modularity and separation of concerns

## System Architecture

```text
Battery Publisher ------> /battery_status ------> Battery Subscriber

Temperature Publisher --> /temperature_status --> Temperature Subscriber
```

## Topics

### /battery_status

Publishes battery level information.

Example:

```text
Battery: 100%
Battery: 99%
Battery: 98%
```

### /temperature_status

Publishes temperature information.

Example:

```text
Temperature: 25C
Temperature: 26C
Temperature: 27C
```

## Nodes

### battery_publisher

Publishes battery percentage on `/battery_status`.

### battery_subscriber

Subscribes to `/battery_status` and displays received messages.

### temperature_publisher

Publishes temperature values on `/temperature_status`.

### temperature_subscriber

Subscribes to `/temperature_status` and displays received messages.

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

Run Battery Publisher:

```bash
ros2 run robot_status battery_publisher
```

Run Battery Subscriber:

```bash
ros2 run robot_status battery_subscriber
```

Run Temperature Publisher:

```bash
ros2 run robot_status temperature_publisher
```

Run Temperature Subscriber:

```bash
ros2 run robot_status temperature_subscriber
```

## Design Improvement

The project originally used a single topic containing multiple robot status values.

It was later refactored into separate battery and temperature topics to improve modularity, scalability, and maintainability following ROS2 best practices.

## Lessons Learned

During development I encountered and resolved several issues including:

- Incorrect subscription initialization
- ROS2 package build and sourcing issues
- Topic and node configuration mistakes
- Refactoring a ROS2 system into multiple publishers and subscribers

These debugging exercises helped me better understand ROS2 package structure and node communication.