#!/usr/bin/python3

import json
import sys
import argparse

def find_min_price(rooms):
    if len(rooms) == 0:
        return None, None

    min_name, min_price = next(iter(rooms.items()))
    min_price = float(min_price)
    for name, price in rooms.items():
        price = float(price)
        if price < min_price:
            min_name, min_price = name, price

    return min_name, min_price

def process(data, out):
    for hotel in data['assignment_results']:
        print(f'For hotel "{hotel["hotel_name"]}":', file=out)

        if len(hotel['shown_price']) == 0:
            print(f'\tNo rooms!\nNumber of guests: {hotel["number_of_guests"]}', file=out)
            continue

        min_name, min_price = find_min_price(hotel['shown_price'])

        # Task a
        print(f'\tCheapest price: {min_price}', file=out)
        print(file=out)

        # Task b
        print('\tCheapest room:', file=out)
        print(f'\t\tType: {min_name}', file=out)
        print(f'\t\tPrice: {min_price}', file=out)
        print(f'\t\tNumber of guests: {hotel["number_of_guests"]}', file=out)
        print(file=out)

        # Task c
        taxes_total = sum(float(price) for _, price in json.loads(hotel['ext_data']['taxes']).items())

        print("\tPrices for all rooms:", file=out)
        for room_name, room_price in hotel['net_price'].items():
            room_price = float(room_price) + taxes_total
            print(f'\t\t"{room_name}" : {room_price}', file=out)
        
        print(file=out)
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Fornova task")
    parser.add_argument('-i', '--input', type=str, default=None, help="Input file (stdin by default)")
    parser.add_argument('-o', '--output', type=str, default=None, help="Output file (stdout by default)")
    options = parser.parse_args(sys.argv[1:])

    if options.input:
        with open(options.input, 'r') as file:
            data = json.load(file)
    else:
        data = json.load(sys.stdin)

    if options.output:
        with open(options.output, 'w') as out:
            process(data, out)
    else:
        process(data, sys.stdout)
