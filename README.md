# PGL-QRTeam
This script fetch the QR team data from [PGL](https://3ds.pokemon-gl.com/) website, and display it in a simple offline web page.
## Requirement
```sh
$ pip install -r requirements.txt
```

## Step
#### 1.Download the data
```bash
$ python runner.py download
```

#### 2.View the web page
open web/index.html in your favourite browser! ( I only tested chrome.)

## Update Data
```bash
$ python runner.py clean
$ python runner.py download
```
## Feature
- offline webpage
- filter search with PokemonName/Tariner/CountryCode

## License
GNU General Public License v3.0
