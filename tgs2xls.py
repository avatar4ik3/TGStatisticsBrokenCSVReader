import datetime
import sys
import pandas as pd
import argparse

argParser = argparse.ArgumentParser(description="Program that reads telegram statistic .cvs file and parces it to .xlsx file")
argParser.add_argument("-i", "--input", help="input .csv file form tg stats service")
argParser.add_argument("-o", "--output", help="name of excel file, without extensions, wich will be created",default="output")
argParser.add_argument('--parce', action=argparse.BooleanOptionalAction,help="option to parce date from csv")

args = argParser.parse_args()

frame = pd.read_csv(args.input,
                    delimiter='\t',
                    )
if args.parce:
    print("parcfe!")
    frame['date'] = pd.to_datetime(frame['date'], format='%d %b %Y  %H:%M %Z').dt.tz_localize(None)    

frame.to_excel(args.output + ".xlsx")