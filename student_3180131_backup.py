############ CODE BLOCK 0 ################
# ^ DO NOT CHANGE THIS LINE


# Import everything in one cell
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Note: if this gives you errors, then scroll down to the section on environments

############ CODE BLOCK 1 ################
# ^ DO NOT CHANGE THIS LINE

#Implement your method here
def hello(word):
    if (word == 'World'):
        return 'Hello World!'
    elif (word == 'you'):
        return 'Hello You!'

############ CODE BLOCK 2 ################
# ^ DO NOT CHANGE THIS LINE 

def roll_array(array, steps, direction='left'):
    '''Roll the contents of a 1D array, "steps" steps in the given direction, wrapping around. '''
    if (direction == 'left'):
        steps = 0 - steps
    rolled_array = np.roll(array, steps)
    
    return rolled_array

############ CODE BLOCK 3 ################
# ^DO NOT CHANGE THIS LINE

#Implement your method here
import pandas as pd

def surface_class(frame, min_surface):
    labels = frame.loc[(frame["height"] * frame["width"]) >= min_surface, "class_labels"].values
    return labels

############ CODE BLOCK 4 ################
# ^ DO NOT CHANGE THIS LINE
 
def generate_data(
    amount=100, proportion=0.7, # By default we want 70% class a, 30% class b
    signal_a_height=5, signal_a_width=10, a_noise=2,
    signal_b_height=4, signal_b_width=6, b_noise=3,
    random_state=42  # by default, always generate the same data
):
    if random_state is not None:
        np.random.seed(random_state)
    
    # Calculate how many instances of each class to generate
    a_amount = int(amount * proportion)
    b_amount = amount - a_amount
    
    # Generate instances of class a
    # The height and width are the sum of signal + noise
    a_height = signal_a_height + (np.random.randn(a_amount) * a_noise)
    a_width = signal_a_width + (np.random.randn(a_amount) * a_noise)
    a_labels = np.full(a_amount, 'a')
    
    # Do the same for b
    b_height = signal_b_height + (np.random.randn(b_amount) * b_noise)
    b_width = signal_b_width + (np.random.randn(b_amount) * b_noise)
    b_labels = np.full(b_amount, 'b')

    # Wrap it up in a nice dataframe
    df = pd.DataFrame({
        'height': np.concatenate([a_height, b_height]),
        'width': np.concatenate([a_width, b_width]),
        'label': np.concatenate([a_labels, b_labels])
    })
    return df

############ CODE BLOCK 5 ################
#^ DO NOT CHANGE THIS LINE

class OneNearestNeighborClassifier:
    def __init__(self):
        self.y_train = None
        self.x_train = None

    def fit(self, x_train, y_train):
        """ To fit, we just store the entire training data. """
        self.x_train = x_train
        self.y_train = y_train

    def distance(self, a, b):
        """ Return the Euclidean distance between point a and b """
        return np.sqrt(np.sum((a - b)**2))

    def predict(self, x_test):
        """ Predict the label of test instances 
        
        For each test instance, find the nearest point in the training set.
        Then return a list of the labels of the nearest points that you found.
        """
        x_test = np.asarray(x_test)
        prediction = []
        dist = []
        for test in x_test:
            dist = []
            for train in x_train:
                dist.append(self.distance(test, train))
                #dist = np.array([self.distance(test, self.x_train)])
                print(dist)

            prediction.append(np.min(dist))
        print(prediction)

        if isinstance(x_test, pd.DataFrame):
            return pd.Series(prediction)

        return np.asarray(prediction)  # as a numpy array

