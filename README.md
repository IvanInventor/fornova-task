# fornova-task
## Usage
```
usage: ./main.py [-h] [-i INPUT] [-o OUTPUT]

Fornova task

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file (stdin by default)
  -o OUTPUT, --output OUTPUT
                        Output file (stdout by default)
```
## Example
```bash
./main.py -i Python-task.json -o out.txt
```
### Result
```
For hotel "Home2 Suites By Hilton San Francisco Airport North":
	Cheapest price: 90.00

	Cheapest room:
		Type: King Studio Suite - Non Smoking
		Price: 90.00
		Number of guests: 4

	Total price for all rooms (net + taxes):
		"King Studio Suite - Hearing Accessible/Non-Smoking" : 131.76
		"King Studio Suite - Non Smoking" : 108.71
		"King Room - Mobility/Hearing Accessible - Non-Smoking" : 133.76
		"Queen Suite with Two Queen Beds - Non-Smoking" : 130.76
```
