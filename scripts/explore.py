import open3d as o3d
import numpy as np
import cv2

# Paths to dataset
DATA_PATH = "DeFlow_Dataset/Data"
PLY_PATH = f"{DATA_PATH}/PLY_Files"
CAM1_PATH = f"{DATA_PATH}/Cam1"

# ─────────────────────────────────────────
# 1. Visualize a single point cloud
# ─────────────────────────────────────────
def visualize_single_pointcloud(frame="00001"):
    print(f"\n[1] Point cloud — frame {frame}")
    pcd = o3d.io.read_point_cloud(f"{PLY_PATH}/{frame}.ply")
    print(f"  Number of points : {len(pcd.points)}")
    print(f"  First points (x,y,z) : {np.asarray(pcd.points)[:3]}")
    o3d.visualization.draw_geometries([pcd], window_name=f"Point Cloud — Frame {frame}")

# ─────────────────────────────────────────
# 2. Compare two point clouds over time
# ─────────────────────────────────────────
def compare_two_pointclouds(frame1="00001", frame2="00500"):
    print(f"\n[2] Comparing point clouds — {frame1} vs {frame2}")
    pcd1 = o3d.io.read_point_cloud(f"{PLY_PATH}/{frame1}.ply")
    pcd2 = o3d.io.read_point_cloud(f"{PLY_PATH}/{frame2}.ply")

    # Blue = early frame, Red = later frame
    pcd1.paint_uniform_color([0, 0.5, 1])
    pcd2.paint_uniform_color([1, 0.3, 0])

    print(f"  Points in frame {frame1} : {len(pcd1.points)}")
    print(f"  Points in frame {frame2} : {len(pcd2.points)}")

    o3d.visualization.draw_geometries(
        [pcd1, pcd2],
        window_name=f"Blue={frame1} vs Red={frame2}"
    )

# ─────────────────────────────────────────
# 3. Compare three camera frames
# ─────────────────────────────────────────
def compare_three_camera_frames(f1="00001", f2="03000", f3="06000"):
    print(f"\n[3] Camera comparison — {f1} | {f2} | {f3}")
    img1 = cv2.imread(f"{CAM1_PATH}/{f1}.jpg")
    img2 = cv2.imread(f"{CAM1_PATH}/{f2}.jpg")
    img3 = cv2.imread(f"{CAM1_PATH}/{f3}.jpg")

    h, w = img1.shape[:2]
    def resize(img):
        return cv2.resize(img, (w//3, h//3))

    # Side by side: beginning | middle | end of debris flow
    compare = np.hstack([resize(img1), resize(img2), resize(img3)])
    cv2.imshow(f"Frame {f1} (start) | {f2} (middle) | {f3} (end)", compare)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
if __name__ == "__main__":
    visualize_single_pointcloud("00001")
    compare_two_pointclouds("00001", "00500")
    compare_three_camera_frames("00001", "03000", "06000")
EOF