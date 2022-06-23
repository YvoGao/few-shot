import collections
import json
import pdb
import numpy as np
import torch
# 均值为0， 标准差为1
from torchtext.vocab import Vocab, Vectors

from dataset import utils
from dataset.loader import _data_to_nparray, _read_words
from tools.tool import parse_args

def load_data(file_path):
    label = {}
    with open(file_path, 'r', errors='ignore') as f:
        data = []
        for line in f:
            row = json.loads(line)
            item = {
                'label': int(row['label']),
                'text': row['text'][:500],
                'raw': row['raw']
            }


            keys = ['head', 'tail', 'ebd_id']
            for k in keys:
                if k in row:
                    item[k] = row[k]

            data.append(item)

    return data


# 在进行词向量编码后进行特征间增强
def Random_Perturb(dataset, aug, args):

    XS = dataset

    XS_tmp = XS
    D_f = dataset.size()
    for i  in range(aug):
        tmp = torch.tensor(np.random.normal(loc=0.0, scale=1.0, size=D_f)).cuda(args.cuda)
        new_i = tmp*0.5 + XS
        XS_tmp = torch.cat((XS_tmp, new_i))


    dataset = XS_tmp

# 在进行词向量编码后进行特征间增强
def Random_Perturb1(dataset, aug, args):

    XS = dataset

    XS_tmp = XS
    D_f = dataset.size()
    for i  in range(aug):
        tmp = torch.tensor(np.random.normal(loc=0.0, scale=1.0, size=D_f)).cuda(args.cuda)
        new_i = tmp*0.5 + XS
        XS_tmp = torch.cat((XS_tmp, new_i))


    dataset = XS_tmp




# 外插法数据增强
# def



if __name__ == '__main__':
    dataname = 'reuters'
    classes = [22,24,25,26,28]
    args = parse_args()

    tmpdata = load_data('../data/reuters/reuters.json')
    support_data = []
    for td in tmpdata:
        if td["label"] in classes:
            support_data.append(td)

    all_data = load_data("../data/" + dataname + "/" + dataname + ".json")
    vectors = Vectors("../pretrain_wordvec/wiki.en.vec", cache="../pretrain_wordvec")
    vocab = Vocab(collections.Counter(_read_words(all_data)), vectors=vectors,
                  specials=['<pad>', '<unk>'], min_freq=5)

    support = _data_to_nparray(support_data, vocab, args)
    support = utils.to_tensor(support, args.cuda, ['raw', 'vocab_size'])
    pdb.set_trace()

    print(support['text'].size())
    Random_Perturb(support,3)
    print(support['text'].size())