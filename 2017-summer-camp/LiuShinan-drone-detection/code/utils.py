import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, precision_score, recall_score, confusion_matrix

##################################
# weight and bias initialization #
##################################
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)
    
def bias_variable(shape):
    initial = tf.constant(0.1, shape = shape)
    return tf.Variable(initial)

###########################
# convolution and pooling #
###########################
def conv2d(x, W, strides = [1, 1, 1, 1], padding = 'VALID'):
    return tf.nn.conv2d(x, W, strides = strides, padding = padding)

def max_pooling_2x2(x, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'VALID'):
    return tf.nn.max_pool(x, ksize = ksize, 
                          strides = strides, padding = padding)

#################
# loss function #
#################
def RMSE(reconstructed_x, x):
    return tf.reduce_mean(tf.square(x - reconstructed_x))

class Data(object):
    pass

def get_data(train, test):
    """build Data object which include train set and test set
    Args:
        train: DataSet, train set
        test: DataSet, test set
    """
    data = Data()
    data.train = train
    data.test = test
    return data
    

class DataSet(object):
  """create same API with input_data.DataSet, but not change the data format
  """
  def __init__(self, images, labels):
    self._num_examples = images.shape[0]
    self._images = images
    self._labels = labels
    self._epochs_completed = 0
    self._index_in_epoch = 0
    # Shuffle the data
    perm = np.arange(self._num_examples)
    np.random.shuffle(perm)
    self._images = self._images[perm]
    self._labels = self._labels[perm]        
  @property
  def images(self):
    return self._images
  @property
  def labels(self):
    return self._labels
  @property
  def num_examples(self):
    return self._num_examples
  @property
  def epochs_completed(self):
    return self._epochs_completed
  def next_batch(self, batch_size):
    start = self._index_in_epoch
    self._index_in_epoch += batch_size
    if self._index_in_epoch > self._num_examples:
        # Finished epoch
        self._epochs_completed += 1
        # Shuffle the data
        perm = np.arange(self._num_examples)
        np.random.shuffle(perm)
        self._images = self._images[perm]
        self._labels = self._labels[perm]
        # Start next epoch
        start = 0
        self._index_in_epoch = batch_size
        assert batch_size <= self._num_examples
    end = self._index_in_epoch
    return self._images[start:end], self._labels[start:end]

########################
# fill feed dictionary #
########################
def fill_feed_dict(data_set, images_pl, labels_pl, batch_size):
  """Fills the feed_dict for training the given step.
  A feed_dict takes the form of:
  feed_dict = {
      <placeholder>: <tensor of values to be passed for placeholder>,
      ....
  }
  Args:
    data_set: The set of images and labels, from input_data.read_data_sets()
    images_pl: The images placeholder, from placeholder_inputs().
    labels_pl: The labels placeholder, from placeholder_inputs().
  Returns:
    feed_dict: The feed dictionary mapping from placeholders to values.
  """
  # Create the feed_dict for the placeholders filled with the next
  # `batch size` examples.
  images_feed, labels_feed = data_set.next_batch(batch_size)
  feed_dict = {
      images_pl: images_feed,
      labels_pl: labels_feed,
  }
  return feed_dict

################################
# get evaluation metrics value #
################################
def do_eval(y_score, y_true):
    """Runs one evaluation against the full epoch of data.
    Args:
        sess: The session in which the model has been trained.
        y_score: numpy array, float - [batch_size, n_classes]
        y_true: numpy array, float - [batch_size, n_classes]
    Returns:
        (AUC, accuray, precision, recall, f1)
    """
    auc = roc_auc_score(y_true, y_score)
    y_pred = np.argmax(y_score, axis=1)
    y_true = np.argmax(y_true, axis=1)
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return (auc, accuracy, precision, recall, f1)


##################################
# confusion matrix plot function #
##################################
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(list(range(cm.shape[0])), list(range(cm.shape[1]))):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    
def scale_to_unit_interval(ndar, eps=1e-8):
    """Scales all values in the values int the ndarray ndar to be between 0 and 1"""
    ndar = ndar.copy()
    ndar -= ndar.min()
    ndar *= 1.0 / (ndar.max() + eps)
    
    return ndar


def tile_raster_images(X, img_shape, tile_shape, tile_spacing=(0, 0), 
                       scale_imgs_to_unit_interval=True,
                       output_pixel_vals=True):
    """
    Transform an array with one image into an array in which images are layed out like tiles on a floor.
    """
    
    assert len(img_shape) == 2
    assert len(tile_shape) == 2
    assert len(tile_spacing) == 2
    
    out_shape = [
        (ishp + tsp) * tshp - tsp
        for ishp, tshp, tsp in zip(img_shape, tile_shape, tile_spacing)
    ]
    
    H, W = img_shape
    Hs, Ws = tile_spacing
    
    # generate a matrix to store the output
    dt = X.dtype
    if output_pixel_vals:
        dt = 'uint8'
    out_array = np.zeros(out_shape, dtype=dt)
    
    for tile_row in range(tile_shape[0]):
        for tile_col in range(tile_shape[1]):
            if tile_row * tile_shape[1] + tile_col < X.shape[3]:
                this_x = X[:, :, 0, tile_row * tile_shape[1] + tile_col]
                if scale_imgs_to_unit_interval:
                    this_img = scale_to_unit_interval(this_x)
                else:
                    this_img = this_x
                
                # add the slice to the corresponding position in the output array
                c = 1
                if output_pixel_vals:
                    c = 255
                out_array[
                    tile_row * (H + Hs) : tile_row * (H + Hs) + H,
                    tile_col * (W + Ws) : tile_col * (W + Ws) + W
                ] = this_img * c
                
    return out_array    
