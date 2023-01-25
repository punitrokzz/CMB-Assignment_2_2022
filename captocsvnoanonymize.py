import os
import numpy as np
import pandas as pd
from glob import glob
from nfstream import NFStreamer

file = os.path.join(os.path.dirname(__file__),*.pcap)
dataframe = []
streamdata = NFStreamer(source(file))
dataframe = streamdata.to_pandas(columns_to_anonymize=[])
dataframe.to_csv('output.zip', index = False, compression=compression_opts,os.path.dirname(__file__))