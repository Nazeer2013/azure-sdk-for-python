# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=redefined-builtin

from typing import Dict, overload

from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.constants._component import IOConstants

from .base import _InputOutputBase
from .utils import _remove_empty_values


class Output(_InputOutputBase):
    """Define an output of a Component or Job.

    :param type: The type of the data output. Possible values include:
                        'uri_folder', 'uri_file', 'mltable', 'mlflow_model', 'custom_model', and user-defined types.
    :type type: str
    :param path: The path to which the output is pointing. Needs to point to a cloud path.
    :type path: str
    :param mode: The mode of the data output. Possible values are:
                        'rw_mount': Read-write mount the data,
                        'upload': Upload the data from the compute target,
                        'direct': Pass in the URI as a string
    :type mode: str
    :param description: Description of the output
    :type description: str
    """

    @overload
    def __init__(self, type="uri_folder", path=None, mode=None, description=None):
        """Define a uri_folder output.

        :param type: The type of the data output. Possible values include:
                            'uri_folder', 'uri_file', 'mltable', 'mlflow_model', 'custom_model', and user-defined types.
        :type type: str
        :param path: The path to which the output is pointing. Needs to point to a cloud path.
        :type path: str
        :param mode: The mode of the data output. Possible values are:
                            'rw_mount': Read-write mount the data,
                            'upload': Upload the data from the compute target,
                            'direct': Pass in the URI as a string
        :type mode: str
        :param description: Description of the output
        :type description: str
        """

    @overload
    def __init__(self, type="uri_file", path=None, mode=None, description=None):
        """Define a uri_file output.

        :param type: The type of the data output. Possible values include:
                            'uri_folder', 'uri_file', 'mltable', 'mlflow_model', 'custom_model', and user-defined types.
        :type type: str
        :param path: The path to which the output is pointing. Needs to point to a cloud path.
        :type path: str
        :param mode: The mode of the data output. Possible values are:
                            'rw_mount': Read-write mount the data,
                            'upload': Upload the data from the compute target,
                            'direct': Pass in the URI as a string
        :type mode: str
        :param description: Description of the output
        :type description: str
        """

    def __init__(self, *, type=AssetTypes.URI_FOLDER, path=None, mode=None, description=None, **kwargs):
        super(Output, self).__init__(type=type)
        # As an annotation, it is not allowed to initialize the name.
        # The name will be updated by the annotated variable name.
        self.name = None
        self._is_primitive_type = self.type in IOConstants.PRIMITIVE_STR_2_TYPE
        self.description = description

        self.path = path
        self.mode = mode
        # use this field to determine the Output is control or not, currently hide in kwargs
        self.is_control = kwargs.pop("is_control", None)

    def _get_hint(self, new_line_style=False):
        comment_str = self.description.replace('"', '\\"') if self.description else self.type
        return '"""%s"""' % comment_str if comment_str and new_line_style else comment_str

    def _to_dict(self, remove_name=True):
        """Convert the Output object to a dict."""
        keys = ["name", "path", "type", "mode", "description", "is_control"]
        if remove_name:
            keys.remove("name")
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    def _to_rest_object(self) -> Dict:
        # this is for component rest object when using Output as component outputs, as for job output usage,
        # rest object is generated by extracting Output's properties, see details in to_rest_data_outputs()
        return self._to_dict()

    @classmethod
    def _from_rest_object(cls, obj: Dict) -> "Output":
        # this is for component rest object when using Output as component outputs
        return Output(**obj)