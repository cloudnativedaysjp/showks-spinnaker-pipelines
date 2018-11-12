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

    APPNAME = 'showks-canvas' + args.id

    df['application'] = APPNAME
    df['expectedArtifacts'][0]['defaultArtifact']['id'] = APPNAME + '-defaultArtifact'
    df['expectedArtifacts'][0]['id'] = APPNAME + '-manifest'
    df['expectedArtifacts'][0]['matchArtifact']['id'] = APPNAME + '-manifest-github'
    df['id'] = APPNAME + '-pipeline'
    df['stages'][0]['manifestArtifactId'] = APPNAME + '-manifest'
    df['triggers'][0]['expectedArtifactIds'][0] = APPNAME + '-manifest'
    df['triggers'][0]['slug'] = APPNAME  #GitHub Repo Name

    with open(args.outfile, 'w') as of:
        json.dump(df, of, indent=2)

if __name__ == '__main__':
    main()
