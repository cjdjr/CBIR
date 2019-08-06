import sys
sys.path.insert(0, '.')
import numpy as np
import pickle


def load_features(dataset_name):
    if dataset_name == 'Holiday':
        with open('../datasets/Holiday/features.pk','rb') as pk_file:
            features_obj = pickle.load(pk_file,encoding='bytes')
        with open('../datasets/Holiday/gt.pk','rb') as pk_file:
            gt_obj = pickle.load(pk_file,encoding='bytes')
        return features_obj, gt_obj
    else:
        print('do not support the {} dataset'.format(dataset_name))
        assert False


if __name__ == '__main__':
    features_obj, gt_obj = load_features('Holiday')
    #print(features_obj)
    print(features_obj.keys(), gt_obj.keys())
    print(np.shape(features_obj.values()))