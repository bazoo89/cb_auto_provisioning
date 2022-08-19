# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Gio Corp
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    ProcessingResponse,
    ScheduledExecutionResponse,
    ValidationResponse,
)
#from requests_oauthlib import OAuth1Session


class Loops_as_a_serviceExtension(Extension):

    #async def process_asset_purchase_request(self, request):
    #    self.logger.info(f"Obtained request with id {request['id']}")
    #    return ProcessingResponse.done()

    #async def validate_asset_purchase_request(self, request):
    #    self.logger.info(f"Obtained request with id {request['id']}")
    #    return ValidationResponse.done(request)

    #async def execute_scheduled_processing(self, schedule):  # pragma: no cover
    #    self.logger.info(
    #        f"Received event for schedule  {schedule['id']}",
    #    )
    #    return ScheduledExecutionResponse.done()
    
    def execute_scheduled_processing(self, schedule):  # pragma: no cover
        self.logger.info(
            f"Received event for schedule  {schedule['id']}",
        )
        return ScheduledExecutionResponse.done()

    def approve_asset_request(self, request, template_id):
        self.testExternalCall()
        self.logger.info(f'request_id={request["id"]} - template_id={template_id}')
        self.client.requests[request['id']]('approve').post(
            {
                'template_id': template_id,
            }
        )
        self.logger.warning(f"Approved request {request['id']}")

    def process_asset_purchase_request(self, request): # This example function processes purchase subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    def process_asset_change_request(self, request): # This example function processes change subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    def process_asset_cancel_request(self, request): # This example function processes cancel subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    def process_asset_suspend_request(self, request): # This example function processes suspend subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            #self.testExternalCall()
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()
 
    def process_asset_resume_request(self, request): # This example function processes resume subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    """def testExternalCall(self):
        CONSUMER_KEY = ""
        CONSUMER_SECRET = ""

        host = "cbc.demo.cloudblue.com"
        uri = "/aps/2/services/order-manager/orders?like(orderNumber,*CL000058)"

        oauthRequest = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
        url = 'https://' + host + uri

        headers = {
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate",
        }

        response = oauthRequest.get(url, headers=headers)

        print(response.status_code)
        print(response.content) """