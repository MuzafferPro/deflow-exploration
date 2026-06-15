# DeFlow Dataset Exploration

Personal exploration of the [DeFlow dataset](https://github.com/prs-eth/DeFlow) 
published by ETH Zurich (Zhu et al., CVPRW 2023, Best Paper Award).

This repository documents my hands-on investigation of debris flow data 
as part of my preparation for a PhD position in computer vision applied 
to natural hazards at ETH Zurich.

---

## What is a debris flow?

A debris flow is a rapid mixture of water, mud, rocks and wood that rushes 
down a mountain channel. It can destroy infrastructure and claim lives within 
minutes. Monitoring and understanding these events in real time is a major 
open challenge in geohazard research.

## Dataset

The DeFlow dataset was captured at the Illgraben catchment in Switzerland 
and contains:

- 6,000 camera frames from two synchronized cameras (Cam1, Cam2)
- 6,000 LiDAR point clouds in .ply format, with 131,072 points each
- Calibration files for camera-LiDAR fusion

Each point in the LiDAR scan contains: x, y, z, intensity  
High intensity values correspond to dry rock surfaces.  
Low intensity values correspond to water, mud or wet surfaces.  
Zero values represent invalid returns caused by laser absorption or occlusion.

## Key observations

After exploring the dataset visually, I made the following observations.

On the camera frames:
- Frame 1 shows a calm river bed with very little water and low flow
- Frame 3000 shows dense mud flow with rocks in motion
- Frame 6000 shows peak flow with high volume and maximum pressure at the channel center
- Large rocks tend to concentrate at the center of the channel where hydraulic pressure is highest
- Rain is visible in the frames and introduces visual noise

On the LiDAR point clouds:
- Early frames have fewer valid points because dry and wet surfaces tend to absorb the laser signal
- Later frames show denser and more continuous point clouds as the debris mass reflects the laser more effectively
- Zero-value points at coordinates (0, 0, 0) represent invalid returns and must be filtered before any processing

## Scripts

| Script | Description |
|--------|-------------|
| `scripts/explore.py` | Visualize point clouds and camera frames |

### How to run

```bash
python3 -m venv deflow_env
source deflow_env/bin/activate
pip install open3d numpy matplotlib opencv-python
python3 deflow-exploration/scripts/explore.py
```

## Why this matters

The core challenge of this dataset is that debris flows are non-rigid. 
Unlike autonomous driving scenarios where objects move as rigid bodies, 
every part of a debris flow, whether rocks, mud, water or wood, moves 
differently. Classical motion estimation methods fail here.

DeFlow (Zhu et al., 2023) addresses this with a self-supervised approach. 
Since manual annotation of 3D motion is physically impossible in this context, 
the model learns by enforcing geometric consistency between successive frames.

I am currently studying this approach and reproducing parts of the pipeline 
as a personal research exercise.

## References

- Zhu et al., DeFlow: Self-supervised 3D Motion Estimation of Debris Flow, CVPRW 2023 Best Paper Award
- ETH Zurich Engineering Geology Group
- Dataset: Illgraben catchment, Switzerland