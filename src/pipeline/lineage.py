import hashlib
import json
import datetime
from utils.logger import logger

def compute_file_hash(file_path: str) -> str:
    """Compute SHA256 hash of a file for lineage tracking."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def validate_schema(record: dict, schema: dict) -> bool:
    """Validate a single record against a schema definition."""
    for field, dtype in schema.items():
        if field not in record:
            logger.warning(f"⚠️ Missing field: {field}")
            return False
        if dtype == "string" and not isinstance(record[field], str):
            logger.warning(f"⚠️ Field {field} expected string, got {type(record[field])}")
            return False
        if dtype == "datetime":
            try
