[![Build Status](https://travis-ci.org/ironcarocto/simulateur_ironcar.svg?branch=master)](https://travis-ci.org/ironcarocto/simulateur_ironcar)

Ce simulateur permet de générer un dataset préqualifié d'images de
route tel que la verrait la caméra d'une **ironcar** associées à la commande de direction pour l'ironcar.

[Ironcar](http://ironcar.org/) est un championnat de courses de voitures
autonomes en modèle réduit !

__2 exemples de sortie de simulateur_ironcar__

![Banner](docs/images/21_cmd_0.png)![Banner](docs/images/155_cmd_2.png)

## Dernière version du code source de ce programme

```bash
git clone https://github.com/ironcarocto/simulateur_ironcar.git
```

## Utiliser le simulateur

1. Installer le simulateur avec pip

```bash
pip install simulateur_ironcar
```

2. Créer un dossier pour un profil de génération de route

```bash
mkdir mydirectory
cd mydirectory
```

3. Initialiser un profile de génération de route depuis ce dossier


```bash
simulateur_ironcar init
```

Vous devez obtenir le dossier suivant

```
.
├── configuration.json
├── grounds
│   ├── IMG_1417.JPG
│   └── IMG_5993.JPG
└── photos
```

* le dossier ``grounds`` contient les terrains sur lesquels vous voulez générer des routes

4. Configurez votre profile de génération de route

    1. placez de nouveaux grounds dans le dossier ``ground``
    2. configurez les valeurs souhaités dans le fichier ``configuration.json``

5. Générez les routes

```
simulateur_ironcar generate
```

les routes sont dans le dossier photos avec le format suivant :

```
photos/cadran=0_angle=14_id=0_did=dataset.png
...
```

les roues droites au sens trigo sont à 90°.

* cadran 0 : roue de 0 à 35° (sens trigo)
* cadran 1 : roue de 35 à 70° (sens trigo)
* cadran 2 : roue de 70° à 110° (sens trigo)
* cadran 3 : roue de 110° à 145° (sens trigo)
* cadran 4 : roue de 145° à 190° (sens trigo)

### contenu du fichier configuration.json

[en savoir plus](docs/configuration_json.md)

## Contribuer au projet

1. créer un environnement virtuel

```
virtualenv venv -p python3
```

2. installer les dépendances de développement

```bash
. venv/bin/activate; pip install -e .[dev]
```

3. exécuter les tests

```bash
. venv/bin/activate; pytest
```

### les commandes de build

```
make help

dist                           package simulateur_ironcar as a wheel and a source distribution
freeze_requirements            update the project dependencies based on setup.py declaration
help                           provides cli help for this makefile (default)
install_requirements_dev       install pip requirements for development
install_requirements           install pip requirements based on requirements.txt
lint                           run pylint
tests                          run automatic tests
tox                            run tests described in tox.ini for multi-python environments
upload                         package and upload simulateur_ironcar on python package index
venv                           build a virtual env for python 3 in ./venv
```

## License

MIT License

Copyright (c) 2019 Constant Bridon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
