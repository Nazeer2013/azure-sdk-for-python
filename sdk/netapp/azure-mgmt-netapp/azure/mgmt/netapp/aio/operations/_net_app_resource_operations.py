# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, Union, cast

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._net_app_resource_operations import (
    build_check_file_path_availability_request,
    build_check_name_availability_request,
    build_check_quota_availability_request,
    build_query_network_sibling_set_request,
    build_query_region_info_request,
    build_update_network_sibling_set_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class NetAppResourceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.netapp.aio.NetAppManagementClient`'s
        :attr:`net_app_resource` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def check_name_availability(
        self,
        location: str,
        name: str,
        type: Union[str, _models.CheckNameResourceTypes],
        resource_group: str,
        **kwargs: Any
    ) -> _models.CheckAvailabilityResponse:
        """Check resource name availability.

        Check if a resource name is available.

        :param location: The name of Azure region. Required.
        :type location: str
        :param name: Resource name to verify. Required.
        :type name: str
        :param type: Resource type used for verification. Known values are:
         "Microsoft.NetApp/netAppAccounts", "Microsoft.NetApp/netAppAccounts/capacityPools",
         "Microsoft.NetApp/netAppAccounts/capacityPools/volumes", and
         "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots". Required.
        :type type: str or ~azure.mgmt.netapp.models.CheckNameResourceTypes
        :param resource_group: Resource group name. Required.
        :type resource_group: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckAvailabilityResponse or the result of cls(response)
        :rtype: ~azure.mgmt.netapp.models.CheckAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.CheckAvailabilityResponse] = kwargs.pop("cls", None)

        _body = _models.ResourceNameAvailabilityRequest(name=name, resource_group=resource_group, type=type)
        _json = self._serialize.body(_body, "ResourceNameAvailabilityRequest")

        request = build_check_name_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckAvailabilityResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/checkNameAvailability"
    }

    @distributed_trace_async
    async def check_file_path_availability(
        self, location: str, name: str, subnet_id: str, **kwargs: Any
    ) -> _models.CheckAvailabilityResponse:
        """Check file path availability.

        Check if a file path is available.

        :param location: The name of Azure region. Required.
        :type location: str
        :param name: File path to verify. Required.
        :type name: str
        :param subnet_id: The Azure Resource URI for a delegated subnet. Must have the delegation
         Microsoft.NetApp/volumes. Required.
        :type subnet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckAvailabilityResponse or the result of cls(response)
        :rtype: ~azure.mgmt.netapp.models.CheckAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.CheckAvailabilityResponse] = kwargs.pop("cls", None)

        _body = _models.FilePathAvailabilityRequest(name=name, subnet_id=subnet_id)
        _json = self._serialize.body(_body, "FilePathAvailabilityRequest")

        request = build_check_file_path_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_file_path_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckAvailabilityResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_file_path_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/checkFilePathAvailability"
    }

    @distributed_trace_async
    async def check_quota_availability(
        self,
        location: str,
        name: str,
        type: Union[str, _models.CheckQuotaNameResourceTypes],
        resource_group: str,
        **kwargs: Any
    ) -> _models.CheckAvailabilityResponse:
        """Check quota availability.

        Check if a quota is available.

        :param location: The name of Azure region. Required.
        :type location: str
        :param name: Name of the resource to verify. Required.
        :type name: str
        :param type: Resource type used for verification. Known values are:
         "Microsoft.NetApp/netAppAccounts", "Microsoft.NetApp/netAppAccounts/capacityPools",
         "Microsoft.NetApp/netAppAccounts/capacityPools/volumes", and
         "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots". Required.
        :type type: str or ~azure.mgmt.netapp.models.CheckQuotaNameResourceTypes
        :param resource_group: Resource group name. Required.
        :type resource_group: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckAvailabilityResponse or the result of cls(response)
        :rtype: ~azure.mgmt.netapp.models.CheckAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.CheckAvailabilityResponse] = kwargs.pop("cls", None)

        _body = _models.QuotaAvailabilityRequest(name=name, resource_group=resource_group, type=type)
        _json = self._serialize.body(_body, "QuotaAvailabilityRequest")

        request = build_check_quota_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_quota_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckAvailabilityResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_quota_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/checkQuotaAvailability"
    }

    @distributed_trace_async
    async def query_region_info(self, location: str, **kwargs: Any) -> _models.RegionInfo:
        """Describes region specific information.

        Provides storage to network proximity and logical zone mapping information.

        :param location: The name of Azure region. Required.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RegionInfo or the result of cls(response)
        :rtype: ~azure.mgmt.netapp.models.RegionInfo
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.RegionInfo] = kwargs.pop("cls", None)

        request = build_query_region_info_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.query_region_info.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RegionInfo", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_region_info.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/regionInfo"
    }

    @distributed_trace_async
    async def query_network_sibling_set(
        self, location: str, network_sibling_set_id: str, subnet_id: str, **kwargs: Any
    ) -> _models.NetworkSiblingSet:
        """Describe a network sibling set.

        Get details of the specified network sibling set.

        :param location: The name of Azure region. Required.
        :type location: str
        :param network_sibling_set_id: Network Sibling Set ID for a group of volumes sharing networking
         resources in a subnet. Required.
        :type network_sibling_set_id: str
        :param subnet_id: The Azure Resource URI for a delegated subnet. Must have the delegation
         Microsoft.NetApp/volumes. Example
         /subscriptions/subscriptionId/resourceGroups/resourceGroup/providers/Microsoft.Network/virtualNetworks/testVnet/subnets/{mySubnet}.
         Required.
        :type subnet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NetworkSiblingSet or the result of cls(response)
        :rtype: ~azure.mgmt.netapp.models.NetworkSiblingSet
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.NetworkSiblingSet] = kwargs.pop("cls", None)

        _body = _models.QueryNetworkSiblingSetRequest(
            network_sibling_set_id=network_sibling_set_id, subnet_id=subnet_id
        )
        _json = self._serialize.body(_body, "QueryNetworkSiblingSetRequest")

        request = build_query_network_sibling_set_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.query_network_sibling_set.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("NetworkSiblingSet", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_network_sibling_set.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/queryNetworkSiblingSet"
    }

    async def _update_network_sibling_set_initial(
        self,
        location: str,
        network_sibling_set_id: str,
        subnet_id: str,
        network_sibling_set_state_id: str,
        network_features: Union[str, _models.NetworkFeatures] = "Basic",
        **kwargs: Any
    ) -> Optional[_models.NetworkSiblingSet]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[Optional[_models.NetworkSiblingSet]] = kwargs.pop("cls", None)

        _body = _models.UpdateNetworkSiblingSetRequest(
            network_features=network_features,
            network_sibling_set_id=network_sibling_set_id,
            network_sibling_set_state_id=network_sibling_set_state_id,
            subnet_id=subnet_id,
        )
        _json = self._serialize.body(_body, "UpdateNetworkSiblingSetRequest")

        request = build_update_network_sibling_set_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._update_network_sibling_set_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("NetworkSiblingSet", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _update_network_sibling_set_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/updateNetworkSiblingSet"
    }

    @distributed_trace_async
    async def begin_update_network_sibling_set(
        self,
        location: str,
        network_sibling_set_id: str,
        subnet_id: str,
        network_sibling_set_state_id: str,
        network_features: Union[str, _models.NetworkFeatures] = "Basic",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NetworkSiblingSet]:
        """Update the network features of a network sibling set.

        Update the network features of the specified network sibling set.

        :param location: The name of Azure region. Required.
        :type location: str
        :param network_sibling_set_id: Network Sibling Set ID for a group of volumes sharing networking
         resources in a subnet. Required.
        :type network_sibling_set_id: str
        :param subnet_id: The Azure Resource URI for a delegated subnet. Must have the delegation
         Microsoft.NetApp/volumes. Example
         /subscriptions/subscriptionId/resourceGroups/resourceGroup/providers/Microsoft.Network/virtualNetworks/testVnet/subnets/{mySubnet}.
         Required.
        :type subnet_id: str
        :param network_sibling_set_state_id: Network sibling set state Id identifying the current state
         of the sibling set. Required.
        :type network_sibling_set_state_id: str
        :param network_features: Network features available to the volume, some such. Known values are:
         "Basic", "Standard", "Basic_Standard", and "Standard_Basic". Default value is "Basic".
        :type network_features: str or ~azure.mgmt.netapp.models.NetworkFeatures
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either NetworkSiblingSet or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.netapp.models.NetworkSiblingSet]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.NetworkSiblingSet] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_network_sibling_set_initial(
                location=location,
                network_sibling_set_id=network_sibling_set_id,
                subnet_id=subnet_id,
                network_sibling_set_state_id=network_sibling_set_state_id,
                network_features=network_features,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("NetworkSiblingSet", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_update_network_sibling_set.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/updateNetworkSiblingSet"
    }
