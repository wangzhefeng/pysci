# -*- coding: utf-8 -*-

"""
@author:
@date:
"""


"""
# ----------------------------------------------------------------------------
## 模型中的超参数
# ----------------------------------------------------------------------------
* Decision Tree
    - 
* AdaBoost
    - n_estimators
* Bagging
    - n_estimators
* Random Forest
    - n_estimators
    - 
* SVC:
    - C
    - kernel
    - gamma
* Logistic Regression with regu 
    - C
* Lasso
    - alpha
# ----------------------------------------------------------------------------
# Find the names and current values for all parameters for a given estimator:
# ----------------------------------------------------------------------------
* estimator.get_params()


# ----------------------------------------------------------------------------
# Tuning the hyper-parameters of an estimator
# ----------------------------------------------------------------------------
# estimator
    - classifier
    - regressioner
# parameter space
    - grid_params = [
        {'param1': [], 'param2': [], ...},
        {'param1': [], 'param2': [], 'param3': []...}
      ]
    - 
# method for search or sampling candidates
    - GridSearchCV
    - RandomizeSearchCV
# cross-valdation schema
    - train_test_split
    - KFold...
    - cross_val_score
    - cross_validate
# score function
    - scoring = ['', '']

# ----------------------------------------------------------------------------
# Tips
# ----------------------------------------------------------------------------
# Specifying an objective metric
# Specifying multiple metrics for evaluation
# Composite estimators and parameter spaces
# Model selection: development and evaluation
# Parallelism
# Robustness to failure

"""


# data split
from sklearn.model_selection import train_test_split
# CV split
from sklearn.model_selection import KFold
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import LeavePOut
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GroupKFold
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.model_selection import LeavePGroupsOut
from sklearn.model_selection import GroupShuffleSplit
# CV method
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
# Model CV
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import RidgeClassifierCV
from sklearn.linear_model import LassoCV
from sklearn.linear_model import LarsCV
from sklearn.linear_model import LassoLarsCV
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.linear_model import ElasticNetCV
from sklearn.linear_model import MultiTaskElasticNetCV
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import OrthogonalMatchingPursuitCV
from sklearn.linear_model import LassoLarsIC
# OOB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor



# =======================================================================
# Methods
# =======================================================================
def train_test(X, y, test_rate = 0.2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_rate, random_state = 0)
    return X_train, X_test, y_train, y_test


def iid_cv_iterators(model, X, y, n_splits = 5, n_repeats = 100, shuffle = False, test_size = 0.3, train_size = 0.7, lpo_p = 2, random_state = 0):

    kf = KFold(n_splits = n_splits, shuffle = shuffle, random_state = random_state)
    for k, train, test in enumerate(kf.split(X)):
        model.fit(X[train], y[train])

    repeat_kf = RepeatedKFold(n_splits, n_repeats = n_repeats, random_state = random_state)
    for k, train, test in enumerate(repeat_kf.split(X)):
        model.fit(X[train], y[train])

    stra_kf = StratifiedKFold(n_splits = n_splits, shuffle = shuffle, random_state = random_state)
    for k, train, test in enumerate(stra_kf.split(X, y)):
        model.fit(X[train], y[train])

    stra_shuffle_kf = StratifiedShuffleSplit(n_splits = n_splits,
                                             test_size = test_size,
                                             train_size = train_size,
                                             random_state = random_state)
    for k, train_index, test_index in enumerate(stra_shuffle_kf.split(X, y)):
        model.fit(X[train_index], y[train_index])

    repeat_stra_kf = RepeatedStratifiedKFold(n_splits = n_splits, n_repeats = n_repeats, random_state = random_state)
    for k, train, test in enumerate(repeat_stra_kf.split(X, y)):
        model.fit(X[train], y[train])

    loo = LeaveOneOut()
    for k, train_index, test_index in enumerate(loo.split(X)):
        model.fit(X[train_index], y[train_index])

    lpo = LeavePOut(p = lpo_p)
    for k, train_index, test_index in enumerate(lpo.spit(X)):
        model.fit(X[train_index], y[train_index])



def cross_validation(model, X, y, method = "cross_validate", cv = 5, scoring = None):
    """
    Cross-Validation
    """
    if method == "cross_validate":
        scores = cross_validate(model,
                                X,
                                y,
                                cv = cv,
                                scoring = scoring,
                                return_train_score = True)
        scores_keys = sorted(scores.key())

        return scores, scores_keys
    elif method == "cross_val_score":
        scores = cross_val_score(model,
                                 X,
                                 y,
                                 cv = cv,
                                 scoring = scoring)
        return scores


def tuning_param_cv(method, model, X, y, method_cv, param_grid, param_dist, scoring, cv_inner, cv_outer, is_refit, n_iter):
    # inner_cv = iid_cross_validation_iterators()
    # outer_cv = iid_cross_validation_iterators()
    if method == "GridSearchCV":
        gscv = GridSearchCV(estimator = model,
                            param_grid = param_grid,
                            scoring = scoring,
                            n_jobs = None,
                            refit = is_refit,
                            cv = cv_inner,
                            return_train_score = True)
        gscv.fit(X, y)
        cv_result = gscv.cv_results_
        best_estimator = gscv.best_estimator_
        best_index = gscv.best_index_
        best_params = gscv.best_params_
        best_score = gscv.best_score_
        scorer = gscv.scorer_
        n_splits = gscv.n_splits_
        refit_time = gscv.refit_time_

        nested_scores = cross_validation(gscv,
                                         X,
                                         y,
                                         method = method_cv,
                                         cv = cv_outer,
                                         scoring = scoring)
        gen_scores = nested_scores.mean()

        return cv_result, best_estimator, best_index, best_params, best_score, scorer, n_splits, refit_time, gen_scores

    elif method == "RandomizedSearchCV":
        rscv = RandomizedSearchCV(estimator = model,
                                  param_distributions = param_dist,
                                  n_iter = n_iter,
                                  scoring=scoring,
                                  n_jobs = None,
                                  refit = is_refit,
                                  cv = cv_inner,
                                  return_train_score = True)
        rscv.fit(X, y)
        cv_result = rscv.cv_results_
        best_estimator = rscv.best_estimator_
        best_index = rscv.best_index_
        best_params = rscv.best_params_
        best_score = rscv.best_score_
        scorer = rscv.scorer_
        n_splits = rscv.n_splits_
        refit_time = rscv.refit_time_

        nested_scores = cross_validation(rscv,
                                         X,
                                         y,
                                         method = method_cv,
                                         cv = cv_outer,
                                         scoring = scoring)
        gen_scores = nested_scores.mean()

        return cv_result, best_estimator, best_index, best_params, best_score, scorer, n_splits, refit_time, gen_scores






