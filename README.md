# Mullpy
[![Build Status](https://travis-ci.org/franccesco/mullpy.svg?branch=master)](https://travis-ci.org/franccesco/mullpy) [![Coverage Status](https://coveralls.io/repos/github/franccesco/mullpy/badge.svg?branch=develop)](https://coveralls.io/github/franccesco/mullpy?branch=develop)

A little tool to check if you're currently connected to **Mullvad** VPN or not and also checks for an open port and a DNS leak test. If you want to read more about Mullvad VPN you can goa head and read the _very flattering_ [Mullvad review here](https://thatoneprivacysite.net/2017/10/03/mullvad-review/) by [That One Privacy Site](https://thatoneprivacysite.net/)

The tool _does not_ intend to be a swiss army knife, just a two day mini-project so I don't have to go to [am.i.mullvad.net](http://am.i.mullvad.net/) everytime to check on my connection. **For WebRTC you should go to their website!**

![Mullvad ON](assets/mullvad_on.png)

# Installation

**Requirements:**
* Python 3.6 and up.

**Instalation vía Pip:**
```bash
$ pip install --user mullvad-python
```

# Usage
```bash
$ mullpy
   \  |         |  |               
  |\/ |  |   |  |  |  __ \   |   | 
  |   |  |   |  |  |  |   |  |   | 
 _|  _| \__,_| _| _|  .__/  \__, | 
                     _|     ____/  

Using Mullvad:	True
Server Type:	Wireguard
IP Address:	185.232.22.59
Country:	New York, United States
Location:	-74.0052, 40.7214
Organization:	M247 Europe SRL
Blacklisted: 	False

$ mullpy --help
Usage: mullpy [OPTIONS]

  CLI for Mullvad API.

Options:
  -d, --dns           Check for DNS leak.
  -p, --port INTEGER  Checks for open port
  --help              Show this message and exit.
```

# Contribution
If you want to contribute to the project then:
1. Fork the project.
2. Make changes.
2. Make a pull request to the **develop** branch.

# TODO
- [x] CLI
- [x] Testing
- [x] Continuous Integration
- [x] Code Coverage
- [x] Port Checking
- [x] DNS Leak Test

# Support this project
If you like the project and would like to support me you can buy me a cup of coffee, that would be much appreciated 🙏. If you can't, don't worry, enjoy it!

<a href="https://www.paypal.me/orozcofranccesco">
  <img height="32" src="assets/paypal_badge.png" />
</a> <a href="https://www.buymeacoffee.com/franccesco" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/white_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> <a href='https://ko-fi.com/V7V8AXFE' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi2.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
