# Neural Style Transfer: Creating Art with Deep Learning using tf.keras and Eager Execution

Welcome to the Neural Style Transfer project! This project leverages deep learning techniques to combine the style of one image with the content of another to create a unique piece of art. The implementation is based on the principles laid out by deeplearning.ai, utilizing `tf.keras` and eager execution in TensorFlow.

## What is Neural Style Transfer?

Neural Style Transfer (NST) is a deep learning technique that merges two images: a content image (e.g., a photograph) and a style image (e.g., a painting by a famous artist). The goal is to create a new image that maintains the content of the content image but adopts the artistic style of the style image.

## What are Deep Convolutional Networks Learning?

Deep Convolutional Networks (CNNs) learn to extract features from images at multiple levels of abstraction. Lower layers capture simple features like edges and textures, while higher layers capture more complex features like shapes and objects. In the context of NST, we use these hierarchical features to separate and recombine the content and style of images.

## Cost Function

The NST algorithm optimizes an image to minimize a cost function that combines two parts: the content cost and the style cost. The total cost \( J \) is given by:

\[ J = \alpha J_{content} + \beta J_{style} \]

Where:
- \( J_{content} \) is the content cost
- \( J_{style} \) is the style cost
- \( \alpha \) and \( \beta \) are weighting parameters to balance the two costs

### Content Cost Function

The content cost function measures how much the generated image differs from the content image. It is based on the differences in the feature representations between the two images at a specific layer in the network. Mathematically, it is defined as:

\[ J_{content}(\mathbf{C}, \mathbf{G}, l) = \frac{1}{2} \sum_{i,j} (A^{(l)}_{ij} - A^{(l, G)}_{ij})^2 \]

Where:
- \( A^{(l)} \) is the feature map of the content image at layer \( l \)
- \( A^{(l, G)} \) is the feature map of the generated image at layer \( l \)

### Style Cost Function

The style cost function measures how much the style of the generated image differs from the style image. It uses the Gram matrix, which captures the correlations between different filter responses in a layer. The style cost is calculated as:

\[ J_{style}(\mathbf{S}, \mathbf{G}) = \sum_{l} w_l \frac{1}{4N_l^2M_l^2} \sum_{i,j} (G^{(l)}_{ij} - A^{(l, G)}_{ij})^2 \]

Where:
- \( G^{(l)} \) is the Gram matrix of the style image at layer \( l \)
- \( G^{(l, G)} \) is the Gram matrix of the generated image at layer \( l \)
- \( w_l \) is the weight assigned to the style cost at layer \( l \)
- \( N_l \) and \( M_l \) are the dimensions of the feature map at layer \( l \)

## Eager Execution

Eager execution is an imperative, define-by-run programming environment that evaluates operations immediately. This makes it easier to debug and experiment with the model. TensorFlow's eager execution provides an intuitive and flexible way to build and train neural networks, which is particularly useful for complex tasks like NST.

## A Neural Algorithm of Artistic Style

The foundational paper for NST, "A Neural Algorithm of Artistic Style" by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge, laid the groundwork for using CNNs to separate and recombine image content and style. This implementation is inspired by their work and adapts it to modern deep learning frameworks and techniques.

## Getting Started

To run this project, you need to have TensorFlow installed. You can install it via pip:

```bash
pip install tensorflow
```

### Running the Neural Style Transfer

1. **Load the images**: Load your content and style images.
2. **Preprocess the images**: Prepare the images for the model.
3. **Build the model**: Use a pre-trained CNN, such as VGG19, to extract features.
4. **Define the loss functions**: Implement the content and style cost functions.
5. **Optimize the image**: Use gradient descent to minimize the total cost function.

### Example Code

Here is a simplified example to get you started:

```python
import tensorflow as tf
from tensorflow.keras.applications import VGG19
from tensorflow.keras.preprocessing import image as kp_image
from tensorflow.keras.models import Model
import numpy as np

# Load and preprocess images
def load_and_process_img(path_to_img):
    img = kp_image.load_img(path_to_img, target_size=(512, 512))
    img = kp_image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.vgg19.preprocess_input(img)
    return img

# Define the model
vgg = VGG19(include_top=False, weights='imagenet')
vgg.trainable = False

# Define content and style layers
content_layers = ['block5_conv2']
style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']

# Create the model
def get_model():
    outputs = [vgg.get_layer(name).output for name in (style_layers + content_layers)]
    model = Model([vgg.input], outputs)
    return model

# Compute content cost
def compute_content_cost(content_output, generated_output):
    return tf.reduce_mean(tf.square(content_output - generated_output))

# Compute style cost
def compute_style_cost(style_output, generated_output):
    def gram_matrix(input_tensor):
        result = tf.linalg.einsum('bijc,bijd->bcd', input_tensor, input_tensor)
        input_shape = tf.shape(input_tensor)
        num_locations = tf.cast(input_shape[1]*input_shape[2], tf.float32)
        return result/(num_locations)

    style_gram = gram_matrix(style_output)
    generated_gram = gram_matrix(generated_output)
    return tf.reduce_mean(tf.square(style_gram - generated_gram))

# Combine costs
def compute_total_cost(model, content_img, style_img, generated_img):
    model_outputs = model(generated_img)
    style_outputs = model_outputs[:len(style_layers)]
    content_output = model_outputs[len(style_layers):]

    style_cost = tf.add_n([compute_style_cost(style_output, gen_output)
                           for style_output, gen_output in zip(style_outputs, model(style_img)[:len(style_layers)])])
    
    content_cost = compute_content_cost(content_output[0], model(content_img)[len(style_layers)])
    
    total_cost = style_cost + content_cost
    return total_cost

# Optimizer
opt = tf.optimizers.Adam(learning_rate=0.02)

# Training step
@tf.function()
def train_step(image, model, content_img, style_img):
    with tf.GradientTape() as tape:
        total_cost = compute_total_cost(model, content_img, style_img, image)
    grad = tape.gradient(total_cost, image)
    opt.apply_gradients([(grad, image)])
    image.assign(tf.clip_by_value(image, -1.0, 1.0))

# Main function
def run_style_transfer(content_path, style_path, num_iterations=1000):
    content_img = load_and_process_img(content_path)
    style_img = load_and_process_img(style_path)
    generated_img = tf.Variable(content_img, dtype=tf.float32)
    
    model = get_model()
    
    for i in range(num_iterations):
        train_step(generated_img, model, content_img, style_img)
        if i % 100 == 0:
            print(f"Iteration {i}: cost = {compute_total_cost(model, content_img, style_img, generated_img)}")
            
    final_img = generated_img.numpy()
    return final_img

# Usage
final_image = run_style_transfer('path_to_content_image.jpg', 'path_to_style_image.jpg')
```

## Conclusion

Neural Style Transfer is a fascinating application of deep learning that blends the worlds of technology and art. This project demonstrates the use of `tf.keras` and eager execution to create stunning artworks by combining the content of one image with the style of another. Explore different content and style images to create your own unique pieces of art!

Feel free to contribute to this project or modify it to suit your creative needs. Happy coding and creating!
