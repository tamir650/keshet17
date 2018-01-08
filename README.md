# Introduction to Data Science

## Installation

Download the repository

    Download as zip file from the green button on hte top right area or use git:  
    git clone https://github.com/tamir650/keshet17


To install virtualenv on your computer using terminal (this may require running with `sudo`):

    pip install virtualenv

OR

    pip install --install-option="--prefix=$HOME/local" virtualenv

To create a new virtual enviroment directory:

    mkdir ~/virtual_environment

To create a new virtualenv introduction_to_data_science in the ~/virtual_environment work directory (when virtualenv is not in the local directory):

    virtualenv ~/virtual_environment/introduction_to_data_science

OR

    $HOME/local/virtualenv ~/virtual_environment/introduction_to_data_science

Activate the new virtualenv:

    source ~/virtual_environment/introduction_to_data_science/bin/activate

To install the dependencies:

    pip install -r requirements.txt

