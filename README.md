# p3bot_description

ROS2 Robot description package for **P3Bot**, including its kinematic structure, visual and collision models, and integrated dual Kinova Gen3 arms.

This repository provides a **pure robot description** (URDF/xacro + meshes) intended to be reused by simulation, bringup, control, and planning packages.

---

## 📦 Contents

- Complete URDF/xacro description of the P3Bot mobile manipulator
- Dual **Kinova Gen3 7-DoF** arms (left and right)
- Visual and collision meshes for the full robot

---

## 🧱 Design Principles

Key architectural decisions:

- The Kinova Gen3 arm is defined as a **reusable xacro macro**
- Arms are fully namespaced (`left_`, `right_`) to support dual-arm setups
- Frame conventions follow **REP-103**

---

## 🦾 Kinova Gen3 Integration

The Kinova Gen3 7-DoF arm is integrated as a parametrized xacro macro:

- Independent from the P3Bot base
- Mount position and orientation defined externally
- Suitable for left, right, or single-arm configurations

Mounting is performed using explicit fixed joints, ensuring:
- correct gravity direction
- consistent behavior in RViz
- no hidden transformations inside the arm model

---