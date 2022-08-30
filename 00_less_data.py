from asyncio import FastChildWatcher
import pandas as pd
import argparse
import os
import sys
# parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("filename", type=str)
argparser.add_argument("--folderLoc", type=str, 
                        default="/home/fede/Dataset/goodreads/")
argparser.add_argument("--nRows", type=int, default=100)
argparser.add_argument("--only", type=int, default=100)
argparser.add_argument("--lessData", type=bool, default=True)
argparser.add_argument("--isolateText", type=bool, default=False)
argparser.add_argument("--varText", type=str, default="No var selected")
# argparser.add_argument("--type", type=str, default="csv")
args = argparser.parse_args()

# compose the complete file location
file_loc = f'{args.folderLoc}{args.filename}'

# save the file type based on filename to use the right import function 
file_base, file_ext = os.path.splitext(args.filename)

if (args.lessData == True) and (args.isolateText == False): # to avoid lessData if 
    if file_ext == ".csv":
        dataset = pd.read_csv(file_loc)
        dataset_mini = dataset.sample(n=args.nRows)
        dataset_mini.to_csv(f'{args.folderLoc}{file_base}_mini{file_ext}', index=False)
        print("Mini csv file saved")
    elif file_ext == ".pkl":
        dataset = pd.read_pickle(file_loc)
        dataset_mini = dataset.sample(n=args.nRows)
        dataset_mini.to_pickle(f'{args.folderLoc}{file_base}_mini{file_ext}')
        print("Mini pickle file saved")
    else:
        print("file type not supported")


if args.isolateText == True:
    if args.varText == "No var selected":
        print("If you want to isolate the text variable his name is needed, specify with arguments: --varText")
        sys.exit()
    if file_ext == ".csv":
        dataset = pd.read_csv(file_loc)
        dataset_remained = dataset.drop(columns=[f"{args.varText}"],axis=1)
        dataset_remained.to_csv(f'{args.folderLoc}{file_base}_remained{file_ext}', index=False)
        print("csv remained file saved")
        dataset = dataset[f"{args.varText}"]
        dataset.to_csv(f'{args.folderLoc}{file_base}_text{file_ext}', index=False)
        print("csv texts file saved")
    elif file_ext == ".pkl":
        dataset = pd.read_pickle(file_loc)
        dataset_remained = dataset.drop(columns=[f"{args.varText}"],axis=1)
        dataset_remained.to_pickle(f'{args.folderLoc}{file_base}_remained{file_ext}', index=False)
        print("Pickle remained file saved")
        dataset = dataset[f"{args.varText}"]
        dataset.to_pickle(f'{args.folderLoc}{file_base}_text{file_ext}', index=False)
        print("Pickle texts file saved")
    else:
        print("file type not supported")
