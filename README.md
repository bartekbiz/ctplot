[![Test](https://github.com/bartekbiz/ctplot/actions/workflows/test.yml/badge.svg)](https://github.com/bartekbiz/ctplot/actions/workflows/test.yml)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/bartekbiz/ctplot)


# CTPlot

Application in python that draws graphs of analog signals, developed for university course digital measuring techniques (*pl. cyfrowe techniki pomiarowe*). It contains functions that simplifies calculations that we conducted during our laboratories. 

## About

<img width="1192" alt="screen_displacement_module" src="https://github.com/bartekbiz/ctplot/assets/95227378/c1e5918c-8d37-4ce3-8ac5-a8650b5aefc8">

<img width="1192" alt="screen_flow_module" src="https://github.com/bartekbiz/ctplot/assets/95227378/0139e562-7a0c-48e6-b71a-f1830c6da4c1">


## Usage
To run program you simply need to download most recent version of repo and cd into directory
```bash
git clone https://github.com/bartekbiz/ctplot
cd ctplot
```

Create venv in the directory and activate venv (or skip if you already have required packages on your pc)
```bash
python -m venv venv
```

Activate venv on windows
```bash
.\venv\Scripts\Activate.ps1
```

And finally you can run
```
python3 main.py
```



## Functions

Selection of counting modes (Discplacement/Flow)
Possibility to specify the measuring range of the instrument
Display of chart limit values
Possibility of specifying limit values for each graph
Possibility to specify sampling values for graph drawing(span)
Chart reset button(reset)
Button for activating changes to chart limits(apply)

Additionally in flow mode
Pipe diameter can be specified(Diameter)
Display of chart limit values and cross-sectional area, V-average and Flow value

## Authors

CTPlot was created by [Mateusz Grochowski](https://github.com/Gromate), [Bartek Bizoń](https://github.com/bartekbiz/), [Filip Gnojek](https://github.com/alien2fg) and [Vladyslav Dikhtiaruk](https://github.com/vladdikhtia)

## License

GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.
