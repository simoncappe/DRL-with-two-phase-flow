# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import system as sys
"""
if __name__ == '__main__':
    args = sys.args[-2:]
args = '0 1'"""
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
bulles_00150vtu = XMLUnstructuredGridReader(registrationName='bulles_00150.vtu', FileName=['C:\\Users\\stephane.abdulnour\\Projet_Fluide\\Exercices\\Interface_DRL\\resultats\\A3\\Run_0\0\\vtu\\2d\\bulles_00150.vtu'])
bulles_00150vtu.CellArrayStatus = ['RhoC', 'EtaC']
bulles_00150vtu.PointArrayStatus = ['Erreur', 'Vitesse', 'Pression', 'Eta', 'RhoCp', 'LevelSetEntree3Filtree', 'LevelSetEntree3', 'diff', 'tape', 'AppartientTop', 'BordNoeud', 'AppartientEntree3', 'AppartientEntreeE1', 'AppartientEntreeE2', 'AppartientEntreeE1_bis', 'AppartientEntreeE2_bis', 'ParaboleE1X', 'ParaboleE1Y', 'ParaboleE2X', 'ParaboleE2Y', 'AppartientEntreeS', 'AppartientEntreeGoal', 'X', 'Y', 'AppartientEntreeC']

# Properties modified on bulles_00150vtu
bulles_00150vtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
bulles_00150vtuDisplay = Show(bulles_00150vtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
bulles_00150vtuDisplay.Representation = 'Surface'
bulles_00150vtuDisplay.ColorArrayName = [None, '']
bulles_00150vtuDisplay.SelectTCoordArray = 'None'
bulles_00150vtuDisplay.SelectNormalArray = 'None'
bulles_00150vtuDisplay.SelectTangentArray = 'None'
bulles_00150vtuDisplay.OSPRayScaleArray = 'AppartientEntree3'
bulles_00150vtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bulles_00150vtuDisplay.SelectOrientationVectors = 'None'
bulles_00150vtuDisplay.ScaleFactor = 1.159099
bulles_00150vtuDisplay.SelectScaleArray = 'AppartientEntree3'
bulles_00150vtuDisplay.GlyphType = 'Arrow'
bulles_00150vtuDisplay.GlyphTableIndexArray = 'AppartientEntree3'
bulles_00150vtuDisplay.GaussianRadius = 0.05795495
bulles_00150vtuDisplay.SetScaleArray = ['POINTS', 'AppartientEntree3']
bulles_00150vtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bulles_00150vtuDisplay.OpacityArray = ['POINTS', 'AppartientEntree3']
bulles_00150vtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bulles_00150vtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
bulles_00150vtuDisplay.PolarAxes = 'PolarAxesRepresentation'
bulles_00150vtuDisplay.ScalarOpacityUnitDistance = 0.5663673166182984
bulles_00150vtuDisplay.OpacityArrayName = ['POINTS', 'AppartientEntree3']

# reset view to fit data
renderView1.ResetCamera(False)

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4.204505, 0.0, 10000.0]
renderView1.CameraFocalPoint = [4.204505, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(bulles_00150vtuDisplay, ('POINTS', 'LevelSetEntree3Filtree'))

# rescale color and/or opacity maps used to include current data range
bulles_00150vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
bulles_00150vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'LevelSetEntree3Filtree'
levelSetEntree3FiltreeLUT = GetColorTransferFunction('LevelSetEntree3Filtree')

# get opacity transfer function/opacity map for 'LevelSetEntree3Filtree'
levelSetEntree3FiltreePWF = GetOpacityTransferFunction('LevelSetEntree3Filtree')

# get color legend/bar for levelSetEntree3FiltreeLUT in view renderView1
levelSetEntree3FiltreeLUTColorBar = GetScalarBar(levelSetEntree3FiltreeLUT, renderView1)

# change scalar bar placement
levelSetEntree3FiltreeLUTColorBar.Orientation = 'Horizontal'
levelSetEntree3FiltreeLUTColorBar.WindowLocation = 'Any Location'
levelSetEntree3FiltreeLUTColorBar.Position = [0.3361205766710353, 0.04396984924623118]
levelSetEntree3FiltreeLUTColorBar.ScalarBarLength = 0.3299999999999999

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1526, 796)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4.204505, 0.0, 10000.0]
renderView1.CameraFocalPoint = [4.204505, 0.0, 0.0]
renderView1.CameraParallelScale = 3.4299127458185406

# save screenshot
SaveScreenshot('C:/Users/stephane.abdulnour/Projet_Fluide/Exercices/Interface_DRL/resultats/A3/Run_0/Screenshots/vtu_0.png', renderView1, ImageResolution=[1526, 796])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1526, 796)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4.204505, 0.0, 10000.0]
renderView1.CameraFocalPoint = [4.204505, 0.0, 0.0]
renderView1.CameraParallelScale = 3.4299127458185406

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).