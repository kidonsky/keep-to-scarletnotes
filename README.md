# Keep to Scarlet Notes
**This is a fork of google-keep-scraper from *jconti* :  https://github.com/jcontini/google-keep-scraper**

**This repo is a project repo, it does work but with minimal functionnalities for the moment.** 

Apparently there's no simple way to export your notes from Google Keep to other notes apps. This script accepts the Keep folder Google Takeout archive, and outputs all of the Keep notes as a txt file compatible with an import for Scarlett Notes app (https://github.com/BijoySingh/Scarlet-Notes). 

This is done independently from Scarlet-Notes app development.

## Install
1. Clone or download this repository
1. Open a terminal to the repository folder (`keep-to-scarletnotes`)
1. Run `pip install -r requirements.txt` to install dependencies

## Run
First we need to download all the Keep files through Google Takeout.
1. Go to [Google Takeout](https://takeout.google.com/settings/takeout)
1. Make sure the 'Keep' checkbox is selected (you can deselect all others)
1. Download and export the archive to a folder that has the 'Keep' folder
1. Move the `Keep` folder into this folder, so it's alongside `keep.py`
1. Run `python keep.py`
1. All of your Keep notes should be exported to txt in the same file.
1. Copy this file in your mobile 
1. From Scarlet Notes, go on the gear to enter parameters and import, then select the txt file you copied

Congratulations, you just finished to import Google Keep notes to your Scarlet Notes app ! 

## Troubleshooting
If you get an error about a missing dependency, be sure to run `pip install -r requirements.txt` prior to running the script so that it can download the dependencies needed.**

**This repo is a project repo, it does work but with minimal functionnalities for the moment.** 
