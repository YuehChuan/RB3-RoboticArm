# KEEP UBUNTU OR DEBIAN UP TO DATE

sudo apt -y update
sudo apt -y upgrade
sudo apt -y dist-upgrade
sudo apt -y autoremove


# INSTALL THE DEPENDENCIES

# Build tools:
sudo apt install -y build-essential cmake

# GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):
sudo apt install -y qt5-default libvtk6-dev
sudo apt install -y libqt5opengl5-dev
sudo apt install -y python3-pyqt5.qtopengl python3-opengl

# Media I/O:
sudo apt install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libopenexr-dev libgdal-dev

# Video I/O:
sudo apt install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libxine2-dev

# Parallelism and linear algebra libraries:
sudo apt install -y libtbb-dev libeigen3-dev
sudo apt install -y  libatlas-base-dev libclblas-dev

# gstreamer and vtk
sudo apt install -y libgstreamer1.0-0
sudo apt install libgstreamer-plugins-*-dev
sudo apt install -y vtk6 python-vtk6

# Python:
sudo apt install -y python3-pip
sudo apt install -y python3-dev python3-tk python3-numpy
sudo apt install -y python3-scipy 
pip3 install wheel

# Java:
sudo apt install -y ant default-jdk

# Documentation:
sudo apt install -y doxygen
sudo apt install -y unzip wget
sudo apt clean

# INSTALL THE LIBRARY (YOU CAN CHANGE '3.2.0' FOR THE LAST STABLE VERSION)

cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
unzip opencv_contrib.zip

cd opencv-3.2.0
mkdir build
cd build

# Fixes FFPMEG related errors.
sed -i '1s/^/#define AV_CODEC_FLAG_GLOBAL_HEADER (1 << 22)\n#define CODEC_FLAG_GLOBAL_HEADER AV_CODEC_FLAG_GLOBAL_HEADER\n#define AVFMT_RAWPICTURE 0x0020\n/' ~/opencv-3.2.0/modules/videoio/src/cap_ffmpeg_impl.hpp

cmake -D CMAKE_BUILD_TYPE=RELEASE -DBUILD_SHARED_LIBS=OFF -DBUILD_EXAMPLES=OFF -DBUILD_opencv_apps=OFF -DBUILD_DOCS=OFF -DBUILD_PERF_TESTS=OFF -DBUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX=/usr/local -DENABLE_PRECOMPILED_HEADERS=OFF -DWITH_LIBV4L=ON -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=OFF -DWITH_GDAL=ON -DWITH_XINE=ON -DWITH_OPENMP=ON -DWITH_GSTREAMER=ON -DWITH_OPENCL=ON -DWITH_LIBV4L=OFF -DWITH_V4L=ON -DWITH_DSHOW=ON -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules ../

make -j 8
sudo make install
sudo ldconfig

#install the imutils (which depend on the OpenCV just built)
sudo -H pip3 install setuptools --upgrade
pip3 install imtools


# EXECUTE SOME OPENCV EXAMPLES AND COMPILE A DEMONSTRATION

# To complete this step, please visit 'http://milq.github.io/install-opencv-ubuntu-debian'.

