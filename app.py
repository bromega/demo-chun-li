import inflection
import yaml

file = open("data.yaml")
data = yaml.safe_load(file)
fighters = data["Fighters"]["Fighter"]
for k in fighters["Zangief"].keys():
    print(k)
    print(f"pluralize: {inflection.pluralize(k)}")
    print(f"tableize: {inflection.tableize(k)}")
    print(f"titleize: {inflection.titleize(k)}")
