## GitHub and code setup

*Setup.py* is responsible for building this machine learning application as a package. For example, it allows this application to be built as a package that is deployed in PyPi, and other users can download and install this machine learning application.

The `setup()` function provides the general information about the entire project.

```python
setup(
    name='students-performance',
    version='0.0.1',
    author='Diogo',
    author_email='diogojfr1@gmail.com', 
    packages=find_packages(),
    install_requires =  get_requirements('requirements.txt')  
)
```

The `__init__.py` in the *src* (source) folder allows that folder to be built as a package when setup.py is run.

The requirements.txt file contains all the libraries required for the project. For the first building, it is required to add a line with `-e .`.

The function get_requirements takes a string (the path of requirements.txt) and and returns a list of libraries. The argument `file_path` is expected to be of type ´str´ and the return type ´List´ of strings.

```python
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements ]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
```

Building the package:
```python
pip install -r requirements.txt
```
<br>
Strcture of the project:

```bash 
|__src/ # project source folder
|   |__components/ # modules for the project
|   |   |__ __init__.py
|   |   |__data_ingestion.py
|   |   |__data_transformation.py
|   |   |__model_trainer.py
|   |__pipeline/ # pipiles for training and prediction
|   |   |__ __init__.py
|   |   |__predict_pipeline.py
|   |   |__train_pipeline.py
|   |__ __init__.py
|   |__logger.py
|   |__exception.py
|   |__utils.py
|__setup.py
|__app.py
|__artifacts/ # train and test data
|__notebook/ # EDA in jupyter notebook 
|   |__data/ # raw dataset    
|__templates/ # templates for html pages
|__requirements.txt # libraries
```