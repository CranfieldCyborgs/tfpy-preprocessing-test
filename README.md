# Preprocessing test

This prototype explores preprocessing data using just tensorflow.

## Todo

- [x] Read image
- [ ] Convert color
- [ ] Resize image

# Usage

Clone the project using `git clone` and then `cd` into the project.
To setup the same environment as the one required by the project in a folder called `envs` in the root of the project, create a new conda environment using:

`conda env create -f .\environment.yml -p .\envs`

> Note: The encoding of the file `environment.yml` has to be UTF-8 and not UTF-16. If you are getting the issue similar to `Issue#1` then this might be why. To change it, follow the solution referenced on the issue.

And activate it using:

`conda activate .\envs`

And finally, run the project from the root directory of the project using
`python src/main.py`.
