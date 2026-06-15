# ROS2 Robot Status Monitor

## Project Overview

This project implements a simple robot monitoring system using ROS2 Jazzy and Python.

The system simulates two robot sensors:

- Battery Sensor
- Temperature Sensor

Each sensor publishes its data on a dedicated ROS2 topic. Subscribers display the incoming data, while monitoring nodes analyze sensor values and generate warnings when thresholds are exceeded.

## Motivation

The goal of this project was to gain hands-on experience with:

- ROS2 package creation
- Publishers and Subscribers
- Topic-based communication
- ROS2 build workflow
- Debugging ROS2 applications
- Git and GitHub project management
- ROS2 node modularity and separation of concerns
- Monitoring and event-based warning generation
- Multiple subscriptions within a single ROS2 node

## System Architecture

```text
Battery Publisher ------> /battery_status ------> Battery Subscriber
                           |
                           +-------------> Battery Monitor
                           |
                           +-------------> Robot Monitor

Temperature Publisher --> /temperature_status --> Temperature Subscriber
                           |
                           +-------------> Temperature Monitor
                           |
                           +-------------> Robot Monitor
```

## Topics

### /battery_status

Message Type:

```text
std_msgs/msg/Int64
```

Publishes battery level values.

Example output from nodes:

```text
Battery: 100%
Battery: 99%
Battery: 98%
```

### /temperature_status

Message Type:

```text
std_msgs/msg/Int64
```

Publishes temperature values.

Example output from nodes:

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

### battery_monitor

Subscribes to `/battery_status` and generates a warning when battery level drops below 20%.

### temperature_monitor

Subscribes to `/temperature_status` and generates a warning when temperature reaches 35C or higher.

### robot_monitor

Subscribes to both `/battery_status` and `/temperature_status` and monitors the overall robot condition.

## Message Refactoring

The project initially used `std_msgs/msg/String` messages for battery and temperature communication.

As the project evolved, the battery and temperature topics were refactored to use:

```text
std_msgs/msg/Int64
```

This change provides:

- Stronger type safety
- Easier numeric comparisons
- Cleaner monitoring logic
- Better ROS2 design practices

## Technologies Used

- ROS2 Jazzy
- Python
- Ubuntu 24.04
- Git
- GitHub

## How to Run

Build the package:

```bash
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

Run Battery Monitor:

```bash
ros2 run robot_status battery_monitor
```

Run Temperature Monitor:

```bash
ros2 run robot_status temperature_monitor
```

Run Robot Monitor:

```bash
ros2 run robot_status robot_monitor
```

## Design Improvements

The project evolved through multiple refactoring stages:

- Splitting robot data into separate battery and temperature topics
- Adding dedicated monitoring nodes
- Introducing a combined robot monitor node
- Migrating battery and temperature communication from String messages to Int64 messages

These improvements increased modularity, maintainability, and adherence to ROS2 best practices.

## Lessons Learned

During development I encountered and resolved several issues including:

- Incorrect subscription initialization
- ROS2 package build and sourcing issues
- Topic and node configuration mistakes
- Refactoring a ROS2 system into multiple publishers and subscribers
- Creating monitoring nodes using ROS2 callbacks

These debugging exercises helped me better understand ROS2 package structure and node communication.
