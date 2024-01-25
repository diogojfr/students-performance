## Data Trasformation

The data transformation is initiated by setting the path where the preprocessor object will be stored. This task is performed by the `DataTransformationConfig` class.

```python
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
```

In the `DataTransformation` class, the `get_data_transformer_obj` function returns the preprocessor object that will perform the imputation, scaling, and encoding of the categorical/numeric variables.

The second function, `initiate_data_transformation`, takes as input arguments the paths for the train/test data. This function applies the preprocessor object to the train/test data frame and returns arrays with the transformed data. 

The preprocessor object is saved as a pickle file using the `save_object` function. The `save_object` function is available in the `utils.py` script.

```python
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        """
        This function is responsible for data transformation
        """
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # Imputing and scaling the numerical columns
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
                ]
            )

            #Imputing, encoding and scaling the categorical columns
            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}") 

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )  

            # retuning the modified dataset
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path) 

            logging.info('Reading train and test data completed')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj=self.get_data_transformer_obj()

            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            # getting X_train
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)

            # getting y_train
            target_feature_train_df=train_df[target_column_name]

            # getting X_test
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)

            # getting y_test 
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
        
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)

            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
```