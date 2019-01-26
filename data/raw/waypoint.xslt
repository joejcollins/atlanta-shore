<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:ogr="http://osgeo.org/gdal" xmlns:gpx="http://www.topografix.com/GPX/1/1" 
    xmlns="http://www.w3.org/1999/xhtml"
    exclude-result-prefixes="ogr gpx">
<xsl:strip-space elements="*"/>
<xsl:output method="xml" omit-xml-declaration="no" indent="yes"/>

<!-- 
Copy everything that has no other pattern defined 
-->
<xsl:template match="*">
<xsl:copy>
    <xsl:copy-of select="@*"/>
    <xsl:apply-templates />
</xsl:copy>
</xsl:template>

<xsl:template match="gpx:extensions">
    <name><xsl:value-of select="ogr:id"/></name>
    <xsl:element name="description" xmlns="http://www.topografix.com/GPX/1/1">Sample Site <xsl:value-of select="ogr:id"/></xsl:element>
</xsl:template>

</xsl:stylesheet>