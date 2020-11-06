---
date: 2020-11-04
title: "How to install librealsense and pyrealsense2 on the Jetson NX"
layout: base
tags:
  - public
  - howto
  - documentation
permalink: "/{{page.fileSlug}}/"
---

<div class = "toc">

[[toc]]

</div>

## Introduction

**GitHub issue [here](https://github.com/IntelRealSense/librealsense/issues/7722)**

I'm going to send in a PR today just to contribute back to the community.

`pyrealsense2` is a set of Python bindings for Intel's `librealsense` library.
It is needed to run the
[code examples showing how to use LibRealSense's Python wrapper](https://dev.intelrealsense.com/docs/python2).

This set of instructions is a synthesis of both READMEs here:
[Build LibRealSense from source](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)
[Build Python Wrappers](https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python#building-from-source)

Neither of the READMEs give a full set of instructions to follow;
each of them is missing some piece.
I have thus written this how-to mainly for myself to reference in the future,
but also in the hopes that it might save some others' time.
These commands have been tested to work on the Jetson NX running Ubuntu 18.04
and using Python 3.6.9.

This how-to provides a complete set of instructions to install `librealsense`
and its bindings on the Jetson NX.

## Prerequisites

You should first disconnect your RealSense Camera if it is connected,
because the `/setup_udev_rules.sh` bash script requires your camera to be disconnected.

## Instructions

```bash
# Installs librealsense and pyrealsense2 on the Jetson NX running Ubuntu 18.04
# and using Python 3
# Tested on a Jetson NX running Ubuntu 18.04 and Python 3.6.9

sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install -y --no-install-recommends \
    python3 \
    python3-setuptools \
    python3-pip \
	python3-dev

# Install the core packages required to build librealsense libs
sudo apt-get install -y git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
# Install Distribution-specific packages for Ubuntu 18
sudo apt-get install -y libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev

# Install LibRealSense from source
# We need to build from source because
# the PyPi pip packages are not compatible with Arm processors.
# See link [here](https://github.com/IntelRealSense/librealsense/issues/6964).

# First clone the repository
git clone https://github.com/IntelRealSense/librealsense.git
cd ./librealsense

# Make sure that your RealSense cameras are disconnected at this point
# Run the Intel Realsense permissions script
./scripts/setup_udev_rules.sh

# Now the build
mkdir build && cd build
## Install CMake with Python bindings (that's what the -DBUILD flag is for)
## see link: https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python#building-from-source
cmake ../ -DBUILD_PYTHON_BINDINGS:bool=true
## Recompile and install librealsense binaries
## This is gonna take a while! The -j4 flag means to use 4 cores in parallel
## but you can remove it and simply run `sudo make` instead, which will take longer
sudo make uninstall && sudo make clean && sudo make -j4 && sudo make install

## Export pyrealsense2 to your PYTHONPATH so `import pyrealsense2` works
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2
```

`librealsense` and `pyrealsense2` should now be installed on your computer.
To test this,
download an example Python file
(e.g. [opencv_viewer_example.py](https://github.com/IntelRealSense/librealsense/blob/master/wrappers/python/examples/opencv_viewer_example.py))
and run it with `python3 opencv_viewer_example.py`.
You should expect to see a window with both RGBA and depth output.

## Future extensions

I'm currently trying to build a Dockerfile based on this set of instructions.
Let me know if the instructions don't work for you by emailing me at
`lieu(at)lieuzhenghong(dotcom)`.
