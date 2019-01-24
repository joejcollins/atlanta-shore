---
permalink: /index.html
---

*To Create the points*

1. Web - Quick Map Services - Bing Map 
2. Change CRS to EPSG:4326 (bottom right hand corner of the map)
3. New Shapefile Layer (line with star in yellow box) and choose Polygon
4. Save file with .shp extension
5. Toggle Editing (yellow pencil)
6. Add feature Green (green blob with star in yellow box)
7. Create area, right click to finish
8. Select the area (yellow with pointer)
9. Vector - Research Tools - Random points inside polygon

*To Export GPX for use in View Ranger*

1. Right click on the points layer
2. Save As
3. Format GPX 
4. Choose a file name
5. CRS = (EPSG:4326 - WGS 84)
6. don't `Add saved file to map`
7. and set `GPX_USE_EXTENSIONS = YES`

*To Export CSV OS XY to convert to grid references with sheet numbers*

1. Right click on the points layer
2. Save As 
3. Format Comma Separated Value
4. Choose a file name
5. CRS = (EPSG:27700 - OSGB 1936)
6. don't `Add saved file to map`
7. Layer Option, CREATE_CSVT = YES
8. Layer Option, GEOMETRY = AS_XY
9. Layer Option, SEPARATOR = COMMA
