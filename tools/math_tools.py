import torch
from pytorch3d.transforms import euler_angles_to_matrix, Transform3d


def get_transformation_matrix(rotation_tensor, translation_tensor):
    rotation_matrix = euler_angles_to_matrix(rotation_tensor, convention="XYZ")
    transformation_matrix = torch.eye(4)
    transformation_matrix[:3, :3] = rotation_matrix
    transformation_matrix[:3, 3] = translation_tensor
    return transformation_matrix
