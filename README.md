# pearce

PEARCE stands for "Python Example and Random CLI Explanation" and was created as a personal project to help my nephews and nieces with their software engineering interests.

## Environment Setup

Use the following to prepare your local environment.

1. Ensure you have the latest `pip` installed.  
   ```
   python3 -m pip install --upgrade pip
   ```
1. Install `virtualenv` to avoid installing anything globally that may disrupt your other applications.  
   ```
   python3 -m pip install --user virtualenv
   python3 -m venv  ./venv 
   source ./venv/bin/activate
   ```
1. Run `pip` with the requirements file to locally install necessary modules.  
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Usage

To use the python script, invoke it as shown in the example below. Use the `--help` option for additional options. 

```
$ ./pearce.py -i 2
[12/Jun/2021:09:44:44 -0400] [DEBUG] Starting main().
[12/Jun/2021:09:44:44 -0400] [DEBUG] Iteration 0 with random value 65
[12/Jun/2021:09:44:45 -0400] [DEBUG] Iteration 1 with random value 21
[12/Jun/2021:09:44:46 -0400] [DEBUG] Exiting main().
```

## Contributions

Basic unit tests required. Currently linting is only done with `flake8`.
```
flake8 pearce.py
```


## Reference

 * https://choosealicense.com/licenses/
 * https://www.viget.com/articles/two-ways-to-share-git-hooks-with-your-team/
 * https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/signing-commits
 * http://docopt.org/

