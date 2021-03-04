# Generate a list of even numbers

In this small project, we look at multiple variations on how we may structure the code in Python to generate a list of even numbers.

## 1. Set up your environment

Python 3 must be installed and available in your PATH environment variable.

``` bash
# check that you have the right python version
> python --version
Python 3.9.0

# check that you have pip installed
> python -m pip --version
pip 21.0.1 from [....]

# install project requirements
> python -m pip install -r requirements.txt

```

## 2. Design choices

What is the best way to structure this small application?

We start with two assumptions:

1. the application will run locally (installed on your machine)
2. the values passed as either integers or floats.

Then, we should dive deeper into the problem and answer some questions that will help us come up with an acceptable design:

* Which values are going to be volatile? And which ones, static?
* What type of inputs are we expecting to be passed in the program?



------------

## 3. The most suitable version

``` python

def generate_list(start, end):
    """Returns a list of even numbers."""
    if start < end:
        even_numbers_list = [x for x in range(start, end) if x % 2 == 0]
        return even_numbers_list
    else:
        raise ValueError(f"{start} is not smaller than {end}.")

```

Here are two ponints regarding the design choices.

* I didn't hardcode the start and end values. This allows the function to return a list of even numbers across different ranges.
* I used a conditional statement instead of passing the count parameter (with value 2) in the range function. This is to avoid returning an incorrect list in the case the start value of the range is an odd number.