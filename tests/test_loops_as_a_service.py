# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Gio Corp
# All rights reserved.
#
import pytest

from loops_connect_ext.extension import Loops_as_a_serviceExtension


@pytest.mark.asyncio
async def test_process_asset_purchase_request(
    async_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = await async_client_factory(responses)
    ext = Loops_as_a_serviceExtension(client, logger, config)
    result = await ext.process_asset_purchase_request(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_validate_asset_purchase_request(
    async_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = await async_client_factory(responses)
    ext = Loops_as_a_serviceExtension(client, logger, config)
    result = await ext.validate_asset_purchase_request(request)
    assert result.status == 'success'
    assert result.data == request


@pytest.mark.asyncio
async def test_execute_scheduled_processing(
    async_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = await async_client_factory(responses)
    ext = Loops_as_a_serviceExtension(client, logger, config)
    result = await ext.execute_scheduled_processing(request)
    assert result.status == 'success'
