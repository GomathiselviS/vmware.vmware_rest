#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: appliance_monitoring_query
short_description: Get monitoring data.
description: Get monitoring data.
options:
  end_time:
    description:
    - End time in UTC This parameter is mandatory.
    required: true
    type: str
  function:
    choices:
    - AVG
    - COUNT
    - MAX
    - MIN
    description:
    - C(function_type) Defines aggregation function This parameter is mandatory.
    required: true
    type: str
  interval:
    choices:
    - DAY1
    - HOURS2
    - HOURS6
    - MINUTES30
    - MINUTES5
    description:
    - C(interval_type) Defines interval between the values in hours and mins,                    for
      which aggregation will apply This parameter is mandatory.
    required: true
    type: str
  names:
    description:
    - 'monitored item IDs Ex: CPU, MEMORY This parameter is mandatory.'
    elements: str
    required: true
    type: list
  session_timeout:
    description:
    - 'Timeout settings for client session. '
    - 'The maximal number of seconds for the whole operation including connection
      establishment, request sending and response. '
    - The default value is 300s.
    type: float
    version_added: 2.1.0
  start_time:
    description:
    - Start time in UTC This parameter is mandatory.
    required: true
    type: str
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter password
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Query the monitoring backend
  vmware.vmware_rest.appliance_monitoring_query:
    end_time: 2021-04-14T09:34:56Z
    start_time: 2021-04-14T08:34:56Z
    names:
    - mem.total
    interval: MINUTES5
    function: AVG
  register: result
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Query the monitoring backend
value:
  description: Query the monitoring backend
  returned: On success
  sample:
  - data:
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    - ''
    end_time: '2021-04-14T09:34:56.000Z'
    function: AVG
    interval: MINUTES5
    name: mem.total
    start_time: '2021-04-14T08:34:56.000Z'
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "query": {
        "query": {
            "end_time": "end_time",
            "function": "function",
            "interval": "interval",
            "names": "names",
            "start_time": "start_time",
        },
        "body": {},
        "path": {},
    }
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["end_time"] = {"required": True, "type": "str"}
    argument_spec["function"] = {
        "required": True,
        "type": "str",
        "choices": ["AVG", "COUNT", "MAX", "MIN"],
    }
    argument_spec["interval"] = {
        "required": True,
        "type": "str",
        "choices": ["DAY1", "HOURS2", "HOURS6", "MINUTES30", "MINUTES5"],
    }
    argument_spec["names"] = {"required": True, "type": "list", "elements": "str"}
    argument_spec["start_time"] = {"required": True, "type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/appliance/monitoring/query").format(
        **params
    )


async def entry_point(module, session):

    func = globals()["_query"]

    return await func(module.params, session)


async def _query(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["query"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["query"])
    subdevice_type = get_subdevice_type("/api/appliance/monitoring/query")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/appliance/monitoring/query"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.get(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "query")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
