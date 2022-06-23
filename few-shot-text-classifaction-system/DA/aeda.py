import json
import random
"""
通过随机增加标点符号的方式进行数据增强AEDA
"""
random.seed(0)

# 加入标点符号置换
PUNCTUATIONS = ['.', ',', '!', '?', ';', ':']
# 数据集位置
# DATASETS = ['20news', 'reuters']
DATASETS = ['20news']
# 增强数量
NUM_AUGS = [1, 2, 4, 8]
# 置换比率
PUNC_RATIO = 0.3

# Insert punction words into a given sentence with the given ratio "punc_ratio"
def insert_punctuation_marks(sentence, punc_ratio=PUNC_RATIO):
	words = sentence.split(' ')
	new_line = []
	q = random.randint(1, int(punc_ratio * len(words) + 1))
	qs = random.sample(range(0, len(words)), q)

	for j, word in enumerate(words):
		if j in qs:
			new_line.append(PUNCTUATIONS[random.randint(0, len(PUNCTUATIONS)-1)])
			new_line.append(word)
		else:
			new_line.append(word)
	new_line = ' '.join(new_line)
	# print(new_line)
	return new_line


def main(dataset):
	for aug in NUM_AUGS:
		data_aug = []
		with open("../data/"+dataset + '/' + dataset + '.json', 'r', encoding='utf-8') as train_orig:
			for line in train_orig:
				row = json.loads(line)
				# label = row['label']
				sentence = row['raw']
				line_aug = row
				if dataset == "reuters":
					train_classes = list(range(15))
				else:
					train_classes = list(range(5, 13))
				if row['label'] in train_classes:
					for i in range(aug):
						sentence_aug = insert_punctuation_marks(sentence)
						line_aug['text'] = sentence_aug.split(' ')
						line_aug['raw']  = sentence_aug
						data_aug.append(line_aug)
				data_aug.append(row)

		with open("../data/"+dataset + '/' + dataset + str(aug) + '.json', 'w', encoding="utf-8") as train_orig_plus_augs:
			# train_orig_plus_augs.writelines(data_aug)
			for t in data_aug:
				tmp = json.dumps(t)
				train_orig_plus_augs.write(tmp + '\n')

if __name__ == "__main__":
	for dataset in DATASETS:
		main(dataset)
