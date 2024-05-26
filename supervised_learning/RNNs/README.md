Overview
This repository contains code implementations for various topics related to Recurrent Neural Networks (RNNs) and their advanced variants, including Long Short-Term Memory (LSTM) networks and Gated Recurrent Units (GRUs). The aim is to provide hands-on examples to help you understand and implement these concepts in practical applications.

Contents
Code Implementations
MIT 6.S191: RNN

Code based on the RNN concepts covered in the MIT 6.S191 course, demonstrating basic RNN architectures and their applications.
Introduction to RNNs

Basic examples introducing the fundamental operations and use cases of RNNs.
Illustrated Guide to RNNs

Implementations that follow the visual explanations of RNNs, helping you understand their structure and functionality through code.
Illustrated Guide to LSTM’s and GRU’s

Step-by-step code examples that illustrate the workings of LSTM and GRU cells, aligning with the detailed guide explanations.
Detailed Tutorials
RNNs Tutorial, Part 1

Basic RNN implementation, covering the foundational architecture and operations of RNNs.
RNNs Tutorial, Part 2

Intermediate RNN implementations, focusing on more advanced concepts and techniques.
RNNs Tutorial, Part 3

Advanced topics in RNNs, including optimization techniques and performance improvements.
RNNs Tutorial, Part 4

Detailed implementations of RNNs, LSTMs, and GRUs.
Note: There is a slight mistake in the last equation for the GRU cell. The correct equation should be: s_t = (1 - z) * s_t-1 + z * h.
Additional Implementations
Bidirectional RNN In-depth Intuition

Code examples demonstrating the implementation of Bidirectional RNNs, showing how they can improve performance by considering context from both past and future data points.
Deep RNN

Implementation of deep RNN architectures, involving stacking multiple RNN layers to capture more complex patterns in the data.