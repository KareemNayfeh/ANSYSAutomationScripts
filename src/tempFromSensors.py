import re
from config import PATH

# helper functions
def get_row(file_path, T):
    best = None
    diff_min = float("inf")

    with open(file_path, 'r') as f:
        next(f)
        for line in f:
            row = line.strip().split(',')
            diff = abs(T - float(row[0]))
            if diff < diff_min:
                diff_min = diff
                best = row
    return best

def is_sensor(name):
    return re.search(r'(NTC|RTD)\d+$', name)

# temperatures
T1 = 0
T2 = 12

ntc1 = get_row(PATH, T1)
ntc2 = get_row(PATH, T2)
rtd1 = get_row(PATH, T1)
rtd2 = get_row(PATH, T2)

geometry = DataModel.GetObjectsByName("Geometry")[0].Children
analysis = DataModel.GetObjectById(266)

for body in geometry:
    for child in body.Children:
        if is_sensor(child.Name):
            idx = int(child.Name[-2:])
            temp = analysis.AddTemperature()
            temp.Name = child.Name[-5:]

            if "NTC" in child.Name:
                delta = float(ntc2[idx]) - float(ntc1[idx])
            else:
                delta = float(rtd2[idx]) - float(rtd1[idx])

            temp.Magnitude.Output.SetDiscreteValue(
                0, Quantity(delta, "C")
            )
            temp.PromoteToNamedSelection()

            ns_list = DataModel.GetObjectsByName("Named Selections")[0].Children
            for ns in ns_list:
                if ns.Name == temp.Name:
                    target = ns
                    break

            target.ScopingMethod = GeometryDefineByType.Worksheet
            crit = target.GenerationCriteria.Add(None)
            crit.EntityType = SelectionType.GeoBody
            crit.Criterion = SelectionCriterionType.Name
            crit.Operator = SelectionOperatorType.Equal
            crit.Value = child.Name
            target.Generate()
