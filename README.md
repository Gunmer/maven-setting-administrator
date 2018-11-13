# Maven settings manager

Command line tool for manage several settings file

## Getting Started

### Installing
#### With python 2
You can install Maven Settings Manager (msa) with pip:
```
    pip install msa --user
```

> You can install pip [here](https://www.makeuseof.com/tag/install-pip-for-python/)

#### With python 3
You can install Maven Settings Manager (msa) with pip:
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

Coming soon...

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Cristiam Sosa** - *Author* - [Gunmer](https://github.com/Gunmer)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
