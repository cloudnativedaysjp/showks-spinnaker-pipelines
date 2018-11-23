import sys
import json
import argparse

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("id", help="id", type=str)
    parser.add_argument("stage", help="stg or prod", type=str)
    parser.add_argument("template", help="template file path", type=str)
    parser.add_argument("outfile", help="output json file path", type=str)

    args = parser.parse_args()

    return(args)

def main():
    args = get_args()

    with open(args.template) as f:
        df = json.load(f)

    APPNAME = 'showks-canvas-' + args.id
    STAGE = args.stage
    DEPNAME = APPNAME + '-' + STAGE

    df['application'] = APPNAME
    df['name'] = 'deploy-to-' + STAGE
    df['expectedArtifacts'][0]['defaultArtifact']['id'] = DEPNAME + '-defaultArtifact'
    df['expectedArtifacts'][0]['id'] = DEPNAME + '-manifest'
    df['expectedArtifacts'][0]['matchArtifact']['id'] = DEPNAME + '-manifest-github'
    df['expectedArtifacts'][0]['matchArtifact']['name'] = 'manifests/' + APPNAME + '/manifest.yaml'
    df['id'] = DEPNAME + '-pipeline'
    df['stages'][0]['account'] = 'showks-cluster-' + STAGE + '-account'
    df['stages'][0]['manifestArtifactId'] = DEPNAME + '-manifest'
    df['stages'][0]['moniker']['app'] = APPNAME
    df['triggers'][0]['expectedArtifactIds'][0] = DEPNAME + '-manifest'
    df['triggers'][0]['slug'] = 'showks-manifests-' + STAGE #GitHub Repo Name

    with open(args.outfile, 'w') as of:
        json.dump(df, of, indent=2)

if __name__ == '__main__':
    main()
