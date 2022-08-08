# Python Argument Parser

This is an assignment practice for the Getting Started Programming with Python ([Memulai Pemrograman dengan Python](https://www.dicoding.com/academies/86 "Memulai Pemrograman dengan Python - Dicoding")) class, Popular Libraries in Python ([Library Populer pada Python](https://www.dicoding.com/academies/86/tutorials/5082 "Library Populer pada Python - Memulai Pemrograman dengan Python")) module, on the [Machine Learning Developer Learning Path](https://www.dicoding.com/learningpaths/30 "Machine Learning Developer Learning Path at Dicoding Indonesia") at [Dicoding Indonesia](https://www.dicoding.com "Dicoding Indonesia").

## Script Description

The argument parser is useful when creating small program or script that can be directly receive parameter(s) when the program is run. Application program or script can be run via the CLI (Command-Line Interface) or Terminal or CMD (Command Prompt).

When the program is run, it will aks for parameter `name` and `date of birth`. If the program is run without the parameters or only one parameter, then the program will return an error. The date of birth parameter format is `DD-MM-YYYY`. If the format of the date of birth parameter is incorrect, then the program will hanlde an exception (`ValueError`) which is checked in the `validDate` function.

The program will calculate the age that obtained from the date of birth parameter, so if the age is less than 30 years, then the output will display "kakak", otherwise the output will display "bapak."

You can try this program by:

> 1. Make sure Python is installed on your local machine (`python --version`)  
>    If Python has not been installed, you can download it via this [link](https://www.python.org/downloads "Python Download")
> 2. Save or Download the Python file on local as `argParser.py` via this [**`link`**](https://github.com/aNdr3W03/Python-Argument-Parser/raw/main/argParser.py "argParser.py")
> 3. Run the file on `CLI` or `Terminal` or `CMD`
> 4. See the output example below if you need help

## Output Example

```powershell
argParser.py -h
```
```powershell
usage: argParser.py [-h] -n NAME -d DOB

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  input your name
  -d DOB, --dob DOB     input your date of birth (DD-MM-YYYY)
```

#

```console
argParser.py -n INPUTNAME -d INPUTDOB
```
```console
INPUTNAME : input your name
INPUTDOB  : input your date of birth (format: DD-MM-YYYY)
```

#

```powershell
argParser.py -n Andrew -d 20-01-2003
```
```powershell
Terima kasih telah menggunakan argParser.py pada tahun 2022, kakak Andrew
```

#

```powershell
argParser.py -n Andrew -d 20-01-1990
```
```powershell
Terima kasih telah menggunakan argParser.py pada tahun 2022, bapak Andrew
```

#

```powershell
argParser.py -n Andrew -d 2003-01-20
```
```powershell
usage: argParser.py [-h] -n NAME -d DOB
argParser.py: error: argument -d/--dob: ERROR, not a valid date: '2003-01-20'
```

#

```powershell
argParser.py -n Andrew
```
```powershell
usage: argParser.py [-h] -n NAME -d DOB
argParser.py: error: the following arguments are required: -d/--dob
```

#

```powershell
argParser.py -d 2003-01-20
```
```powershell
usage: argParser.py [-h] -n NAME -d DOB
argParser.py: error: the following arguments are required: -n/--name
```

#

```powershell
argParser.py
```
```powershell
usage: argParser.py [-h] -n NAME -d DOB
argParser.py: error: the following arguments are required: -n/--name, -d/--dob
```

## References

[(Stack Overflow) Specify date format for Python argparse input arguments](https://stackoverflow.com/questions/25470844/specify-date-format-for-python-argparse-input-arguments)

[(Stack Overflow) Python : extract parameters created with argparse](https://stackoverflow.com/questions/49311085/python-extract-parameters-created-with-argparse)

[(Stack Overflow) Age from birthdate in python](https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python)

[(Stack Overflow) TypeError:'datetime.datetime' object is not subscriptable](https://stackoverflow.com/questions/11177293/typeerrordatetime-datetime-object-is-not-subscriptable)

[(Programiz) Python strptime()](https://www.programiz.com/python-programming/datetime/strptime)

[(Dicoding) Penanganan Pengecualian](https://www.dicoding.com/academies/86/tutorials/6421)

[(Dicoding) Library Populer pada Python](https://www.dicoding.com/academies/86/tutorials/5082)
