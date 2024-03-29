# coding: utf-8

"""
    Web Forms API version 1.1

    The Web Forms API facilitates generating semantic HTML forms around everyday contracts.   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_webforms.models.web_form_summary import WebFormSummary  # noqa: F401,E501
from docusign_webforms.client.configuration import Configuration


class WebForm(WebFormSummary):
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
        'version_id': 'int',
        'form_content': 'WebFormContent'
    }
    if hasattr(WebFormSummary, "swagger_types"):
        swagger_types.update(WebFormSummary.swagger_types)

    attribute_map = {
        'version_id': 'versionId',
        'form_content': 'formContent'
    }
    if hasattr(WebFormSummary, "attribute_map"):
        attribute_map.update(WebFormSummary.attribute_map)

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """WebForm - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._version_id = None
        self._form_content = None
        self.discriminator = None
        WebFormSummary.__init__(self, _configuration, **kwargs)

        setattr(self, "_{}".format('version_id'), kwargs.get('version_id', None))
        setattr(self, "_{}".format('form_content'), kwargs.get('form_content', None))

    @property
    def version_id(self):
        """Gets the version_id of this WebForm.  # noqa: E501


        :return: The version_id of this WebForm.  # noqa: E501
        :rtype: int
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this WebForm.


        :param version_id: The version_id of this WebForm.  # noqa: E501
        :type: int
        """

        self._version_id = version_id

    @property
    def form_content(self):
        """Gets the form_content of this WebForm.  # noqa: E501


        :return: The form_content of this WebForm.  # noqa: E501
        :rtype: WebFormContent
        """
        return self._form_content

    @form_content.setter
    def form_content(self, form_content):
        """Sets the form_content of this WebForm.


        :param form_content: The form_content of this WebForm.  # noqa: E501
        :type: WebFormContent
        """

        self._form_content = form_content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(WebForm, dict):
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
        if not isinstance(other, WebForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebForm):
            return True

        return self.to_dict() != other.to_dict()
