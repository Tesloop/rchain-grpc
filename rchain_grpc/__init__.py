# hack needed becouse protc use absolute imports
import os
import sys
import CasperMessage_pb2  # isort:skip
import CasperMessage_pb2_grpc  # isort:skip
import RhoTypes_pb2  # isort:skip
import RhoTypes_pb2_grpc  # isort:skip

ROOT = os.path.dirname(__file__)
GENERATED = os.path.join(ROOT, 'generated')
sys.path.append(GENERATED)

__version__ = '0.0.9'
