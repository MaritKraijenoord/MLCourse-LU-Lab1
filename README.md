# MLCourse-LU-Lab1
This lab contains a tutorial of the key tools to be used during the remainder of this course, as well as a few (ungraded) exercises.

## Installation
Depending on your Python environment, you may have to install a few things.

* This lab required Python 3.6 or higher.
* If you are using Anaconda, you shouldn't have to do anything.
* If you are using Google Colab, you may need to install `pytest`. 
* If you are using a different environment, you may need to install `pytest`, `numpy`, `pandas`, `matplotlib`, and `jupyter notebook`. You can do with with for example:

    `pip3 install numpy pandas matplotlib pytest jupyter notebook`

## Getting started
Run the `Lab1.ipynb` Jupyter Notebook. Depending on your choice of platform:
* Run `jupyter notebook` then select the `Lab1.ipynb` notebook in your browser.
* Upload the notebook to Google Colab and continue from there.

Once you have the notebook running, read the explanations and do the exercises.

## Finishing up
While this lab isn't graded, you can still submit it to test the procedure.
1. Copy the work you did on the exercises in the notebook to the function skeletons in `Lab1.py` in your repository directory.
2. Check if everything really works by running `pytest Lab1_test.py` from the command line. Alternatively, you can run `!python3 -m pytest Lab1_test.py` from the notebook (especially if using Google Colab).
3. If all the tests work to satisfaction, *commit* your changes to `Lab1.py` and then *push* them back to the online repository.
4. Now our autograding code will run. You can look at the "actions" tab to see the outcome. If they succeed, you're done. 
   
    If they fail, look at the test output and fix what needs fixing, then commit and push again to run the autograding again.