import tensorflow as tf
from tensorflow.contrib.saved_model.python.saved_model import signature_def_utils
from tensorflow import saved_model as sm
import logging
from config import DEFAULT_MODEL_PATH

logger = logging.getLogger()


class ModelWrapper(object):
    """Model wrapper for TensorFlow models in SavedModel format"""
    def __init__(self, path=DEFAULT_MODEL_PATH):
        logger.info('Loading model from: {}...'.format(path))
        sess = tf.Session(graph=tf.Graph())
        # Load the graph
        model_graph_def = sm.loader.load(sess, [sm.tag_constants.SERVING], path)
        sig_def = signature_def_utils.get_signature_def_by_key(model_graph_def, sm.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY)
        input_name = sig_def.inputs['input'].name
        output_name = sig_def.outputs['output'].name

        # Set up instance variables and required inputs for inference
        self.sess = sess
        self.model_graph_def = model_graph_def
        self.output_tensor = sess.graph.get_tensor_by_name(output_name)
        self.input_name = input_name
        logger.info('Loaded model')

    def predict(self, x):

        # Run prediction on input
        preds = self.sess.run(self.output_tensor, {self.input_name: x})
        return preds
