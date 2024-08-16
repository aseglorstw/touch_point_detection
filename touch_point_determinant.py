import meshlib.mrmeshpy as mr
from tools import mesh_tools
from tools import visualize_tools
import time


def determine_touch_points_meshlib(path_to_robot_mesh, terrain_mesh, output_path):
    robot_mesh = mr.loadMesh(path_to_robot_mesh)
    terrain_mesh = mr.loadMesh(terrain_mesh)
    start = time.time()
    intersection = mr.boolean(terrain_mesh, robot_mesh, mr.BooleanOperation.Intersection)
    end = time.time()
    print(end - start)
    mr.saveMesh(intersection.mesh, output_path)


def main():
    path_to_robot_mesh = "/home/robert/catkin_ws/src/robot_touch_point_detection/experiments/first_experiment/transformed_robot.stl"
    path_to_terrain_mesh = "/home/robert/catkin_ws/src/robot_touch_point_detection/experiments/terrain_mesh.obj"
    output_path = "/home/robert/catkin_ws/src/robot_touch_point_detection/experiments/second_experiment/transformed_robot_simplified.stl"
    # determine_touch_points_meshlib()
    # mesh_tools.simplify_mesh_and_save(path_to_robot_mesh, output_path)
    visualize_tools.visualize_two_meshes("/home/robert/catkin_ws/src/robot_touch_point_detection/experiments/second_experiment/transformed_robot_simplified.stl", "/home/robert/catkin_ws/src/robot_touch_point_detection/experiments/first_experiment/terrain_mesh.stl")


if __name__ == '__main__':
    main()
