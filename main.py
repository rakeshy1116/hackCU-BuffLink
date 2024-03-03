import sys
sys.path.insert(1, './parser/')

from dynamo.aws_dynamo import upload_to_dynamo
from parse_calendar import get_data_list

data_list = []
data_list = get_data_list()
upload_to_dynamo(data_list)

