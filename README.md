# Timeseries Analysis and Plotting (TAP) Tool

#### Abstract:

The Timeseries Analysis and Plotting (TAP) Tool is being developed to provide exploratory data analysis for the Land 
Change Monitoring, Assessment, and Projection 
([LCMAP](https://eros.usgs.gov/science/land-change-monitoring-assessment-and-projection-lcmap)) project at 
[USGS EROS](https://eros.usgs.gov/).  TAP is an open-source project written in python that uses PyQt5 and matplotlib 
for generating interactive GUIs and plots.  Currently, it provides the following functionality:

* Plot a timeseries of Landsat Analysis Read Data 
([ARD](https://landsat.usgs.gov/ard))
  * Landsat 4-7 Bands 1, 2, 3, 4, 5, 7 Surface Reflectance
  * Landsat 8 Bands 2-7 Surface Reflectance
  * Landsat 4-7 Band 6 Brightness Temperature
  * Landsat 8 Band 10 Brightness Temperature
* Plot model parameters and curve-fits from the Continuous Change Detection and Classification 
([CCDC](https://www.sciencedirect.com/science/article/pii/S0034425714000248)) 
algorithm
* Calculate indices on the fly for plotting and visualization
  * NDVI
  * MSAVI
  * SAVI
  * EVI
  * NDMI
  * NBR
  * NBR-2
* Display RGB visualizations of Landsat ARD
* Export plotted Landsat ARD surface reflectance, brightness temperature, and index values to a .csv file
* Save a plot figure as a .png file
* Save a Landsat ARD RGB display as a .png file
* Save ESRI point shapefile for plotted coordinates


## Installation
These instructions work for both Windows and Linux systems.

lcmap_tap has been installed and tested successfully on Windows 7 & 10, and CentOS Linux (version 7).

Version 1.1.0

_Note: some functionality could be unstable or intermittent as development of LCMAP operations is ongoing._
##

##### System Requirements:

python >= 3.6

PyQt5 == 5.10.1*

matplotlib

numpy

GDAL

pandas

pyyaml

cytoolz

cython

requests

[lcmap-merlin](https://pypi.org/project/lcmap-merlin/)

\* Note on PyQt5:  For development any version of PyQt5>=5.9 is currently suitable.  For running TAP, it is 
recommended to use PyQt5==5.10.1 because of an issue in later versions in which Qtwebengineprocess does not close on
 TAP exit.  If building a stand-alone executable with PyInstaller, PyQt5==5.10.1 seems to work best at the moment.

# 

__The tool currently requires the following data inputs:__
* Serialized change and cover results generated by [PyCCD](https://github.com/USGS-EROS/lcmap-pyccd).
* Landsat ARD (obtained via HTTP request)

***Landsat ARD and the PyCCD algorithm are publicly available.  However, TAP currently requires access to ARD via a 
web-service that is currently available to on-site personnel at USGS EROS only.  In addition, the pre-generated PyCCD 
results must be stored locally and are expected to be in a specific format.  For these reasons, TAP is not intended
for general public use until these datasets become widely available at a future date.***

#

##### Note:
It is recommended to use an [Anaconda](https://www.anaconda.com/) virtual environment since it provides an easier 
method of installation for GDAL, [cython](https://cython.org/), and [cytoolz](https://github.com/pytoolz/cytoolz).  Otherwise, information for installing GDAL manually can be found 
[here](https://www.gdal.org/index.html).  
#
#### Create a Virtual Environment

* Install Anaconda or Miniconda
  * Download [here](https://www.anaconda.com/download/)
* Create a virtual environment with python 3.6, include the following dependencies in the environment creation:
  * __GDAL__
  * __cython__
  * __cytoolz__
  * __numpy__
  * __pandas__
  
  ```bash
  conda create -n <env-name> python=3.6 gdal cython cytoolz numpy pandas
  The following NEW packages will be INSTALLED:
  ...
  Proceed ([y]/n)? y

  ```

* Download the TAP source code [here](https://github.com/USGS-EROS/lcmap-tap/archive/develop-research.zip) and extract the
zipped folder.  From the command line, cd into the extracted folder.

#### Install TAP Source Code

* From the command line, activate the virtual environment (must use source if using bash)
        
* Use pip to install TAP and the remaining dependencies (matplotlib, PyQt, PyYAML, and requests)
  * The reason for using pip to install PyQt is that the most recent version available on conda is 5.9.2
    as of 2/15/2019

    **Windows and Linux**
    ```bash
    pip install --trusted-host pypi.org --trusted-host python.pypi.org --trusted-host files.pythonhosted.org .
    ...

    ```

## Run the Tool

Once installed, lcmap_tap can be executed directly from the command line if the virtual environment 
is activated:
```bash
activate env-name
lcmap_tap
```
