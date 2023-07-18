from sklearn import linear_model
from sklearn.metrics import r2_score


def regression_func(X, Y, fit_intercept):
    reg = linear_model.LinearRegression(fit_intercept = fit_intercept).fit(X, Y)
    if fit_intercept:
        coefs = reg.coef_
        intercept = reg.intercept_
        R2 = reg.score(X, Y)

        return coefs, intercept, R2
    else:
        coefs = reg.coef_
        R2 = reg.score(X, Y)

        return coefs, R2