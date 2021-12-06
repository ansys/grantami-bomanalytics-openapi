# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import Model


class CommonIndicatorResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'flag': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'flag': 'Flag'
    }

    subtype_mapping = {
    }


    def __init__(self, name=None, flag=None):  # noqa: E501
        """CommonIndicatorResult - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._flag = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if flag is not None:
            self.flag = flag

    @property
    def name(self):
        """Gets the name of this CommonIndicatorResult.  # noqa: E501

        :return: The name of this CommonIndicatorResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommonIndicatorResult.

        :param name: The name of this CommonIndicatorResult.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def flag(self):
        """Gets the flag of this CommonIndicatorResult.  # noqa: E501

        :return: The flag of this CommonIndicatorResult.  # noqa: E501
        :rtype: str
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this CommonIndicatorResult.

        :param flag: The flag of this CommonIndicatorResult.  # noqa: E501
        :type: str
        """
        self._flag = flag

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CommonIndicatorResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CommonIndicatorResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
