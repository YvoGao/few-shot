import os
import pickle
from classifier.classifier_getter import get_classifier
from train.train import train
from train.test import test

from tools.tool import parse_args, print_args, set_seed
from tools.visualization import Print_Attention

import dataset.loader as loader
from embedding.embedding import get_embedding



def main():

    # make_print_to_file(path='/results')

    # 训练的参数都在这里调整
    args = parse_args()
    args.cuda = 0
    # args.result_path='./result/20new.pt'
    # args.save=True
    args.n_workers=1
    args.mode='test'
    args.lr_scheduler = 'ExponentialLR'
    args.k = 5
    args.shot = 1
    args.dataset = "cnews"
    args.data_path = "../data/cnews/cnews.json"
    args.n_train_class = 3
    args.n_val_class = 3
    args.n_test_class = 4
    args.train_mode = "t_add_v"
    args.wv_path = "../data/cnews/pretrain_word"
    args.word_vector = "../data/cnews/pretrain_word/sgns.sogou.word"
    args.way = 3
    args.save=True
    # args.dataset = "huffpost"
    # args.data_path = "../data/huffpost.json"
    # args.n_train_class = 20
    # args.n_val_class = 5
    # args.n_test_class = 16
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
                                          args.test_episodes, 1)
    with open('cnews_result.txt', 'a', encoding='utf-8') as f:
        f.write("{},{},{}\n".format(test_acc,test_std,args.data_path ))
    # path_drawn = args.path_drawn_data
    # with open(path_drawn, 'w') as f_w:
    #     pickle.dump(drawn_data, f_w)
    #     print("store drawn data finished.")
    #
    # file_path = r'../data/attention_data.json'
    # Print_Attention(file_path, vocab, model, args)

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
    main()