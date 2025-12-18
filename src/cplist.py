# build CPLIST APDL snippet

rps = DataModel.GetObjectsByName("Remote Points")[0].Children
names = [rp.PilotNodeAPDLName for rp in rps]

cmd = "*dim,CPLIST,string,32,{}\n".format(len(names))

for i, name in enumerate(names, start=1):
    cmd += "CPLIST(1,{}) = '{}'\n".format(i, name)

solution = DataModel.GetObjectsByName("Solution")[0]
snippet = solution.AddCommandSnippet()
snippet.Input = "resume\nalls\n" + cmd
snippet.Name = "Define CPLIST"
