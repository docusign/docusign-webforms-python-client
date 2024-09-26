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


class WebFormMetadata(object):
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
        'source': 'WebFormSource',
        'type': 'WebFormType',
        'source_form_id': 'str',
        'owner': 'WebFormUserInfo',
        'sender': 'WebFormUserInfo',
        'last_modified_by': 'WebFormUserInfo',
        'form_content_modified_by': 'WebFormUserInfo',
        'form_properties_modified_by': 'WebFormUserInfo',
        'last_published_by': 'WebFormUserInfo',
        'last_enabled_by': 'WebFormUserInfo',
        'last_disabled_by': 'WebFormUserInfo',
        'archived_date_time': 'datetime',
        'created_date_time': 'datetime',
        'last_modified_date_time': 'datetime',
        'form_content_modified_date_time': 'datetime',
        'form_properties_modified_date_time': 'datetime',
        'last_published_date_time': 'datetime',
        'last_enabled_date_time': 'datetime',
        'last_disabled_date_time': 'datetime',
        'last_sender_consent_date_time': 'datetime',
        'published_slug': 'str',
        'published_component_names': 'dict(str, WebFormComponentType)'
    }

    attribute_map = {
        'source': 'source',
        'type': 'type',
        'source_form_id': 'sourceFormId',
        'owner': 'owner',
        'sender': 'sender',
        'last_modified_by': 'lastModifiedBy',
        'form_content_modified_by': 'formContentModifiedBy',
        'form_properties_modified_by': 'formPropertiesModifiedBy',
        'last_published_by': 'lastPublishedBy',
        'last_enabled_by': 'lastEnabledBy',
        'last_disabled_by': 'lastDisabledBy',
        'archived_date_time': 'archivedDateTime',
        'created_date_time': 'createdDateTime',
        'last_modified_date_time': 'lastModifiedDateTime',
        'form_content_modified_date_time': 'formContentModifiedDateTime',
        'form_properties_modified_date_time': 'formPropertiesModifiedDateTime',
        'last_published_date_time': 'lastPublishedDateTime',
        'last_enabled_date_time': 'lastEnabledDateTime',
        'last_disabled_date_time': 'lastDisabledDateTime',
        'last_sender_consent_date_time': 'lastSenderConsentDateTime',
        'published_slug': 'publishedSlug',
        'published_component_names': 'publishedComponentNames'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """WebFormMetadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._source = None
        self._type = None
        self._source_form_id = None
        self._owner = None
        self._sender = None
        self._last_modified_by = None
        self._form_content_modified_by = None
        self._form_properties_modified_by = None
        self._last_published_by = None
        self._last_enabled_by = None
        self._last_disabled_by = None
        self._archived_date_time = None
        self._created_date_time = None
        self._last_modified_date_time = None
        self._form_content_modified_date_time = None
        self._form_properties_modified_date_time = None
        self._last_published_date_time = None
        self._last_enabled_date_time = None
        self._last_disabled_date_time = None
        self._last_sender_consent_date_time = None
        self._published_slug = None
        self._published_component_names = None
        self.discriminator = None

        setattr(self, "_{}".format('source'), kwargs.get('source', None))
        setattr(self, "_{}".format('type'), kwargs.get('type', None))
        setattr(self, "_{}".format('source_form_id'), kwargs.get('source_form_id', None))
        setattr(self, "_{}".format('owner'), kwargs.get('owner', None))
        setattr(self, "_{}".format('sender'), kwargs.get('sender', None))
        setattr(self, "_{}".format('last_modified_by'), kwargs.get('last_modified_by', None))
        setattr(self, "_{}".format('form_content_modified_by'), kwargs.get('form_content_modified_by', None))
        setattr(self, "_{}".format('form_properties_modified_by'), kwargs.get('form_properties_modified_by', None))
        setattr(self, "_{}".format('last_published_by'), kwargs.get('last_published_by', None))
        setattr(self, "_{}".format('last_enabled_by'), kwargs.get('last_enabled_by', None))
        setattr(self, "_{}".format('last_disabled_by'), kwargs.get('last_disabled_by', None))
        setattr(self, "_{}".format('archived_date_time'), kwargs.get('archived_date_time', None))
        setattr(self, "_{}".format('created_date_time'), kwargs.get('created_date_time', None))
        setattr(self, "_{}".format('last_modified_date_time'), kwargs.get('last_modified_date_time', None))
        setattr(self, "_{}".format('form_content_modified_date_time'), kwargs.get('form_content_modified_date_time', None))
        setattr(self, "_{}".format('form_properties_modified_date_time'), kwargs.get('form_properties_modified_date_time', None))
        setattr(self, "_{}".format('last_published_date_time'), kwargs.get('last_published_date_time', None))
        setattr(self, "_{}".format('last_enabled_date_time'), kwargs.get('last_enabled_date_time', None))
        setattr(self, "_{}".format('last_disabled_date_time'), kwargs.get('last_disabled_date_time', None))
        setattr(self, "_{}".format('last_sender_consent_date_time'), kwargs.get('last_sender_consent_date_time', None))
        setattr(self, "_{}".format('published_slug'), kwargs.get('published_slug', None))
        setattr(self, "_{}".format('published_component_names'), kwargs.get('published_component_names', None))

    @property
    def source(self):
        """Gets the source of this WebFormMetadata.  # noqa: E501

        The source from which the webform is created. Accepted values are [templates, blank, form]  # noqa: E501

        :return: The source of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this WebFormMetadata.

        The source from which the webform is created. Accepted values are [templates, blank, form]  # noqa: E501

        :param source: The source of this WebFormMetadata.  # noqa: E501
        :type: WebFormSource
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this WebFormMetadata.  # noqa: E501

        Represents webform type. Possible values are [standalone, hasEsignTemplate]  # noqa: E501

        :return: The type of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebFormMetadata.

        Represents webform type. Possible values are [standalone, hasEsignTemplate]  # noqa: E501

        :param type: The type of this WebFormMetadata.  # noqa: E501
        :type: WebFormType
        """

        self._type = type

    @property
    def source_form_id(self):
        """Gets the source_form_id of this WebFormMetadata.  # noqa: E501

        The source form id from which the webform is created.  # noqa: E501

        :return: The source_form_id of this WebFormMetadata.  # noqa: E501
        :rtype: str
        """
        return self._source_form_id

    @source_form_id.setter
    def source_form_id(self, source_form_id):
        """Sets the source_form_id of this WebFormMetadata.

        The source form id from which the webform is created.  # noqa: E501

        :param source_form_id: The source_form_id of this WebFormMetadata.  # noqa: E501
        :type: str
        """

        self._source_form_id = source_form_id

    @property
    def owner(self):
        """Gets the owner of this WebFormMetadata.  # noqa: E501

        The user that created the form or has been transferred ownership  # noqa: E501

        :return: The owner of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this WebFormMetadata.

        The user that created the form or has been transferred ownership  # noqa: E501

        :param owner: The owner of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._owner = owner

    @property
    def sender(self):
        """Gets the sender of this WebFormMetadata.  # noqa: E501

        The user that has added their consent to the form for sending actions  # noqa: E501

        :return: The sender of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this WebFormMetadata.

        The user that has added their consent to the form for sending actions  # noqa: E501

        :param sender: The sender of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._sender = sender

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this WebFormMetadata.  # noqa: E501

        Track the user that last modified anything related to the form  # noqa: E501

        :return: The last_modified_by of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this WebFormMetadata.

        Track the user that last modified anything related to the form  # noqa: E501

        :param last_modified_by: The last_modified_by of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._last_modified_by = last_modified_by

    @property
    def form_content_modified_by(self):
        """Gets the form_content_modified_by of this WebFormMetadata.  # noqa: E501

        Track the user that last modified the form content  # noqa: E501

        :return: The form_content_modified_by of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._form_content_modified_by

    @form_content_modified_by.setter
    def form_content_modified_by(self, form_content_modified_by):
        """Sets the form_content_modified_by of this WebFormMetadata.

        Track the user that last modified the form content  # noqa: E501

        :param form_content_modified_by: The form_content_modified_by of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._form_content_modified_by = form_content_modified_by

    @property
    def form_properties_modified_by(self):
        """Gets the form_properties_modified_by of this WebFormMetadata.  # noqa: E501

        Track the user that last modified the form properties  # noqa: E501

        :return: The form_properties_modified_by of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._form_properties_modified_by

    @form_properties_modified_by.setter
    def form_properties_modified_by(self, form_properties_modified_by):
        """Sets the form_properties_modified_by of this WebFormMetadata.

        Track the user that last modified the form properties  # noqa: E501

        :param form_properties_modified_by: The form_properties_modified_by of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._form_properties_modified_by = form_properties_modified_by

    @property
    def last_published_by(self):
        """Gets the last_published_by of this WebFormMetadata.  # noqa: E501

        Track the user that last published a draft version to active  # noqa: E501

        :return: The last_published_by of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._last_published_by

    @last_published_by.setter
    def last_published_by(self, last_published_by):
        """Sets the last_published_by of this WebFormMetadata.

        Track the user that last published a draft version to active  # noqa: E501

        :param last_published_by: The last_published_by of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._last_published_by = last_published_by

    @property
    def last_enabled_by(self):
        """Gets the last_enabled_by of this WebFormMetadata.  # noqa: E501

        Track the user that last unpublished an active version  # noqa: E501

        :return: The last_enabled_by of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._last_enabled_by

    @last_enabled_by.setter
    def last_enabled_by(self, last_enabled_by):
        """Sets the last_enabled_by of this WebFormMetadata.

        Track the user that last unpublished an active version  # noqa: E501

        :param last_enabled_by: The last_enabled_by of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._last_enabled_by = last_enabled_by

    @property
    def last_disabled_by(self):
        """Gets the last_disabled_by of this WebFormMetadata.  # noqa: E501

        Track the user that last unpublished an active version  # noqa: E501

        :return: The last_disabled_by of this WebFormMetadata.  # noqa: E501
        :rtype: WebFormUserInfo
        """
        return self._last_disabled_by

    @last_disabled_by.setter
    def last_disabled_by(self, last_disabled_by):
        """Sets the last_disabled_by of this WebFormMetadata.

        Track the user that last unpublished an active version  # noqa: E501

        :param last_disabled_by: The last_disabled_by of this WebFormMetadata.  # noqa: E501
        :type: WebFormUserInfo
        """

        self._last_disabled_by = last_disabled_by

    @property
    def archived_date_time(self):
        """Gets the archived_date_time of this WebFormMetadata.  # noqa: E501

        The last time the web form was archived  # noqa: E501

        :return: The archived_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_date_time

    @archived_date_time.setter
    def archived_date_time(self, archived_date_time):
        """Sets the archived_date_time of this WebFormMetadata.

        The last time the web form was archived  # noqa: E501

        :param archived_date_time: The archived_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._archived_date_time = archived_date_time

    @property
    def created_date_time(self):
        """Gets the created_date_time of this WebFormMetadata.  # noqa: E501

        Track the time the web form was created  # noqa: E501

        :return: The created_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this WebFormMetadata.

        Track the time the web form was created  # noqa: E501

        :param created_date_time: The created_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this WebFormMetadata.  # noqa: E501

        The last time anything was modified on the form  # noqa: E501

        :return: The last_modified_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this WebFormMetadata.

        The last time anything was modified on the form  # noqa: E501

        :param last_modified_date_time: The last_modified_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date_time = last_modified_date_time

    @property
    def form_content_modified_date_time(self):
        """Gets the form_content_modified_date_time of this WebFormMetadata.  # noqa: E501

        Track the last time web form content changed.  # noqa: E501

        :return: The form_content_modified_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._form_content_modified_date_time

    @form_content_modified_date_time.setter
    def form_content_modified_date_time(self, form_content_modified_date_time):
        """Sets the form_content_modified_date_time of this WebFormMetadata.

        Track the last time web form content changed.  # noqa: E501

        :param form_content_modified_date_time: The form_content_modified_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._form_content_modified_date_time = form_content_modified_date_time

    @property
    def form_properties_modified_date_time(self):
        """Gets the form_properties_modified_date_time of this WebFormMetadata.  # noqa: E501

        Track the last time the form properties changed.  # noqa: E501

        :return: The form_properties_modified_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._form_properties_modified_date_time

    @form_properties_modified_date_time.setter
    def form_properties_modified_date_time(self, form_properties_modified_date_time):
        """Sets the form_properties_modified_date_time of this WebFormMetadata.

        Track the last time the form properties changed.  # noqa: E501

        :param form_properties_modified_date_time: The form_properties_modified_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._form_properties_modified_date_time = form_properties_modified_date_time

    @property
    def last_published_date_time(self):
        """Gets the last_published_date_time of this WebFormMetadata.  # noqa: E501

        Track the last time a draft version was published to active  # noqa: E501

        :return: The last_published_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_published_date_time

    @last_published_date_time.setter
    def last_published_date_time(self, last_published_date_time):
        """Sets the last_published_date_time of this WebFormMetadata.

        Track the last time a draft version was published to active  # noqa: E501

        :param last_published_date_time: The last_published_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._last_published_date_time = last_published_date_time

    @property
    def last_enabled_date_time(self):
        """Gets the last_enabled_date_time of this WebFormMetadata.  # noqa: E501

        Track the last time the form was enabled  # noqa: E501

        :return: The last_enabled_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_enabled_date_time

    @last_enabled_date_time.setter
    def last_enabled_date_time(self, last_enabled_date_time):
        """Sets the last_enabled_date_time of this WebFormMetadata.

        Track the last time the form was enabled  # noqa: E501

        :param last_enabled_date_time: The last_enabled_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._last_enabled_date_time = last_enabled_date_time

    @property
    def last_disabled_date_time(self):
        """Gets the last_disabled_date_time of this WebFormMetadata.  # noqa: E501

        Track the last time the form was disabled  # noqa: E501

        :return: The last_disabled_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_disabled_date_time

    @last_disabled_date_time.setter
    def last_disabled_date_time(self, last_disabled_date_time):
        """Sets the last_disabled_date_time of this WebFormMetadata.

        Track the last time the form was disabled  # noqa: E501

        :param last_disabled_date_time: The last_disabled_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._last_disabled_date_time = last_disabled_date_time

    @property
    def last_sender_consent_date_time(self):
        """Gets the last_sender_consent_date_time of this WebFormMetadata.  # noqa: E501

        Track the last time a user added their consent for the form.  # noqa: E501

        :return: The last_sender_consent_date_time of this WebFormMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_sender_consent_date_time

    @last_sender_consent_date_time.setter
    def last_sender_consent_date_time(self, last_sender_consent_date_time):
        """Sets the last_sender_consent_date_time of this WebFormMetadata.

        Track the last time a user added their consent for the form.  # noqa: E501

        :param last_sender_consent_date_time: The last_sender_consent_date_time of this WebFormMetadata.  # noqa: E501
        :type: datetime
        """

        self._last_sender_consent_date_time = last_sender_consent_date_time

    @property
    def published_slug(self):
        """Gets the published_slug of this WebFormMetadata.  # noqa: E501

        The public friendly slug that is used to access the form from the player  # noqa: E501

        :return: The published_slug of this WebFormMetadata.  # noqa: E501
        :rtype: str
        """
        return self._published_slug

    @published_slug.setter
    def published_slug(self, published_slug):
        """Sets the published_slug of this WebFormMetadata.

        The public friendly slug that is used to access the form from the player  # noqa: E501

        :param published_slug: The published_slug of this WebFormMetadata.  # noqa: E501
        :type: str
        """

        self._published_slug = published_slug

    @property
    def published_component_names(self):
        """Gets the published_component_names of this WebFormMetadata.  # noqa: E501

        A dictionary containing the mapping of component names to their respective component types for all the published components.  # noqa: E501

        :return: The published_component_names of this WebFormMetadata.  # noqa: E501
        :rtype: dict(str, WebFormComponentType)
        """
        return self._published_component_names

    @published_component_names.setter
    def published_component_names(self, published_component_names):
        """Sets the published_component_names of this WebFormMetadata.

        A dictionary containing the mapping of component names to their respective component types for all the published components.  # noqa: E501

        :param published_component_names: The published_component_names of this WebFormMetadata.  # noqa: E501
        :type: dict(str, WebFormComponentType)
        """

        self._published_component_names = published_component_names

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
        if issubclass(WebFormMetadata, dict):
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
        if not isinstance(other, WebFormMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebFormMetadata):
            return True

        return self.to_dict() != other.to_dict()
