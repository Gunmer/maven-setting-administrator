# Maven settings manager
[![Build Status](https://travis-ci.org/Gunmer/maven-setting-administrator.svg?branch=master)](https://travis-ci.org/Gunmer/maven-setting-administrator)
![](https://img.shields.io/pypi/status/msa.svg)
![](https://img.shields.io/pypi/v/msa.svg)
![](https://img.shields.io/pypi/pyversions/msa.svg)
![](https://img.shields.io/pypi/l/msa.svg)

Command line tool for manage several settings file

## Getting Started

### Installing

You can install Maven Settings Manager (msa) with pip:

#### With python 2

```
    pip install msa --user
```

> You can install pip [here](https://www.makeuseof.com/tag/install-pip-for-python/)

#### With python 3

```
    pip3 install msa --user
```

### Using

The most important commands are:

- **add** To adding setting.
```
    msa add alias ~/Download/settings.xml
```
- **ls** To list settings
```
    msa ls
```
- **use** To select setting to used
```
    msa use alias
```

The others commands are:

- **version** To know the msa version
```
   msa --version 
```

- **fix** To clear and fill database with settings added in msa directory
```
    msa doctor --fix
```

#### Using like python module
```
    python -m msa -h
```
#### Using like command
Before add this to the $PATH:

**Python2**
```
    export PATH="~/Library/Python/2.7/bin:$PATH"
```
**Python3**
```
    export PATH="~/Library/Python/3.7/bin:$PATH"
```
After in you terminal, yo can use:
```
    msa -h
```
> This is available only in bash terminal

## Contributing

To contributing with this project follow the next steps:
    
1. Folk the project
1. Create a branch
1. Add changes and committed
1. Send a pull request

For other suggestions send an email to *csosaur@gmail.com*

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Gunmer/maven-setting-administrator/tags). 

## Changelog

- **1.0.0**
  - Initial version
  - Add basics command: add, ls, use
- **1.0.1**
  - Fix some issue
  - Add version command
- **1.1.0**
  - Add fix command
- **1.1.1**
  - Update pypi info

## Authors

* **Cristiam Sosa** - *Author* - [Gunmer](https://github.com/Gunmer)

See also the list of [contributors](https://github.com/Gunmer/maven-setting-administrator/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
