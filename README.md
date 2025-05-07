<h1 align="center">
  🏘️ ProcTHOR
</h1>

<h3 align="center"><em>Scaling Embodied AI by Procedurally Generating Interactive 3D Environments</em></h3>

![procthor-cover(1)](https://user-images.githubusercontent.com/28768645/191896912-58a2234a-ed50-40b6-a534-348db7260756.jpg)

ProcTHOR procedurally generates interactive, diverse, and semantically plausible houses that are compatible with AI2-THOR.


## Requirements
- Ubuntu 20.04 (Unity 2020.3.25f1 only runs on this Ubuntu version)
- Conda Environment

## To generate the example scene
Run the following code will generate the initial .json file:
```bash
git clone https://github.com/allenai/procthor.git
cd procthor/scripts
conda create --name procthor python=3.10.12
conda activate procthor
pip3 install procthor attrs pandas shapely moviepy==1.0.3 networkx python-fcl scipy invoke torch torchvision compress_json
pip3 install --extra-index-url https://ai2thor-pypi.allenai.org ai2thor==0+8524eadda94df0ab2dbb2ef5a577e4d37c712897
export PYTHONPATH=~/Desktop/procthor
python example.py
```

Run the following to upgrade the .json to make it useable:
```bash
python3 upgrade_house.py temp.json output.json
```

## Load the scene in Unity
1. Install [Unity](https://unity.com/download) and select the editor version `2020.3.25f1`.
2. Clone [AI2-THOR repository](https://github.com/allenai/ai2thor) and switch to the appropriate AI2-THOR commit.
```bash
git clone https://github.com/allenai/ai2thor.git
git checkout 07445be8e91ddeb5de2915c90935c4aef27a241d
```
3. Reinstall some packages:
```bash
pip uninstall Werkzeug
pip uninstall Flask
pip install Werkzeug==2.0.1
pip install Flask==2.0.1
```
4. Load `ai2thor/unity` as project in Unity and open `ai2thor/unity/Assets/Scenes/Procedural/Procedural.unity`.
5. In the terminal, run [this python script](connect_to_unity.py):
```bash
python connect_to_unity --scene <SCENE_JSON_FILE_PATH>
```
6. Press the play button (the triangle) in Unity to load the scene.

## Citation
This code is used to generate houses for the [ProcTHOR](https://procthor.allenai.org/) paper:

```bibtex
@inproceedings{procthor,
  author={Matt Deitke and Eli VanderBilt and Alvaro Herrasti and
          Luca Weihs and Jordi Salvador and Kiana Ehsani and
          Winson Han and Eric Kolve and Ali Farhadi and
          Aniruddha Kembhavi and Roozbeh Mottaghi},
  title={{ProcTHOR: Large-Scale Embodied AI Using Procedural Generation}},
  booktitle={NeurIPS},
  year={2022},
  note={Outstanding Paper Award}
}
```

## 👋 Our Team

ProcTHOR is an open-source project built by the [PRIOR team](//prior.allenai.org) at the [Allen Institute for AI](//allenai.org) (AI2).
AI2 is a non-profit institute with the mission to contribute to humanity through high-impact AI research and engineering.

<br />

<a href="//prior.allenai.org">
<p align="center"><img width="100%" src="https://raw.githubusercontent.com/allenai/ai2thor/main/doc/static/ai2-prior.svg" /></p>
</a>
