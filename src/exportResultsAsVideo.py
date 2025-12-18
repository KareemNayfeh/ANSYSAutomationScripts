from config import PATH

# export images and animations
image_settings = Ansys.Mechanical.Graphics.GraphicsImageExportSettings()
image_settings.CurrentGraphicsDisplay = True

Graphics.ResultAnimationOptions.NumberOfFrames = 8
Graphics.ResultAnimationOptions.Duration = Quantity(3, 's')

solution_items = DataModel.GetObjectsByName("Solution")[0].Children

for result in list(solution_items)[1:]:
    name = result.Name.Replace(" ", "")
    result.ExportAnimation(
        PATH + name + ".mp4",
        GraphicsAnimationExportFormat.MP4
    )
    Graphics.ExportImage(
        PATH + name + "IMG",
        GraphicsImageExportFormat.PNG,
        image_settings
    )
