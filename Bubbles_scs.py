# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
bullesvtu = XMLUnstructuredGridReader(registrationName='bulles_1.vtu', FileName=['C:\\Users\\stephane.abdulnour\\Projet Fluide\\Exercices\\Bubbles_DRL\\vtu\\bulles_1.vtu'])
bullesvtu.CellArrayStatus = ['RhoC', 'EtaC']
bullesvtu.PointArrayStatus = ['Erreur', 'Vitesse', 'Pression', 'Eta', 'RhoCp', 'LevelSetEntree3Filtree', 'AppartientEntreeM1', 'AppartientEntreeM2', 'AppartientEntreeM3', 'AppartientEntreeM4', 'AppartientEntreeM5', 'AppartientEntreeM6', 'AppartientEntreeM7', 'AppartientEntreeM8', 'AppartientEntreeM9', 'AppartientEntreeM10', 'AppartientEntreeM11', 'AppartientEntreeM12', 'AppartientEntreeM13', 'AppartientEntreeM14', 'AppartientEntreeS', 'AppartientEntreeE1', 'AppartientEntreeE2', 'AppartientEntreeE3', 'AppartientEntreeW1', 'AppartientEntreeW2', 'BordNoeud', 'AppartientEntree3']

# Properties modified on bullesvtu
bullesvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
bullesvtuDisplay = Show(bullesvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
bullesvtuDisplay.Representation = 'Surface'
bullesvtuDisplay.ColorArrayName = [None, '']
bullesvtuDisplay.SelectTCoordArray = 'None'
bullesvtuDisplay.SelectNormalArray = 'None'
bullesvtuDisplay.SelectTangentArray = 'None'
bullesvtuDisplay.OSPRayScaleArray = 'AppartientEntree3'
bullesvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bullesvtuDisplay.SelectOrientationVectors = 'None'
bullesvtuDisplay.ScaleFactor = 2.0958300000000003
bullesvtuDisplay.SelectScaleArray = 'AppartientEntree3'
bullesvtuDisplay.GlyphType = 'Arrow'
bullesvtuDisplay.GlyphTableIndexArray = 'AppartientEntree3'
bullesvtuDisplay.GaussianRadius = 0.10479150000000001
bullesvtuDisplay.SetScaleArray = ['POINTS', 'AppartientEntree3']
bullesvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bullesvtuDisplay.OpacityArray = ['POINTS', 'AppartientEntree3']
bullesvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bullesvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
bullesvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
bullesvtuDisplay.ScalarOpacityUnitDistance = 0.9815476180508688
bullesvtuDisplay.OpacityArrayName = ['POINTS', 'AppartientEntree3']

# reset view to fit data
renderView1.ResetCamera(False)

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [10.47915, 0.0, 10000.0]
renderView1.CameraFocalPoint = [10.47915, 0.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

LoadPalette(paletteName='BlackBackground')

# set scalar coloring
ColorBy(bullesvtuDisplay, ('POINTS', 'LevelSetEntree3Filtree'))

# rescale color and/or opacity maps used to include current data range
bullesvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
bullesvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'LevelSetEntree3Filtree'
levelSetEntree3FiltreeLUT = GetColorTransferFunction('LevelSetEntree3Filtree')

# get opacity transfer function/opacity map for 'LevelSetEntree3Filtree'
levelSetEntree3FiltreePWF = GetOpacityTransferFunction('LevelSetEntree3Filtree')

# Properties modified on levelSetEntree3FiltreeLUT
levelSetEntree3FiltreeLUT.ColorSpace = 'Step'

# Properties modified on levelSetEntree3FiltreeLUT
levelSetEntree3FiltreeLUT.RGBPoints = [-0.00491943, 0.231373, 0.298039, 0.752941, 0.0, 0.865003, 0.865003, 0.865003, 0.014571500000000001, 0.705882, 0.0156863, 0.14902]

# get color legend/bar for levelSetEntree3FiltreeLUT in view renderView1
levelSetEntree3FiltreeLUTColorBar = GetScalarBar(levelSetEntree3FiltreeLUT, renderView1)

# Properties modified on levelSetEntree3FiltreeLUTColorBar
levelSetEntree3FiltreeLUTColorBar.AutoOrient = 0
levelSetEntree3FiltreeLUTColorBar.Orientation = 'Horizontal'
levelSetEntree3FiltreeLUTColorBar.WindowLocation = 'Lower Center'

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1525, 757)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [3.671687520298785, -0.04136615357161178, 10000.0]
renderView1.CameraFocalPoint = [3.671687520298785, -0.04136615357161178, 0.0]
renderView1.CameraParallelScale = 0.9226078144558661

# save screenshot
SaveScreenshot('C:/Users/stephane.abdulnour/Projet Fluide/Exercices/Bubbles_DRL/screenshots/Screenshot_1.png', renderView1, ImageResolution=[1525, 757])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1525, 757)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [3.671687520298785, -0.04136615357161178, 10000.0]
renderView1.CameraFocalPoint = [3.671687520298785, -0.04136615357161178, 0.0]
renderView1.CameraParallelScale = 0.9226078144558661

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).