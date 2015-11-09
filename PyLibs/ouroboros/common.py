import os
import sys
import io
import json
import time
import struct
import shutil
import asyncio
import traceback
import configparser
import xml.etree.ElementTree as ET
import xmltodict

from ctypes.wintypes import *
from ctypes import windll, cdll, byref, wintypes

ANSI_CODE_PAGE = 'mbcs'
