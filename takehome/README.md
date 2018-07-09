@ pgh-data-science


Assumes you have downloaded [Anaconda Distribution](https://www.anaconda.com/download/), but you may be able to get away with

Assumes you have downloaded [Anaconda Distribution](https://www.anaconda.com/download/), but you may be able to get away with

* jupyter notebook
* conda 4.4.10 or higher

## Files

* `green.py` - some helper functions for hiding code and getting data
* `data.json` - a data dictionary for the green taxi dataset.  
* `environment.yml` - YAML for setting up the environment dependencies for `co-dsc.ipynb`.

## Folders

* `pics` - contains images using in the Jupyter Notebook

# Instructions

The main notebook, `TJW-C762132.ipynb`, assumes that you have created an api key for google maps.  

You can follow these [instructions](https://console.developers.google.com/flows/enableapi?apiid=maps_backend,geocoding_backend,directions_backend,distance_matrix_backend,elevation_backend&keyType=CLIENT_SIDE&reusekey=true).
The notebook assumes that the api key is available via the environment variable `GOOGLE_API_KEY`.

From this directory run

`conda env create -f environment.yml`

Once this is complete you will see the following instructions
```
#
# To activate this environment, use:
# > activate co-dsc
#
# To deactivate an active environment, use:
# > deactivate
#
# * for power-users using bash, you must source
#
```

Once you have activated the environment, you must enable some notebook extensions so that some of the visuals display correctly.  In particular,
visuals created with [`gmaps`](https://github.com/pbugnion/gmaps) - a plugin for including interactive Google maps in the IPython Notebook.  

```
jupyter nbextension enable --py --sys-prefix widgetsnbextension
jupyter nbextension enable --py --sys-prefix gmaps
```

Once the extensions habe been enabled, run

`jupyter notebook`

The notebook `co-dsc.ipynb` contains all work.  There is an html version available, just open with any modern browser.
