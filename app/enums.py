
from enum import Enum;

class JobStatus(str, Enum):
    queued="queued";
    pending="pending";
    completed="completed";
    failed="failed";