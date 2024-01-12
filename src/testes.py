models = {
                "Random Forest": 'RandomForestRegressor',
                "Decision Tree": 'DecisionTreeRegressor',
                "Gradient Boosting": 'GradientBoostingRegressor',
                "Linear Regression": 'LinearRegression',
                "XGBRegressor": 'XGBRegressor',
                "CatBoosting Regressor": 'CatBoostRegressor',
                "AdaBoost Regressor": 'AdaBoostRegressor',
            }

#print(range(len(list(models))))

report = {}

report[list(models.keys())[0]] = 0.9
print(report)