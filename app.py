# non-native libraries
import yaml
import inflection

# native libraries
import sys

# determine runtime argument if it exists
# otherwise default to Chun Li
# use argv[1] because argv[0] is the filename app.py
# python [0] [1] ...
# python app.py Ryu
if len(sys.argv) > 1:
    fighter = sys.argv[1]
else:
    fighter = "Chun Li"


# pick the first item if it is a dict instead of a string
# i.e. HomeCountry/County
def get_first(val):
    if type(val) is dict:
        return next(v for k, v in val.items())
    else:
        return val


if __name__ == '__main__':
    file = open("data.yaml")
    data = yaml.safe_load(file)
    fighters = data["Fighters"]["Fighter"]

    # print the fighter name specified at runtime (or default Zangief)
    print(fighter)

    # loop through the dict items and print them
    for k, v in fighters[fighter].items():
        #v = get_first(v)
        print(k, v)

        # pluralize the item
        #print(f"{inflection.pluralize(k)} {inflection.pluralize(v)}")

        # tableize the item, for example if you're working with databases
        #print(f"{inflection.tableize(k)} {inflection.tableize(v)}")

        # titleize the item
        #print(f"{inflection.titleize(k)} {inflection.titleize(v)}")
