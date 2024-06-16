[![Test](https://github.com/bartekbiz/ctplot/actions/workflows/test.yml/badge.svg)](https://github.com/bartekbiz/ctplot/actions/workflows/test.yml)

# CTPlot

Application in python that draws graphs of analog signals.


## About

Application lets users select one of calculation modules. Currently, two modules are available: the Displacement Module and the Flow Module. The thoughtful architecture allows for the easy addition of new modules in the future. These modules share some core functionalities while also offering specialized functions unique to them.

Shared functionalities include:

- Drawing multiple plots based on the chosen module,
- Specifying the instrument's measuring range,
- Calculating and displaying statistics in the left pane,
- Setting limit values for each graph,
- Defining sampling intervals (span) for graph generation.


### 1. Displacement module:

This module allows users to visualize displacement data recorded as an analog signal. It also helps the analysis by calculating and plotting the signal's velocity and acceleration.

<img width="1192" alt="screen_displacement_module" src="https://github.com/bartekbiz/ctplot/assets/95227378/c1e5918c-8d37-4ce3-8ac5-a8650b5aefc8">


### 2. Flow module:

This module allows users to visualize and analize flow data recorded as an analog singal. It draws 3 plots: voltage plot, x plot which is multiplied voltage by device range and the velocity of x.

Additionally in flow mode users can:
- Specify pipe diameter,
- Get calculated cross-sectional area, Flow value and V-average.

<img width="1192" alt="screen_flow_module" src="https://github.com/bartekbiz/ctplot/assets/95227378/0139e562-7a0c-48e6-b71a-f1830c6da4c1">


## Installation

```bash
cd ctplot
python -m venv .
pip install -r requirements.txt
```

## License

GPL


