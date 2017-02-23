# yaql_json
Functions to extend YAQL to include `to_json()` and `from_json()`

These functions work with Stackstorm 2.1's mistral implementation.

There's a good chance it'll work under different versions of Stackstorm and may even work with
OpenStack's mistral implementation, but there's no guarantee.

## Installation - Stackstorm

 1. Checkout package from github.
 2. Enable the virtual environment.
 3. Install the module with pip.
 4. Restart the mistral daemon.
 
```
$ cd $TEMP_DIR
$ git clone git@github.com:nzlosh/yaql_json.git
$ cd yaql_json
$ source $ST2_INSTALLATION_PATH/mistral/bin/activate
$ pip install .
# SysV
$ sudo service mistral-server restart
# systemd
$ sudo systemctl restart mistral-server
```
