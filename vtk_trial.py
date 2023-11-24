import numpy as np
from vtk import vtkXMLUnstructuredGridWriter, vtkUnstructuredGrid, vtkPoints, vtkCellArray, vtkFloatArray

# Create a simple sphere
radius = 10.0
center = np.array([0.0, 0.0, 0.0])
theta = np.linspace(0, 2 * np.pi, 100, dtype=np.float32)
phi = np.linspace(0, np.pi, 50, dtype=np.float32)
theta, phi = np.meshgrid(theta, phi)

x = center[0] + radius * np.sin(phi) * np.cos(theta)
y = center[1] + radius * np.sin(phi) * np.sin(theta)
z = center[2] + radius * np.cos(phi)

# Flatten the coordinates
points = np.column_stack((x.flatten(), y.flatten(), z.flatten()))

# Create a VTK unstructured grid
grid = vtkUnstructuredGrid()
points_vtk = vtkPoints()
cells = vtkCellArray()

# Add points to VTK
for point in points:
    point_id = points_vtk.InsertNextPoint(point)
    cells.InsertNextCell(1, [point_id])

grid.SetPoints(points_vtk)
grid.SetCells(1, cells)

# Add scalar data to the points (optional)
scalar_data = np.ones(len(points), dtype=np.float32)  # In this example, all points have a scalar value of 1
vtk_scalar_data = vtkFloatArray()
vtk_scalar_data.SetNumberOfComponents(1)
vtk_scalar_data.SetName('ScalarName')  # You can change 'ScalarName' to a more meaningful name
vtk_scalar_data.SetArray(scalar_data, len(scalar_data), 1)
grid.GetPointData().SetScalars(vtk_scalar_data)

# Write the VTK unstructured grid to a VTU file
writer = vtkXMLUnstructuredGridWriter()
writer.SetFileName('data/sphere.vtu')  # Change 'sphere.vtu' to your desired output file name
writer.SetInputData(grid)
writer.Write()
