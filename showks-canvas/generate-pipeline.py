import sys
import json
import argparse

def get_args():
    parser = argparse.ArgumentParser()
  
    parser.add_argument("id", help="id", type=str)
    parser.add_argument("template", help="template file path", type=str)
    parser.add_argument("outfile", help="output json file path", type=str)

    args = parser.parse_args()

    return(args)

def main():
    args = get_args()

    with open(args.template) as f:
        df = json.load(f)

    df['expectedArtifacts'][0]['matchArtifact']['id'] = 'showks-canvas-' + args.id + '-manifest-github'
    # 以下同様に並べていく

    with open(args.outfile, 'w') as of:
        json.dump(df, of, indent=4)

if __name__ == '__main__':
    main()

