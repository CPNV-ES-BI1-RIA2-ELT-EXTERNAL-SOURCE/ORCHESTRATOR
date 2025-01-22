def get_example_config():
    return [
        {
            "pipeline1": [
                {
                    "step1": {
                        "hostname": "localhost",
                        "contactURL": "/geturl",
                        "method": "GET",
                    }
                }
            ]
        },
        {
            "pipeline2": [
                {
                    "step1": {
                        "hostname": "localhost",
                        "contactURL": "/startprocess",
                        "method": "POST",
                    }
                }
            ]
        },
    ]