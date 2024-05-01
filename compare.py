import open3d as o3d
import numpy as np


def load_and_prepare_ply(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    if not pcd.colors:  # Check if there are colors
        # Assign a default color (e.g., red)
        colors = np.array([[1, 0, 0] for _ in range(len(pcd.points))])
        pcd.colors = o3d.utility.Vector3dVector(colors)
    if not pcd.has_normals():
        pcd.estimate_normals()
    return pcd


file_path = "splat.ply"
pcd = load_and_prepare_ply(file_path)
o3d.visualization.draw_geometries([pcd], window_name="Visualize Point Cloud")
