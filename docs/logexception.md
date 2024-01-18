## Logging and exception handling

- #### **exception.py**

In this project, the *exception.py* file was created to provide a custom exception function to inform the user about errors during execution.

The `CustomException()` class uses the `error_message_detail()` to return an error message and details about the error.

```python
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message =  error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
```
The `error_message_detail()` function takes two arguments: the error and its details (from the *sys* library). 
This function returns a string containing the script name, line number and a message about the error. 

```python
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in pyhton script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message
```

Usage example:
```python
if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)

```
<br>

- #### **logger.py**

The `logger.py` file uses the *logging* module of Python to generate a log.

The user provides a message to the `logging.info()` function and it returns information about the date/time and the message provided by the user.

```python
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 
)
```
Usage example:

```python
if __name__ == "__main__":
    logging.info("Logging has started")
```
<!-- 
|__src/ # project
|   |__components/ # modules for the project
|   |   |__data_ingestion.py
|   |   |__data_transformation.py
|   |   |__model_trainer.py
|   |__pipeline/ # 
|   |   |__predict_pipeline.py
|   |   |__train_pipeline.py
|   |__exception.py
|   |__logger.py
|   |__exception.py
|   |__utils.py
|__setup.py
|__artifacts/ # train and test data
|__notebook/ # EDA in jupyter notebook and raw dataset -->
