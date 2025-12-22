from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    use_meshes_arg = DeclareLaunchArgument(
        'use_meshes',
        default_value='true',
        description='Use mesh files if true, otherwise use primitives'
    )

    pkg_share = get_package_share_directory('p3bot_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'P3Bot.urdf.xacro')

    robot_description = {'robot_description': Command([
        'xacro ', urdf_file, ' use_meshes:=', LaunchConfiguration('use_meshes')
    ])}

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen'
    )

    return LaunchDescription([
        use_meshes_arg,
        robot_state_publisher_node,
        joint_state_publisher_node
    ])
