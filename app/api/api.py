import numpy as np
import re


def convert(payload):
    data = np.array(payload["list"])
    r = re.compile('[A-Ga-g]')

    converter = np.vectorize(lambda x: ord(x)*10 if bool(r.match(x)) else 0)
    result = converter(data)


    return {'result_list': result.tolist()}
