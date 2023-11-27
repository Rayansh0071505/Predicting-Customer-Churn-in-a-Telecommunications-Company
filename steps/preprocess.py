from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


def missing_value(data):

    """
    It will check for missing value if it has missing value it will drop it
    """
    for col in data.columns:
        if data[col].isna().sum() > 0:
            data = data.drop(columns=[col])
        else:
            print(col)

def binary_conversion(data):
    """
    Yes = 1 and No = 0
    """
    for col in data.columns:
        if data[col].dtypes == 'object':
            data[col] = data[col].replace({'Yes': 1, 'No': 0})


def numerical_conversion(data):
    """
    Here we do the Label Encoding
    """
    label_encoder = LabelEncoder()
    for col in data.columns:
        if data[col].dtypes == 'object':
            data[col] = data[col].astype(str)
            data[col] = label_encoder.fit_transform(data[col])

def standard_scaling(data):

    """
    Standard scaling transforms data to have a mean of zero and a standard deviation of one, aiding in normalizing features with varying scales.
    """
    scaler = StandardScaler()
    data = scaler.fit_transform(data)


