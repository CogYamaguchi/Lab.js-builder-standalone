# Lab.js-builder-standalone

This repsository contains a standalone version of [Lab.js](https://lab.js.org/) Builder. It lets you use the Builder on your own computer without connecting the lab.js server. This may be convenient if you have to work on your experiment without an internet connection. 

## How to use the stadalone lab.js builder
To use the standalone lab.js builder, download `standalone-builder.zip` to your Windows PC and unzip it in a folder (to do this, you can either clone the repository or donwload it as a zip file). Then, simply run the exe file `run_builder.exe` in the folder. The Builer will start shortly in your default browser. 

>Note that the `build` folder must be located in the same folder as the exe file. The exe file will launch two new windows, a command prompt that creates something called 'local server' in your computer, and your default browser that accesses the local server and hosts the Builder.

>Currently, the repository hosts two versions of Lab.js Builder. The latest stable version is v20.1.1, which is in the `standalone-builder.zip` file. This is the version used in the current [online Builder](https://labjs.felixhenninger.com/). v20.2.1 is a beta version, which works fine by itself, but the experiment built on v20.2.1 cannot be loaded to v20.1.1. 

## How to close the standalone lab.js builder
To close the standalone Builder, just close both the browser and the command prompt. Closing the browser does not kill the local server, you can open a new browser window and type `localhost:8000` in the address bar will  start the lab.js builder again. If you only close the command prompt, the Builder will still be running on the browser until you close the browser.

## The original script
The original script is written in Python, and it is included in the depository (`run_builder.py`). You can also run the script if Python is installed in your computer. It is compatible with Python3 (for Python2, replace `http.server` with `SimpleHTTPServer` and it should work).

## Updating Builder version
The Builder in this repository is Version 20.1.1. This is the latest stable version as of September 2020. The version may not be updated in this repository very frequently, but you can create the latest version of the Builder standalone by replacing the `build` folder. This requires a bit of work. Namely, you need to create a local copy of the builder by following [this procedure](https://labjs.readthedocs.io/en/latest/meta/contribute/build.html). I got quite a few errors in the process and had to work around problems (mostly about the installation of node.js and yarn, I think). But if successful, you will have a folder containing `packages/builder/build`. Replace the older `build` folder with the new one. The exec file (and Python script) should still work with the new version.

