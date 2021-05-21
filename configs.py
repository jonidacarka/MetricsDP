files_path = "test/"  # path of files to read and calculate
include_types = ['csv']  # file types to consider, might add xlsx or similar
exclude_strings = ['________']  # files to exclude (have this, helpful for some rare cases)

sorting_orders = [
    {  # initial order, right now done through prediction, insert order, size, then id
        'prediction': False,
        'order_id': True
    },
    {  # perfect order, actual, size, insert order
        'actual': False,
        'size': True,
        'order_id': True
    },
    {  # Optimal order, right now done through actual, insert order
        'actual': False,
        'order_id': True
    },
    {  # Worst order, right now done through prediction_1(negated actual), insert order
        'prediction_1': False,
        'order_id': True
    }
]
start_value = 10  # start value for pop
end_value = 50  # end value for pop
step = 5  # steps


def get_configs(): # for file name
    return f"{start_value}___{end_value}___{step}"


normalize_json = {
    'IFA': {
        'optimal': 0,
        'worst': 'x',

    },
    'precision_0_5': {
        'optimal': 1,
        'worst': 0
    },
    'recall': {
        'optimal': 1,
        'worst': 0
    },
    'f1_score': {
        'optimal': 1,
        'worst': 0
    },
    'MAP': {
        'optimal': 1,
        'worst': 0
    },
    'auc': {
        'optimal': 1,
        'worst': 0,
    },
    'g_measure': {
        'optimal': 1,
        'worst': 0
    },
    'mcc': {
        'optimal': 1,
        'worst': 0
    },
    'pop': {
        'optimal': 1,
        'worst': 0
    }
}
popx = {
    'optimal': 1,
    'worst': 0
}
