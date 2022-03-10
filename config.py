seatMapping = {
    '12931': {
        'SN1': ['MMCT', 'BVI', 'VAPI', 'BL', 'NVS', 'ST', 'BH', 'BRC', 'ANND', 'ND', 'ADI'],
        'SN2': ['MMCT', 'BVI', 'VAPI', 'BL', 'NVS', 'ST', 'BH', 'BRC', 'ANND', 'ND', 'ADI'],
        'SN3': ['MMCT', 'BVI', 'VAPI', 'BL', 'NVS', 'ST', 'BH', 'BRC', 'ANND', 'ND', 'ADI'],
        'SN4': ['MMCT', 'BVI', 'VAPI', 'BL', 'NVS', 'ST', 'BH', 'BRC', 'ANND', 'ND', 'ADI'],
        'SN5': ['MMCT', 'BVI', 'VAPI', 'BL', 'NVS', 'ST', 'BH', 'BRC', 'ANND', 'ND', 'ADI']},
    '22222': {
        'SN1': ['CSMT', 'KYN', 'NK', 'JL', 'BPL', 'JHS', 'GWL', 'AGC', 'NZM'],
        'SN2': ['CSMT', 'KYN', 'NK', 'JL', 'BPL', 'JHS', 'GWL', 'AGC', 'NZM'],
        'SN3': ['CSMT', 'KYN', 'NK', 'JL', 'BPL', 'JHS', 'GWL', 'AGC', 'NZM'],
        'SN4': ['CSMT', 'KYN', 'NK', 'JL', 'BPL', 'JHS', 'GWL', 'AGC', 'NZM'],
        'SN5': ['CSMT', 'KYN', 'NK', 'JL', 'BPL', 'JHS', 'GWL', 'AGC', 'NZM']},
    '22436': {
        'SN1': ['NDLS', 'CNB', 'PRYJ', 'BSB'],
        'SN2': ['NDLS', 'CNB', 'PRYJ', 'BSB'],
        'SN3': ['NDLS', 'CNB', 'PRYJ', 'BSB'],
        'SN4': ['NDLS', 'CNB', 'PRYJ', 'BSB'],
        'SN5': ['NDLS', 'CNB', 'PRYJ', 'BSB']},
    '12008': {
        'SN1': ['MYS', 'SBC', 'KPD', 'MAS'],
        'SN2': ['MYS', 'SBC', 'KPD', 'MAS'],
        'SN3': ['MYS', 'SBC', 'KPD', 'MAS'],
        'SN4': ['MYS', 'SBC', 'KPD', 'MAS'],
        'SN5': ['MYS', 'SBC', 'KPD', 'MAS']
    }
}

train_list = {
    '12931': {
        'train_name': 'Double Decker',
        'source': 'MMCT',
        'destination': 'ADI',
        'stations': ['MMCT', 'BVI', 'VAPI', 'BL', 'NVS', 'ST', 'BH', 'BRC', 'ANND', 'ND', 'ADI']
    },
    '22222': {
        'train_name': 'Rajdhani',
        'source': 'CSMT',
        'destination': 'NZM',
        'stations': ['CSMT', 'KYN', 'NK', 'JL', 'BPL', 'JHS', 'GWL', 'AGC', 'NZM']
    },
    '22436': {
        'train_name': 'Vande Bharat',
        'source': 'NDLS',
        'destination': 'BSB',
        'stations': ['NDLS', 'CNB', 'PRYJ', 'BSB']
    },
    '12008': {
        'train_name': 'Shatabdi Express',
        'source': 'MYS',
        'destination': 'MAS',
        'stations': ['MYS', 'SBC', 'KPD', 'MAS']
    }
}

station_name_mapping = {
    'MMCT': 'Mumbai Central',
    'BVI': 'Borivali',
    'VAPI': 'Vapi',
    'BL': 'Valsad',
    'NVS': 'Navsari',
    'ST': 'Surat',
    'BH': 'Bharuch Jn',
    'BRC': 'Vadodara Jn',
    'ANND': 'Anand Jn',
    'ND': 'Nadiad Jn',
    'ADI': 'Ahmedabad Jn',
    'NZM': 'Hazrat Nizamuddin',
    'AGC': 'Agra Cantt',
    'GWL': 'Gwalior Jn',
    'JHS': 'Jhansi Jn',
    'BPL': 'Bhopal Jn',
    'JL': 'Jalgaon Jn',
    'NK': 'Nasik Road',
    'KYN': 'Kalyan Jn',
    'CSMT': 'Mumbai CSMT',
    'NDLS': 'New Delhi',
    'CNB': 'Kanpur Central',
    'PRYJ': 'Prayagraj Jn',
    'BSB': 'Varanasi Jn',
    'MYS': 'Mysore Jn',
    'SBC': 'Ksr Bengaluru',
    'KPD': 'Kalpadi Jn',
    'MAS': 'Mgr Chennai Ctr'
}

seat_names = ['SN1', 'SN2', 'SN3', 'SN4', 'SN5']
