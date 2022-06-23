import os
import pickle
from classifier.classifier_getter import get_classifier
from train.train import train
from train.test import test

from tools.tool import parse_args, print_args, set_seed
from tools.visualization import Print_Attention

import dataset.loader as loader
from embedding.embedding import get_embedding



def main(data_path, i):


    # 训练的参数都在这里调整
    args = parse_args()
    args.cuda = 0
    # args.result_path='./result/result.pt'
    # args.save=True
    args.n_workers=1
    args.mode='train'
    args.k=5
    # args.dataset = "reuters"
    args.data_path = data_path
    # args.n_train_class = 15
    # args.n_val_class = 5
    # args.n_test_class = 11
    args.dataset = "20newsgroup"
    # args.data_path = "../data/20news/20news.json"
    args.n_train_class = 8
    args.n_val_class = 5
    args.n_test_class = 7
    print_args(args)

    set_seed(args.seed)

    # load data
    train_data, val_data, test_data, vocab = loader.load_dataset(args)

    args.id2word = vocab.itos

    # initialize model
    model = {}
    model["G"], model["D"] = get_embedding(vocab, args)
    model["clf"] = get_classifier(model["G"].ebd_dim, args)

    if args.mode == "train":
        # train model on train_data, early stopping based on val_data
        train(train_data, val_data, model, args)

    # val_acc, val_std, _ = test(val_data, model, args,
    #                                         args.val_episodes)

    test_acc, test_std, drawn_data = test(test_data, model, args,
                                          args.test_episodes, i)

    # path_drawn = args.path_drawn_data
    # with open(path_drawn, 'w') as f_w:
    #     pickle.dump(drawn_data, f_w)
    #     print("store drawn data finished.")
    #
    # file_path = r'../data/attention_data.json'
    # Print_Attention(file_path, vocab, model, args)
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write("{},{},{}\n".format(test_acc,test_std,args.data_path ))
    if args.result_path:
        directory = args.result_path[:args.result_path.rfind("/")]
        if not os.path.exists(directory):
            os.mkdir(directory)
        result = {
            "test_acc": test_acc,
            "test_std": test_std,
            # "val_acc": val_acc,
            # "val_std": val_std
        }

        for attr, value in sorted(args.__dict__.items()):
            result[attr] = value
        with open(args.result_path, "wb") as f:
            pickle.dump(result, f, -1)



if __name__ == '__main__':
    dataset = "../data/20news/20news{}.json"
    NUM_AUGS = [1, 2, 4, 8]
    for i  in NUM_AUGS:
        main(dataset.format(i), i)