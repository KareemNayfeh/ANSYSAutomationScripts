import csv
from config import PATH

# create coordinate systems from CSV
csys_mgr = Model.CoordinateSystems

with open(PATH, 'r') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        csys = csys_mgr.AddCoordinateSystem()
        csys.Name = row[0]
        csys.OriginDefineBy = CoordinateSystemAlignmentType.Fixed
        csys.OriginX = Quantity(float(row[1]), "m")
        csys.OriginY = Quantity(float(row[2]), "m")
        csys.OriginZ = Quantity(float(row[3]), "m")
