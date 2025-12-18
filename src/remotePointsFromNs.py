# create remote points from bearing named selections

ns_list = DataModel.GetObjectsByName("Named Selections")[0].Children
rp_mgr = Model.RemotePoints

for ns in ns_list:
    if ns.Name.StartsWith("bearing"):
        rp = rp_mgr.AddRemotePoint()
        rp.ScopingMethod = GeometryDefineByType.Component
        rp.Name = ns.Name + "_rp"
        rp.Location = ns
        rp.PilotNodeAPDLName = rp.Name
