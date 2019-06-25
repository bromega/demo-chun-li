# Demo - Chun Li

This is a Python 3.7 demo

## Requirements

* Python 3.7+
* Git

## Instructions

* [Git](#git)
* [Virtual Environments](#virtual-environments)
* [Dependencies](#dependencies)
* [The Script](#the-script)
  * [Step 1](#step-1)
  * [Step 2](#step-2)
  * [argparse](#argparse)
  * [Step 3](#step-3)
  * [dpath](#dpath)
  * [Step 4](#step-4)

### Git

On your machine, open Terminal or Powershell or Command Prompt. Create a directory for this demo (if you haven't already) and navigate to it:

```
mkdir demo
cd demo
```

Clone this repository:

```
git clone https://github.com/bromega/demo-chun-li.git
```

Navigate to the repository directory:

```
cd demo-chun-li
```

Create a branch and give it a snazzy title (use hyphens for spaces):

```
git checkout -b vega-is-just-spanish-wolverine
```

Run the file:

`python app.py ` or `python3 app.py`

But wait! There's an error! Something like this:

```
File "app.py", line 2, in <module>
  import yaml
ModuleNotFoundError: No module named 'yaml'
```

That's because we are running this on the root machine and not in a virtual environment with the necessary libraries installed.

### Virtual Environments

Create the virtual environment with Python3. Check which version is the default on your root machine:

```
python --version
```

If your machine is only running Python3 or has it as the default:

```
python -m venv venv
```

If your machine runs Python2 and Python3 (for example, OSX ships with Python2 standard):

```
python3 -m venv venv
```

If you only have Python2 installed, install Python3 before proceeding.

---


Activate the virtual environment depending on your command line application

* Terminal: ` source venv/bin/activate `
* cmd.exe ` venv\Scripts\activate.bat `
* Powershell: ` venv\Scripts\Activate.ps1 `

Once inside the virtual environment, your prompt should change to whatever you named your environment (in this case "venv") for example:

```
MFVFWJN2SJ1WL:demos oliver.williams$ source venv/bin/activate
(venv) MFVFWJN2SJ1WL:demos oliver.williams$
```

### Dependencies

Install the required libraries

```
pip install -r requirements.txt
```

Now run the script

```
python app.py
```

Instead of errors you should see a print out of data

### The Script

What's going on in this script? It's reading YAML data from data.yaml and printing it out in the command prompt.

What does app.py print out by default?

```
Chun Li
HomeCountry {'Country': 'China', 'Flag': 'Five Stars'}
DefaultColor Blue
SweetMove Helicopter Kick
```

#### Step 1

Huh, that doesn't look sweet at all. Let's look at the code:

```
print(k, v)
```

And how is the YAML file structured?

```
Fighters:
  Fighter:
    Zangief:
      HomeCountry:
        Country: USSR
        Flag: 'Hammer and Sickle'
      DefaultColor: Red
      SweetMove: '360 Piledriver'
      ...
```

#### Step 2

Ok, so we just want to pull the Country node from HomeCountry. The script has a handy function just for this purpose called get_first. It returns the value of the first item if the passed "val" is a dictionary. Otherwise it will just pass back the original "val":

```
def get_first(val):
    if type(val) is dict:
        return next(v for k, v in val.items())
    else:
        return val
```

Uncomment this line in the script:

```
v = get_first(v)
```

Now run the script again:

```
python app.py
```

Output:

```
Chun Li
HomeCountry China
DefaultColor Blue
SweetMove Helicopter Kick
```

#### Step 3

What if I want to see data on other characters?

```
python app.py Blanka
```

Output:

```
Blanka
HomeCountry Brazil
DefaultColor Orange
SweetMove Electricity
```

We're determining the attribute at runtime by leveraging the native library _sys_ and its attribute _argv_.

```
if len(sys.argv) > 1:
    fighter = sys.argv[1]
else:
    fighter = "Chun Li"
```

There are other more robust libraries for this like [argparse](https://docs.python.org/3/library/argparse.html) which is covered in more detail in [demo-zangief](https://github.com/bromega/demo-zangief)

#### Install inflection

Let's see what else is going on in the script. Uncomment out this line about pluralizing attributes, so the code looks like this:

```
# pluralize the item
print(f"{inflection.pluralize(k)} {inflection.pluralize(v)}")
```

Run the script:

```
python app.py
```

Output:

```
File "app.py", line 42, in <module>
  print(f"{inflection.pluralize(k)} {inflection.pluralize(v)}")
NameError: name 'inflection' is not defined
```

Zoinks! We need to install the non-standard library [inflection](https://inflection.readthedocs.io/en/latest/)

If you're just testing out inflection, you could install inflection directly with:

```
pip install inflection
```

However, once you've determined you're going to use it going forward, you will need to add it to the requirements file for others to use in their environments.

In your requirements.txt file, add inflection:

```
PyYAML
inflection
```

Now from your command prompt, install the requirements.txt file again

```
pip install -r requirements.txt
```

#### Step 4

At the top of app.py, add a line to import inflection

```
import yaml
import inflection
```

Run the script:

```
python app.py
```

Output:

```
Chun Li
HomeCountry China
HomeCountries Chinas
DefaultColor Blue
DefaultColors Blues
SweetMove Helicopter Kick
SweetMoves Helicopter Kicks
```

Run the script with an argument:

```
python app.py Blanka
```

Output:

```
Blanka
HomeCountry Brazil
HomeCountries Brazils
DefaultColor Orange
DefaultColors Oranges
SweetMove Electricity
SweetMoves Electricities
```

Now uncomment the rest of the print commands so your code looks like this:

```
# pluralize the item
print(f"{inflection.pluralize(k)} {inflection.pluralize(v)}")

# tableize the item, for example if you're working with databases
print(f"{inflection.tableize(k)} {inflection.tableize(v)}")

# titleize the item
print(f"{inflection.titleize(k)} {inflection.titleize(v)}")
```

Run the script:

```
python app.py
```

Output:

```
Chun Li
HomeCountry China
HomeCountries Chinas
home_countries chinas
Home Country China
DefaultColor Blue
DefaultColors Blues
default_colors blues
Default Color Blue
SweetMove Helicopter Kick
SweetMoves Helicopter Kicks
sweet_moves helicopter kicks
Sweet Move Helicopter Kick
```

Pretty neat!

#### Finishing Touches

Make sure all your files are saved

Add the changes to staging:

```
git add .
```

Check the status of your files and commit to make sure everything looks good:

```
git status
```

Commit the changes to your git branch with a helpful message:

```
git commit -m "added inflection to test functionality"
```

Push the changes to your branch

```
git push
```
