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

from docusign_webforms.client.configuration import Configuration


class WebFormInstance(object):
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
        'form_url': 'str',
        'instance_token': 'str',
        'token_expiration_date_time': 'datetime',
        'id': 'str',
        'form_id': 'str',
        'account_id': 'str',
        'client_user_id': 'str',
        'tags': 'list[str]',
        'status': 'InstanceStatus',
        'envelopes': 'list[WebFormInstanceEnvelopes]',
        'instance_metadata': 'WebFormInstanceMetadata',
        'form_values': 'WebFormValues'
    }

    attribute_map = {
        'form_url': 'formUrl',
        'instance_token': 'instanceToken',
        'token_expiration_date_time': 'tokenExpirationDateTime',
        'id': 'id',
        'form_id': 'formId',
        'account_id': 'accountId',
        'client_user_id': 'clientUserId',
        'tags': 'tags',
        'status': 'status',
        'envelopes': 'envelopes',
        'instance_metadata': 'instanceMetadata',
        'form_values': 'formValues'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """WebFormInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._form_url = None
        self._instance_token = None
        self._token_expiration_date_time = None
        self._id = None
        self._form_id = None
        self._account_id = None
        self._client_user_id = None
        self._tags = None
        self._status = None
        self._envelopes = None
        self._instance_metadata = None
        self._form_values = None
        self.discriminator = None

        setattr(self, "_{}".format('form_url'), kwargs.get('form_url', None))
        setattr(self, "_{}".format('instance_token'), kwargs.get('instance_token', None))
        setattr(self, "_{}".format('token_expiration_date_time'), kwargs.get('token_expiration_date_time', None))
        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('form_id'), kwargs.get('form_id', None))
        setattr(self, "_{}".format('account_id'), kwargs.get('account_id', None))
        setattr(self, "_{}".format('client_user_id'), kwargs.get('client_user_id', None))
        setattr(self, "_{}".format('tags'), kwargs.get('tags', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('envelopes'), kwargs.get('envelopes', None))
        setattr(self, "_{}".format('instance_metadata'), kwargs.get('instance_metadata', None))
        setattr(self, "_{}".format('form_values'), kwargs.get('form_values', None))

    @property
    def form_url(self):
        """Gets the form_url of this WebFormInstance.  # noqa: E501


        :return: The form_url of this WebFormInstance.  # noqa: E501
        :rtype: str
        """
        return self._form_url

    @form_url.setter
    def form_url(self, form_url):
        """Sets the form_url of this WebFormInstance.


        :param form_url: The form_url of this WebFormInstance.  # noqa: E501
        :type: str
        """

        self._form_url = form_url

    @property
    def instance_token(self):
        """Gets the instance_token of this WebFormInstance.  # noqa: E501


        :return: The instance_token of this WebFormInstance.  # noqa: E501
        :rtype: str
        """
        return self._instance_token

    @instance_token.setter
    def instance_token(self, instance_token):
        """Sets the instance_token of this WebFormInstance.


        :param instance_token: The instance_token of this WebFormInstance.  # noqa: E501
        :type: str
        """

        self._instance_token = instance_token

    @property
    def token_expiration_date_time(self):
        """Gets the token_expiration_date_time of this WebFormInstance.  # noqa: E501


        :return: The token_expiration_date_time of this WebFormInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._token_expiration_date_time

    @token_expiration_date_time.setter
    def token_expiration_date_time(self, token_expiration_date_time):
        """Sets the token_expiration_date_time of this WebFormInstance.


        :param token_expiration_date_time: The token_expiration_date_time of this WebFormInstance.  # noqa: E501
        :type: datetime
        """

        self._token_expiration_date_time = token_expiration_date_time

    @property
    def id(self):
        """Gets the id of this WebFormInstance.  # noqa: E501


        :return: The id of this WebFormInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebFormInstance.


        :param id: The id of this WebFormInstance.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def form_id(self):
        """Gets the form_id of this WebFormInstance.  # noqa: E501

        Web form from which the instance is created  # noqa: E501

        :return: The form_id of this WebFormInstance.  # noqa: E501
        :rtype: str
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this WebFormInstance.

        Web form from which the instance is created  # noqa: E501

        :param form_id: The form_id of this WebFormInstance.  # noqa: E501
        :type: str
        """

        self._form_id = form_id

    @property
    def account_id(self):
        """Gets the account_id of this WebFormInstance.  # noqa: E501


        :return: The account_id of this WebFormInstance.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this WebFormInstance.


        :param account_id: The account_id of this WebFormInstance.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def client_user_id(self):
        """Gets the client_user_id of this WebFormInstance.  # noqa: E501


        :return: The client_user_id of this WebFormInstance.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this WebFormInstance.


        :param client_user_id: The client_user_id of this WebFormInstance.  # noqa: E501
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def tags(self):
        """Gets the tags of this WebFormInstance.  # noqa: E501

        List of tags provided by the user with each request. This field is optional.  # noqa: E501

        :return: The tags of this WebFormInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WebFormInstance.

        List of tags provided by the user with each request. This field is optional.  # noqa: E501

        :param tags: The tags of this WebFormInstance.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def status(self):
        """Gets the status of this WebFormInstance.  # noqa: E501


        :return: The status of this WebFormInstance.  # noqa: E501
        :rtype: InstanceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebFormInstance.


        :param status: The status of this WebFormInstance.  # noqa: E501
        :type: InstanceStatus
        """

        self._status = status

    @property
    def envelopes(self):
        """Gets the envelopes of this WebFormInstance.  # noqa: E501

        The associated envelope that is created when the instance is submitted  # noqa: E501

        :return: The envelopes of this WebFormInstance.  # noqa: E501
        :rtype: list[WebFormInstanceEnvelopes]
        """
        return self._envelopes

    @envelopes.setter
    def envelopes(self, envelopes):
        """Sets the envelopes of this WebFormInstance.

        The associated envelope that is created when the instance is submitted  # noqa: E501

        :param envelopes: The envelopes of this WebFormInstance.  # noqa: E501
        :type: list[WebFormInstanceEnvelopes]
        """

        self._envelopes = envelopes

    @property
    def instance_metadata(self):
        """Gets the instance_metadata of this WebFormInstance.  # noqa: E501


        :return: The instance_metadata of this WebFormInstance.  # noqa: E501
        :rtype: WebFormInstanceMetadata
        """
        return self._instance_metadata

    @instance_metadata.setter
    def instance_metadata(self, instance_metadata):
        """Sets the instance_metadata of this WebFormInstance.


        :param instance_metadata: The instance_metadata of this WebFormInstance.  # noqa: E501
        :type: WebFormInstanceMetadata
        """

        self._instance_metadata = instance_metadata

    @property
    def form_values(self):
        """Gets the form_values of this WebFormInstance.  # noqa: E501


        :return: The form_values of this WebFormInstance.  # noqa: E501
        :rtype: WebFormValues
        """
        return self._form_values

    @form_values.setter
    def form_values(self, form_values):
        """Sets the form_values of this WebFormInstance.


        :param form_values: The form_values of this WebFormInstance.  # noqa: E501
        :type: WebFormValues
        """

        self._form_values = form_values

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
        if issubclass(WebFormInstance, dict):
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
        if not isinstance(other, WebFormInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebFormInstance):
            return True

        return self.to_dict() != other.to_dict()
