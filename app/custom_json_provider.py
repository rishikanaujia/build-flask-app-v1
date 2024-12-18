from flask.json.provider import DefaultJSONProvider
import numpy as np
import pandas as pd


class CustomJSONProvider(DefaultJSONProvider):
    """Custom JSON serialization for unsupported types."""

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.integer, np.floating)):
            return obj.item()
        elif isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        elif isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient="records")
        return super().default(obj)
