---
permalink: /index.html
---

# QGis notes

QGIS version 3.4.3-Madeira

## Locate the survey area

* Change CRS (Coordinate Reference System) to EPSG:4326 - WGS 84 (bottom right hand corner of the window)
* Web > QuickMapServices > Bing > Bing Map
* Zoom in on the area

## To Create the random points within a polygon

* Layer > Create Layer > New Shapefile Layer...
	* Filename `C:\whereever\the\project\is\boundary.shp`
	* Geometry type `polygon`
	* OK
* Select the boundary layer (left click)
* Layer > Toggle Editing (= on)
    * OK
* Edit > Add Polygon Feature
* Mark boundary (left click) and finish with right click
* Layer > Toggle Editing (= off)
* Do you want to save the changes to layer boundary?
    * Save
* Edit > Select > Select Feature(s)
* Click on the polygon
* Vector > Research Tools > Random Points Inside Polygons
    * Expression `60` (= the number of points you want)
    * Minimum distance between points `10 meters`
    * Run
    * Close

### Export GPX points for use in View Ranger

* Right click on the points layer
* Save As
* Format GPX 
* Choose a file name
* CRS = (EPSG:4326 - WGS 84)
* don't `Add saved file to map`
* and set `GPX_USE_EXTENSIONS = YES`

### Export CSV XY to convert to grid references with sheet numbers

Don't know why this isn't available in QGis, maybe I am missing something.

* Right click on the points layer
* Save As 
* Format Comma Separated Value
* Choose a file name
* CRS = (EPSG:27700 - OSGB 1936)
* don't `Add saved file to map`
* Layer Option, CREATE_CSVT = YES
* Layer Option, GEOMETRY = AS_XY
* Layer Option, SEPARATOR = COMMA

### Export boundary for reference purposes

A polygon can't be exported as GPX so it needs to be converted to a `track` to be exported.

* Select the boundary layer (left click)
* Edit > Select > Select Feature(s)
* Click on the polygon
* Vector > Geometry Tools > Polygons to Lines
    * Selected features only (ticked)
    * Run
    * Close
* Right click the new line layer
* Export > Save Features As...
    * File name `C:\whereever\the\project\is\boundary.gpx`
    * CRS `EPSG:4326 - WGS 84`
    * Add saved file to map (un ticked)
    * GPX_USE_EXTENSIONS `YES`
    * FORCE_GPX_TRACK `YES`

The resulting file should look like this:

```xml
<?xml version="1.0"?>
<gpx version="1.1" creator="GDAL 2.4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogr="http://osgeo.org/gdal" xmlns="http://www.topografix.com/GPX/1/1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
<metadata><bounds minlat="52.679782899781813" minlon="-2.679492437047489" maxlat="52.695697527520039" maxlon="-2.650486284870098"/></metadata>                  
<trk>
  <extensions>
  </extensions>
  <trkseg>
    <trkpt lat="52.690123302974932" lon="-2.677763072961032">
    </trkpt>
    <trkpt lat="52.691600303568372" lon="-2.669037645070273">
    </trkpt>
    <trkpt lat="52.693648963609128" lon="-2.667622710817716">
    </trkpt>
```

### Import boundary GPX and convert to polygon

* 