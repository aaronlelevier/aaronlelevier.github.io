# tf.Transform notes

## tensorflow-serving

example command to examine a saved model

```
saved_model_cli show --dir /tmp/data/mnist/tmpymWiby/exported_model_dir/1557495106/ --all
```

The above call will produce output in this structure.

This means that the expected input structure is: `{inputs: {images: <size (1, 784) np.ndarray>}}`

```

MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['predict_images']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['images'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 784)
        name: x:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['scores'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: y:0
  Method name is: tensorflow/serving/predict

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_STRING
        shape: unknown_rank
        name: tf_example:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['classes'] tensor_info:
        dtype: DT_STRING
        shape: (-1, 10)
        name: index_to_string_Lookup:0
    outputs['scores'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: TopKV2:0
  Method name is: tensorflow/serving/classify
```


MNIST example to run

```
(venv) aaron@ ~/Documents/github/serving (master) $ tools/run_in_docker.sh python tensorflow_serving/example/mnist_client.py --num_tests=100 --server=127.0.0.1:8500
```

### My `feature_config`

I think it needs to change to this:

```
serialized_tf_example = tf.placeholder(tf.string, name='tf_example')
feature_configs = {'x': tf.FixedLenFeature(shape=[784], dtype=tf.float32),}
tf_example = tf.parse_example(serialized_tf_example, feature_configs)
x = tf.identity(tf_example['x'], name='x')  # use tf.identity() to assign name
```

## docker

What does this command do?

```
TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"

docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" \
    -e MODEL_NAME=half_plus_two \
    tensorflow/serving &
```

It's serving a model by binding the local volume to a Docker volume

```
docer run --help

# -v, --volume list                    Bind mount a volume
```

### container commands

list containers

```
docker container ls
```

ssh into container

```
docker exec -it <container_id> /bin/bash
```

stop a container

```
docker container stop <container_id>
```

## Current Try

One exported model exists. Output using:

```
saved_model_cli show --dir /tmp/data/mnist/tmpbjd0WU/exported_model_dir/1557712429/ --all 
```

Returns:

```

MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['classification']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_STRING
        shape: (-1)
        name: input_example_tensor:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['classes'] tensor_info:
        dtype: DT_STRING
        shape: (-1, 10)
        name: dnn/head/Tile:0
    outputs['scores'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: dnn/head/predictions/probabilities:0
  Method name is: tensorflow/serving/classify

signature_def['predict']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['examples'] tensor_info:
        dtype: DT_STRING
        shape: (-1)
        name: input_example_tensor:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['class_ids'] tensor_info:
        dtype: DT_INT64
        shape: (-1, 1)
        name: dnn/head/predictions/ExpandDims:0
    outputs['classes'] tensor_info:
        dtype: DT_STRING
        shape: (-1, 1)
        name: dnn/head/predictions/str_classes:0
    outputs['logits'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: dnn/logits/BiasAdd:0
    outputs['probabilities'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: dnn/head/predictions/probabilities:0
  Method name is: tensorflow/serving/predict

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['inputs'] tensor_info:
        dtype: DT_STRING
        shape: (-1)
        name: input_example_tensor:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['classes'] tensor_info:
        dtype: DT_STRING
        shape: (-1, 10)
        name: dnn/head/Tile:0
    outputs['scores'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: dnn/head/predictions/probabilities:0
  Method name is: tensorflow/serving/classify
```

### MNIST LinearClassifier example

From [here](https://www.tensorflow.org/tutorials/representation/kernel_methods)

```python
import time

# Specify the feature(s) to be used by the estimator.
image_column = tf.contrib.layers.real_valued_column('images', dimension=784)
estimator = tf.contrib.learn.LinearClassifier(feature_columns=[image_column], n_classes=10)

# Train.
start = time.time()
estimator.fit(input_fn=train_input_fn, steps=2000)
end = time.time()
print('Elapsed time: {} seconds'.format(end - start))

# Evaluate and report metrics.
eval_metrics = estimator.evaluate(input_fn=eval_input_fn, steps=1)
print(eval_metrics)
```

### Commands to start and communicate with `tf.serving`

```
TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"

docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" \
    -e MODEL_NAME=half_plus_two \
    tensorflow/serving &


docker run -t --rm -p 8501:8501 \
    -v "/tmp/data/mnist/tmpPivLUi/exported_model_dir:/models/mnist" \
    -e MODEL_NAME=mnist \
    tensorflow/serving &


tools/run_in_docker.sh python tensorflow_serving/example/mnist_client.py \
  --num_tests=1000 --server=127.0.0.1:8501
```

## References

[TF Dev Summit 2018 tf.Transform Talk](https://www.youtube.com/watch?v=vdG7uKQ2eKk&t=)

[MNIST fully_connected_reader.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/how_tos/reading_data/fully_connected_reader.py)

[Medium blog](https://codeburst.io/use-tensorflow-dnnclassifier-estimator-to-classify-mnist-dataset-a7222bf9f940) for `DNNClassifier` that I've been trying to use for MNIST. Has an input shape of (28, 28)

[tf.Tensor](https://www.tensorflow.org/api_docs/python/tf/Tensor) docs

[tf.Serving Docker](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/g3doc/docker.md)

[tf.Serving Medium blog](https://medium.com/@tmlabonte/serving-image-based-deep-learning-models-with-tensorflow-servings-restful-api-d365c16a7dc4)

[tf.Serving REST API docs](https://www.tensorflow.org/tfx/serving/api_rest#top_of_page)

[TFX Serving REST API MNIST example in the docs](https://www.tensorflow.org/tfx/tutorials/serving/rest_simple)

[tf.Serving](https://www.tensorflow.org/tfx/serving/serving_basic) basic example

# NEXT

### Save and Restore a TF Model

[TF Docs](https://www.tensorflow.org/guide/saved_model#build_and_load_a_savedmodel)

I'm thinking this is my next step. I need to learn how to do this. Save a Model, then load it and call the Model inference in the same way before it was saved to make sure I know how to **Save** and **Restore** a Model.

### tf.Serving

Then, bind the `dir` the model is in to a `volume` in the `tf.serving` docker container and call the endpoint, maybe using `grpc`. Some references to go off would be:

- `tensorflow_serving.example.mnist_client`
- `tensorflow_serving.example.mnist_saved_model`

### TFX Transform Docs

[here](https://www.tensorflow.org/tfx/guide/transform) maybe I need to read these first