# General Readme

## Hyperparameter

In machine learning, a hyperparameter is a configuration setting external to the model that cannot be learned from the data. These parameters influence the learning process, affecting the model's performance and generalization. Examples include learning rates, batch sizes, and regularization strengths.

## Normalization of Input Data

Normalization is the process of scaling input features to a standard range, typically between 0 and 1 or -1 and 1. This is done to ensure that all features contribute equally to the learning process, preventing one feature from dominating due to its larger scale. Normalization is crucial for algorithms sensitive to input scale, such as neural networks.

## Saddle Point

A saddle point is a critical point in the optimization landscape where the gradient is zero but is neither a minimum nor a maximum. It poses challenges for optimization algorithms like gradient descent, as they might stall or slow down around saddle points. Techniques like momentum and adaptive learning rates help navigate through saddle points.

## Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent is an optimization algorithm used to minimize the cost function in machine learning. It updates model parameters by computing the gradient of the cost function with respect to the parameters using only a subset (a single example or a small batch) of the training data.

## Mini-Batch Gradient Descent

Mini-Batch Gradient Descent is a variation of SGD that divides the training data into small batches. It strikes a balance between the efficiency of stochastic gradient descent and the stability of batch gradient descent, offering faster convergence and reduced memory requirements.

## Moving Average

A moving average is a statistical calculation used to analyze data points over a certain period, smoothing out short-term fluctuations to highlight longer-term trends or patterns. It is commonly employed in optimization algorithms to stabilize convergence and reduce noise in parameter updates.

## Gradient Descent with Momentum

Gradient Descent with Momentum is an optimization technique that introduces a moving average of past gradients to speed up convergence and reduce oscillations. It helps the algorithm continue moving in the same direction, especially through flat regions or saddle points.

## RMSProp

Root Mean Square Propagation (RMSProp) is an adaptive learning rate optimization algorithm. It adjusts the learning rates for each parameter based on the historical magnitudes of their gradients. RMSProp helps overcome issues like vanishing or exploding gradients.

## Adam Optimization

Adam (short for Adaptive Moment Estimation) is a popular optimization algorithm that combines ideas from momentum and RMSProp. It maintains both a running average of past gradients and their squared values, adapting the learning rates for each parameter individually.

## Learning Rate Decay

Learning rate decay is the gradual reduction of the learning rate during training. This helps the optimization process by starting with a larger learning rate for faster initial progress and then decreasing it as the algorithm approaches convergence, allowing for finer adjustments.

## Batch Normalization

Batch Normalization is a technique to improve the training stability and speed of deep neural networks. It normalizes the input of each layer by adjusting and scaling the activations. This not only accelerates training but also makes the network less sensitive to hyperparameter choices.

**Note:** Implementation details and code samples for these concepts may vary depending on the specific machine learning library or framework used. Check the documentation of the chosen tool for detailed instructions.