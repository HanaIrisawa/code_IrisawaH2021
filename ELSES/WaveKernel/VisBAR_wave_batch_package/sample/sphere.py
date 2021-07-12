import vtk

source = vtk.vtkSphereSource()
source.SetCenter(0,0,0)
source.SetRadius(8.0)

mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(source.GetOutput())
else:
    mapper.SetInputConnection(source.GetOutputPort())

 
actor = vtk.vtkActor()
actor.SetMapper(mapper)
 
ren = vtk.vtkRenderer()
ren.AddActor(actor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()

renWin.Render()
iren.Start()
