# -*- coding: utf-8 -*-

import src.parser.toml as tml

from keras import optimizers as opt
from keras import losses as los
from keras import initializers as ini
from keras import callbacks as cal


# Numerical parameters

BATCH_SIZE = tml.value('neuralnet', 'batch_size')

EPOCHS = tml.value('neuralnet', 'epochs')

INPUT_SHAPE = (tml.value('audio', 's_len'), 1)

KERNEL_SIZE = 500

VALIDATION_SPLIT = 0.1


# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('neuralnet', 'learning_rate'), decay=tml.value('neuralnet', 'decay'))

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.Zeros()

LOSS = los.mean_squared_error

CALLBACKS = cal.ModelCheckpoint('model.{epoch:02d}-{val_loss:.2f}.hdf5', period=tml.value('neuralnet', 'save_steps'))


# Strings parameters

FILE_NAME = tml.value('neuralnet', 'fname')

METRICS = ['accuracy']
