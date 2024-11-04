# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
breeder_unit5_300vtk = FindSource('breeder_unit5_300.vtk')

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=breeder_unit5_300vtk)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'k']
clip1.Value = 1116425.6457595825

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.000331878662109375, -260.5]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.0, 0.000331878662109375, -260.5]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'yPlus'
yPlusLUT = GetColorTransferFunction('yPlus')

# get opacity transfer function/opacity map for 'yPlus'
yPlusPWF = GetOpacityTransferFunction('yPlus')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'yPlus']
clip1Display.LookupTable = yPlusLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'U'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 51.900000000000006
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 2.595
clip1Display.SetScaleArray = ['POINTS', 'U']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'U']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = yPlusPWF
clip1Display.ScalarOpacityUnitDistance = 3.5026490227093023
clip1Display.OpacityArrayName = ['POINTS', 'U']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-9420.7099609375, 0.0, 0.5, 0.0, 2127.86962890625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-9420.7099609375, 0.0, 0.5, 0.0, 2127.86962890625, 1.0, 0.5, 0.0]

# hide data in view
Hide(breeder_unit5_300vtk, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# change representation type
clip1Display.SetRepresentationType('Wireframe')

# change representation type
clip1Display.SetRepresentationType('Points')

# change representation type
clip1Display.SetRepresentationType('Feature Edges')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1119, 904)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [831.1902703472334, -497.58847160486914, 74.47492489533848]
renderView1.CameraFocalPoint = [-5.169239341370082e-14, 0.00033187866212652496, -260.49999999999994]
renderView1.CameraViewUp = [0.568089575819698, 0.7870310472789845, -0.24053349967092016]
renderView1.CameraParallelScale = 265.2964755663519

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).