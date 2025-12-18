from config import PATH

# isolator springs
rps = DataModel.GetObjectsByName("Remote Points")[0].Children
iso_mobile = [rp for rp in rps if rp.Name.StartsWith("iso")]

snippet_text = """
*ulib,PATH,inp
kx = 3.565e+005
kz = 5.4622e+005
*use,make6dofspring,kx,kx,kz,0,0,0,isopp,isoppFixed
*use,make6dofspring,kx,kx,kz,0,0,0,isopm,isopmFixed
*use,make6dofspring,kx,kx,kz,0,0,0,isomm,isommFixed
*use,make6dofspring,kx,kx,kz,0,0,0,isomp,isompFixed
*ulib
"""

for rp in iso_mobile:
    rp.ZCoordinate -= Quantity(0.05, 'm')
    fixed = rp.Duplicate()
    fixed.ScopingMethod = GeometryDefineByType.FreeStanding
    fixed.Name = rp.Name + "Fixed"
    fixed.PilotNodeAPDLName = fixed.Name
    snippet_text += "D,{},ALL,0\n".format(fixed.Name)

modal = DataModel.GetObjectsByName("Modal")[0]
snippet = modal.AddCommandSnippet()
snippet.Input = snippet_text
snippet.Name = "Make Isolators"
