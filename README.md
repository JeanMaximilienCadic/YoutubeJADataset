![Youtube Logo](img/youtube.png)
--------------------------------------------------------------------------------

YoutubeJADataset is a Python package that provides a simplified framework based on youtube_dl to download youtube audio and captions easily

You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend Iyo when needed.

We are in an early-release beta. Expect some adventures and rough edges.

- [Installation](#installation)


## Youtube modules

At a granular level, Iyo is a library that consists of the following components:

| Component | Description |
| ---- | --- |
| **YoutubeMaster** | Distributed downloading of the videos from youtube|

## Installation

#### Install IYO and its dependencies

```
# System dependencies
sudo apt-get install g++-5 gcc-5 git sox libsox-dev libsox-fmt-all meshlab python3 python3-pip cmake ffmpeg youtube_dl
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

```

```
# Install python requirements
pip install iyo-utils, gnutools-python, tqdm, numpy
```

