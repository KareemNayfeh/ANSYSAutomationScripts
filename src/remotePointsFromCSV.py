import csv
from config import PATH

# create remote points from CSV
ns_list = DataModel.GetObjectsByName("Named Selections")[0].Children

with open(PATH, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        rp = Model.RemotePoints.AddRemotePoint()
        rp.ScopingMethod = GeometryDefineByType.Component

        for ns in ns_list:
            if ns.Name == row[4]:
                rp.Location = ns
                break

        rp.Name = row[0]
        rp.PilotNodeAPDLName = row[0]
        rp.XCoordinate = Quantity(float(row[1]), "m")
        rp.YCoordinate = Quantity(float(row[2]), "m")
        rp.ZCoordinate = Quantity(float(row[3]), "m")
        rp.PinballRegion = Quantity(float(row[5]), "m")
