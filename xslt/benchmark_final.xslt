<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xccdf="http://checklists.nist.gov/xccdf/1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <!-- Root template -->
  <xsl:template match="/">
    <html>
      <head>
        <title>Benchmark Results</title>
        <style>
          body { font-family: Arial, sans-serif; }
          table { border-collapse: collapse; width: 100%; }
          th, td { border: 1px solid #ddd; padding: 8px; }
          th { background-color: #f2f2f2; }
          tr:nth-child(even) { background-color: #f9f9f9; }
        </style>
      </head>
      <body>
        <h1>Benchmark Results</h1>
        <xsl:apply-templates select="//xccdf:Benchmark"/>
      </body>
    </html>
  </xsl:template>

  <!-- Template for Benchmark -->
  <xsl:template match="xccdf:Benchmark">
    <h2><xsl:value-of select="xccdf:title"/></h2>
    <div><xsl:apply-templates select="xccdf:description/xhtml:p"/></div>
    <div>
      <strong>Version:</strong> <xsl:value-of select="xccdf:version"/><br/>
      <strong>Status:</strong> <xsl:value-of select="xccdf:status"/><br/>
      <strong>Platform:</strong> <xsl:value-of select="xccdf:platform/@idref"/>
    </div>
    <h3>Profiles</h3>
    <xsl:apply-templates select="xccdf:Profile"/>
  </xsl:template>

  <!-- Template for descriptions -->
  <xsl:template match="xccdf:description/xhtml:p">
    <p><xsl:apply-templates/></p>
  </xsl:template>

  <!-- Template for Profiles -->
  <xsl:template match="xccdf:Profile">
    <h4><xsl:value-of select="xccdf:title"/></h4>
    <div><xsl:apply-templates select="xccdf:description/xhtml:p"/></div>
    <h5>Selected Rules</h5>
    <table>
      <tr>
        <th>Rule ID</th>
        <th>Selected</th>
        <th>Rule Title</th>
        <th>Description</th>
        <th>Status</th>
      </tr>
      <xsl:for-each select="xccdf:select">
        <tr>
          <td><xsl:value-of select="@idref"/></td>
          <td><xsl:value-of select="@selected"/></td>
          <td><xsl:value-of select="key('rule', @idref)/xccdf:title"/></td>
          <td><xsl:value-of select="key('rule', @idref)/xccdf:description/xhtml:p"/></td>
          <td><xsl:value-of select="key('rule', @idref)/xccdf:status"/></td>
        </tr>
      </xsl:for-each>
    </table>
  </xsl:template>

  <!-- Template for Rules -->
  <xsl:template match="xccdf:Rule">
    <xsl:variable name="ruleId" select="@id"/>
    <xsl:variable name="ruleTitle" select="xccdf:title"/>
    <xsl:variable name="ruleDescription" select="xccdf:description/xhtml:p"/>
    <xsl:variable name="ruleStatus" select="xccdf:status"/>

    <div id="{$ruleId}">
      <h5><xsl:value-of select="$ruleTitle"/></h5>
      <p><xsl:apply-templates select="$ruleDescription"/></p>
      <p><strong>Status:</strong> <xsl:value-of select="$ruleStatus"/></p>
    </div>
  </xsl:template>

  <!-- Template for Group -->
  <xsl:template match="xccdf:Group">
    <div>
      <h4>Group: <xsl:value-of select="xccdf:title"/></h4>
      <xsl:apply-templates select="xccdf:Rule"/>
      <xsl:apply-templates select="xccdf:Group"/>
    </div>
  </xsl:template>

  <!-- Key for rules -->
  <xsl:key name="rule" match="xccdf:Rule" use="@id"/>
</xsl:stylesheet>
