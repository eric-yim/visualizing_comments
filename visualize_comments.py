import argparse
from util.tt_util import find_all_tt_comments
from util.embed_util import Embedder
from util.plot_util import create_bokeh_html
from util.text_util import wrap_labels
import os, json, glob
import numpy as np
def argparse_args():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('--fpath', required=True, help='local html text file')
    parser.add_argument('--comment_data', default="comment_data", help='json')
    parser.add_argument('--out_file', default="tsne_plot.html", help='output')

    

    # Parse the command-line arguments
    return parser.parse_args()
def embed_comments(args, comment_data):
    """
    input: list of {'comment_text','likes'}
    """
    embedder = Embedder()
    os.makedirs(args.comment_data, exist_ok=True)
    for i, comment in enumerate(comment_data):
        name = os.path.join(args.comment_data, str(i).zfill(5) + '.json')
        if os.path.exists(name):
            print(f"Found {name}. Skipping")
            continue
        if not "comment_text" in comment:
            continue
        try:
            embedding = embedder.embed(comment['comment_text'])
        except Exception as e:
            print(f"Couldnt embed {comment['comment_text']}, {e}")
            embedding = None
        if embedding:
            comment['embedding'] = embedding
            name = os.path.join(args.comment_data, str(i).zfill(5) + '.json')
            json.dump(comment, open(name, 'w'), indent=2)
            print(f"Wrote to {name}")
    
def create_plot(args):
    globber = os.path.join(args.comment_data, '*.json')
    listing = sorted(glob.glob(globber))
    vectors = []
    labels = []
    for item in listing:
        tmp_dict = json.load(open(item, 'r'))
        if 'embedding' in tmp_dict and 'comment_text' in tmp_dict:
            vectors.append(tmp_dict['embedding'])
            labels.append(tmp_dict['comment_text'])
    labels = wrap_labels(labels)
    vectors = np.array(vectors)
    print(f"Num Points: {len(vectors)}")
    create_bokeh_html(vectors, labels, args.out_file)


def read_item(fpath):
    with open(fpath, 'r') as f:
        return f.read()
def main(args):
    html_code = read_item(args.fpath)
    comment_data = find_all_tt_comments(html_code)
    print(f"Num comments: {len(comment_data)}")
    embed_comments(args, comment_data)
    #print(f"Total Likes: {sum([item['likes'] for item in comment_data])}")
    
    create_plot(args)
    
if __name__ == '__main__':
    args = argparse_args()
    main(args)