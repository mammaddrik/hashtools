<h1 align="center">
    <br>
    <a href="https://github.com/mammaddrik/hashtools"><img src="https://i.postimg.cc/yYD6rsH9/logo.png" alt="Hash Tools"></a>
    <br>
    Hash Tools
    <br>
</h1>

<h3 align="center">Tools for Hash Cracker & Generator</h3>

<p align="center">
  <a href="https://github.com/mammaddrik/hashtools/releases">
    <img src="https://img.shields.io/github/release/mammaddrik/hashtools.svg">
  </a>
</p>
<h1 align="center">
    <a href="https://github.com/mammaddrik/hashtools"><img src="https://i.postimg.cc/mDmGWCfY/demo.png" alt="Hash Tools"></a>
</h1>

### Contents  
[Features](#features)<br>
[Installation](#installation)<br>
[Usage](#usage)<br>
[License](#license)

A Python script to crack the hash and create a hash with a different algorithm.

## Features
- Automatic hash type identification.
- Supports MD5, SHA1, SHA256, SHA384, SHA512.

## Installation
> **Note:** Hashtools isn't compatible with python2, run it with python3 instead.<br>
> I suggest you definitely use [cmder](https://cmder.app/).
```
git clone https://github.com/mammaddrik/hashtools.git
cd hashtools
pyrhon pip install -r requirements.txt
python hashtools.py
```
> **Note:** You may encounter an error while installing this requirements. If an error occurs, use the following command:
```
python -m pip install --upgrade pip
pip install hashlib
```
## Usage
After installing the script, you can choose two options from the script:<br>

1. It is for Cracking the hash:
    > **Note:** To crack, you must use a passwordlist.

    [![hashcracker.png](https://i.postimg.cc/rFpHwnpN/hashcracker.png)](https://github.com/mammaddrik/hashtools)
2. It is for Generator the hash:

    [![hashgenerator.png](https://i.postimg.cc/1RTd1Mhq/hashgenerator.png)](https://github.com/mammaddrik/hashtools)

## License
hashtools is licensed under [MIT License](https://github.com/mammaddrik/hashtools/blob/main/LICENSE).