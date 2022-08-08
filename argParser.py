from datetime import datetime
from datetime import date
import argparse

def validDate(s):
    try:
        return datetime.strptime(s, "%d-%m-%Y")
    except ValueError:
        msg = "ERROR, not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser()

# Add argument for name
parser.add_argument('-n',
                    '--name',
                    required=True,
                    help='input your name'
)

# Add argument for date of birth
parser.add_argument('-d',
                    '--dob',
                    required=True,
                    type=validDate,
                    help='input your date of birth (DD-MM-YYYY)'
)

# Parse the argument
args = parser.parse_args()

# Get each date, month, and year from the argument
d = args.dob.date
m = args.dob.month
y = args.dob.year

# Get today date, month, and year
today = date.today()

# Calculate the age with today date - date of birth
age = today.year - y - ((today.month, today.day) < (m, d))

# If the age is less than 30, print with "kakak", else print with "bapak"
if (age < 30):
    print(f"Terima kasih telah menggunakan argParser.py pada tahun {str(today.year)}, kakak {args.name}")
else:
    print(f"Terima kasih telah menggunakan argParser.py pada tahun {str(today.year)}, bapak {args.name}")
