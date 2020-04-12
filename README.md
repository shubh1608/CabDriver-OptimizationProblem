# Cab Driver Profit Optimization

#### Project Status: [Completed]

## Project Objective
Imagine you are working for a leading app-based cab provider in a large metro city, In this highly competitive industry, retention of good cab drivers is a crucial business driver, and we believe that a sound RL-based system for assisting cab drivers can potentially retain and attract new cab drivers. 

### Partner
* Swayam Nanda
   * email: nanda.swayam@gmail.com

### Methods Used
* Reinforcement Learning
* Neural Network
* Q-Learning 
* Markov Decision Process

### Tools/Technologies
* Python
* Jupyter Notebook
* VS Code

## Project Description
* We wanted to develop a RL based system which can hep cab drivers maximise their profits by augmenting them in taking the right decisions when accepting reuests.
* This RL based system will use Q-Learning algorithm for interacting with the environment and maximising Total rewards, also we are using Neural Networks for approximating Q-Value function.
* The need for choosing the "Right" requests
   * Drivers receive multiple requests and they have the option to choose from them, their profits depends on their decision that's why it is important for the drivers to choose rides which are likely to maximise their profits. Let's see how below.
   * For example, say a driver gets three ride requests at 5 PM. The first one is a long-distance ride guaranteeing high fare, but it will take him to a location which is unlikely to get him another ride for the next few hours. The second one ends in a better location, but it requires him to take a slight detour to pick the customer up, adding to fuel costs. Perhaps the best choice is to choose the third one, which although is medium-distance, it will likely get him another ride subsequently and avoid most of the traffic.
   * There are some basic rules governing the ride-allocation system. If the cab is already in use, then the driver won’t get any requests. Otherwise, he may get multiple request(s). He can either decide to take any one of these requests or can go ‘offline’, i.e., not accept any request at all. 

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Open Jupyter Notebook and first set the number of episodes to a small value and start training, make a note of hyperparameters.
3. If everything is running fine, then you can start tuning hyperparameters.
4. After tuning the hyperparameters, see if we can maximise the Total Rewards.
5. As a lost resort you can experiment with the neural network architecture also it you think it is not able to pick optimal action.


## Contact
* Shubham Patel, email: shubhampatel1608@gmail.com, mobile: 8103856241
