import launch
import launch.actions
import launch.substituions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actons.Node(
            psckage='mypkg',
            executable='talker',
            )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='listener',
            output='screen'
            )

    return launch.LaunchDescription([talker, listener])
