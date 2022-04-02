import sys

sys.path.append("..")

from ossapi import OssapiV2
from settings import OSU_CLIENT, OSU_REDIRECT_URI, OSU_TOKEN

api = OssapiV2(OSU_CLIENT, OSU_TOKEN, OSU_REDIRECT_URI)
