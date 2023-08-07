products = {
    'Folding Chair': {
        'discount_rates':[(10,20)],
        'default_unit_price': 20.0
    },
    'Acoustic Bloc Screen': {
        'discount_rates': [[10, 12], [5, 10], [20, 18], [15, 14]],
        'default_unit_price': 50.0
    },
    'Computer Desk': {
        'discount_rates': [],
        'default_unit_price': 250.0
    },
    'Office Chair': {
        'discount_rates': [[2,5], [10,10], [5,7]],
        'default_unit_price': 125.0
    },
}

orders = {
    'SO10001':  { 
        'order_lines': [{
            'name': 'Folding Chair',
            'quantity': 15,
            'unit_price': 20.00,
            'tax_rate': 0.0875
        },
        {
            'name': 'Acoustic Bloc Screen',
            'quantity': 12,
            'unit_price': None,
            'tax_rate': 0.0875
        },
        {
            'name': 'Computer Desk',
            'quantity': 3,
            'unit_price': 200.00,
            'tax_rate': 0
        }
    ]},
    'SO10002': {
        'order_lines': [{
            'name': 'Office Chair',
            'quantity': 10,
            'unit_price': None,
            'tax_rate': 0
        },
    ]},
}