[![Test](https://github.com/bartekbiz/ctplot/actions/workflows/test.yml/badge.svg)](https://github.com/bartekbiz/ctplot/actions/workflows/test.yml)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/bartekbiz/ctplot)


# CTPlot

Application in python that draws graphs of analog signals, developed for university course digital measuring techniques (*pl. cyfrowe techniki pomiarowe*). It contains functions that simplifies calculations that we conducted during our laboratories. 


## About

Application lets users select one of calculation modules. Currently, two modules are available: the Displacement Module and the Flow Module. The thoughtful architecture allows for the easy addition of new modules in the future. These modules share some core functionalities while also offering specialized functions unique to them.

Shared functionalities include:

- Drawing multiple plots based on the chosen module,
- Specifying the instrument's measuring range,
- Calculating and displaying statistics in the left pane,
- Setting limit values for each graph,
- Defining sampling intervals (span) for graph generation.

</br>

### 1. Displacement module:

This module allows users to visualize displacement data recorded as an analog signal. It also helps the analysis by calculating and plotting the signal's velocity and acceleration.

<img width="1192" alt="screen_displacement_module" src="https://github.com/bartekbiz/ctplot/assets/95227378/c1e5918c-8d37-4ce3-8ac5-a8650b5aefc8">


### 2. Flow module:

This module allows users to visualize and analize flow data recorded as an analog signal. It generates three plots: voltage, processed voltage based on device range (x-plot), and the velocity derived from the x-plot.

Additionally in flow mode users can:
- Specify pipe diameter,
- Get calculated cross-sectional area, Flow value and V-average.

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


## Authors

CTPlot was created by [Mateusz Grochowski](https://github.com/Gromate), [Bartek Bizoń](https://github.com/bartekbiz/), [Filip Gnojek](https://github.com/alien2fg) and [Vladyslav Dikhtiaruk](https://github.com/vladdikhtia)


## License

GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.

